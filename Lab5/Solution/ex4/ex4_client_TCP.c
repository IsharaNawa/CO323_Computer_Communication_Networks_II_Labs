/* Sample UDP client */
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char ** argv) {
	
	int sockfd, n;
	struct sockaddr_in servaddr;
	char recvline[1000];

	if (argc != 2) {
		printf("usage:%s <IP address>\n", argv[0]);
		return -1;
	}

	char noOfSentences[4];
	printf("Enter the number of sentences: ");
	scanf("%s",noOfSentences);

	// Create a socket
	sockfd = socket(AF_INET, SOCK_STREAM, 0);

	// Initialize server address
	bzero( & servaddr, sizeof(servaddr));
	
	servaddr.sin_family = AF_INET;
	servaddr.sin_addr.s_addr = inet_addr(argv[1]);
	servaddr.sin_port = htons(32000);

	connect(sockfd, (struct sockaddr*)&servaddr, sizeof(servaddr));

	send(sockfd, noOfSentences, strlen(noOfSentences), 0);

	n=recv(sockfd, recvline, sizeof(recvline), 0);
	recvline[n] = 0;
	printf("Message from the server : %s\n", recvline);

	int number = atoi(noOfSentences);
	int counter;
	char sentence[1000];

	for(counter=0;counter<number+1;counter++){

		
		if(counter==0){
			fgets(sentence, 1000, stdin);
			continue;
		}

		printf("Enter the %d sentence: " ,counter);
		fgets(sentence, 1000, stdin);
		send(sockfd, sentence, strlen(sentence), 0);
		n=recv(sockfd, recvline, sizeof(recvline), 0);
		recvline[n] = 0;
		printf("Message from the server : %s", recvline);

	}	
	
	return 0;
}
