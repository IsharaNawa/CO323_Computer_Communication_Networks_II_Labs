/* Sample UDP server */
#include <sys/socket.h>
#include <netinet/in.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

void capitalize(char * sentence);

int main(int argc, char ** argv) {
	
	int sockfd, n,client_sock;
	struct sockaddr_in servaddr, cliaddr;
	socklen_t len;
	char mesg[1000];
	
	// Create a socket
	//socket is a number therefore it is int
	//AF_INET : Create a socket for ip addressing internet
	//SOCK_DGRAM : Transport Layer Protocol
	//0 specifies the socket protocol(default value is 0) 
	sockfd = socket(AF_INET, SOCK_STREAM, 0);
	// Initialize server address
	servaddr.sin_family = AF_INET;						//sin_family specifies the family of the server
	servaddr.sin_addr.s_addr = htonl(INADDR_ANY);		//sin_addr.s_addr specifies to take the ip of the server automatically
	servaddr.sin_port = htons(32000);					//sin_port specifies the port of the server

	// Bind the socket
	// Bind the socket
	//first argument is the socket
	//second argument is the server
	//third argument is the size of the server
	bind(sockfd, (struct sockaddr * ) & servaddr, sizeof(servaddr));

	listen(sockfd, 1);
	
	// Send and Receive
	len = sizeof(cliaddr);
	client_sock = accept(sockfd, (struct sockaddr*)&cliaddr, &len);

	//receive from : getting the message from the client
	//n is the value of the recvfrom(if >0 then not successful)
	//first argument defines the socket
	//second argument defines the variable to receive the message
	//third argument defines the size of the message
	//fourth argument defines the 0 defaul value
	//fifth argument defiens the client 
	//sixth argument defines the size of the client
	n = recv(client_sock, mesg, sizeof(mesg), 0);
	mesg[n] = 0;

	int number = atoi(mesg);

	//printing the message from the client
	printf("Number of sentences : %d\n", number);

	//send some data to the client
	//first argument : socket
	//second argument : message to send
	//third argument : size of the message
	//fourth argument : 0 default value
	//fifth argument : client
	//size of the client
	send(client_sock, "ack", strlen("ack"), 0);

	printf("Waiting for sentences...\n");

	int counter;

	for(counter=0;counter<number;counter++){
		n = recv(client_sock, mesg, sizeof(mesg), 0);
		mesg[n] = 0;
		printf("Sentence %d : %s", counter+1,mesg);
		capitalize(mesg);
		send(client_sock, mesg, strlen(mesg), 0);
		printf("Waiting for sentences...\n");
	}

	//close(client_sock);
    //close(sockfd);

	return 0;
}

void capitalize(char * sentence){

	int counter;

	for(counter=0;sentence[counter]!='\0';counter++){
		int ch = sentence[counter];
		if(ch>=97 && ch<=122){
                ch -= 32;
                sentence[counter] = ch;
        }
	}

}

