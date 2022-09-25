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
	char sendline[1000];
	char recvline[1000];

	if (argc != 2) {
		printf("usage:%s <IP address>\n", argv[0]);
		return -1;
	}

	printf("Enter the message : ");
	fgets(sendline,1000,stdin);

	// Create a socket
	sockfd = socket(AF_INET, SOCK_DGRAM, 0);

	// Initialize server address
	bzero( & servaddr, sizeof(servaddr));
	
	servaddr.sin_family = AF_INET;
	servaddr.sin_addr.s_addr = inet_addr(argv[1]);
	servaddr.sin_port = htons(32000);
	
	// Send and Receive
	sendto(sockfd, sendline, strlen(sendline), 0, (struct sockaddr * ) & servaddr,
	sizeof(servaddr));

	n = recvfrom(sockfd, recvline, 10000, 0, NULL, NULL);
	recvline[n] = 0;
	printf("Echoing back from the server: %s", recvline);
	return 0;
}
