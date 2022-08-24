#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct User {
	char* username;
	char password[8];
};


struct User* users[10];


void signup() {
	printf("create user in which slot?\n");
    char buf[8];
    fgets(buf, 8, stdin);
    int choice = atoi(buf);
    if(choice < 0 || choice >= 10) {
    	printf("not a valid index...\n");
    }
    char username[128];
    memset(username, 0, 128);
    fgets(username, 128, stdin);
    if(strcmp(username, "admin") == 0) {
    	printf("you can't make an admin account lol\n");
    }
    struct User* new_user = malloc(sizeof(struct User));
    new_user->username = strdup(username);
    fgets(new_user->password,8,stdin);
    users[choice] = new_user;
}

void login() {
	printf("login as which user?\n");
    char buf[8];
    fgets(buf, 8, stdin);
    int choice = atoi(buf);
    if(choice < 0 || choice >= 10) {
    	printf("not a valid index...\n");
    }
    printf("whats the password?\n");
	char pw[128];
    memset(pw, 0, 128);
    fgets(pw, 128, stdin);
    if(strcmp(users[choice]->username, "admin") == 0 && strcmp(pw, users[choice]->password) == 0) {
		char flag[64];
		FILE* f = fopen("flag.txt", "r");
		if(f == 0) {
			printf("make a dummy flag file :)\n");
			exit(1);
		}
		fgets(flag, 64, f);
		puts(flag);
    }
}

void delete() {
	printf("delete which user?\n");
    char buf[8];
    fgets(buf, 8, stdin);
    int choice = atoi(buf);
    if(choice < 0 || choice >= 10) {
    	printf("not a valid index...\n");
    }
    free(users[choice]->username);
}

void forgot() {
    char* msg = malloc(32);
    memset(msg, 0, 32);
    fgets(msg, 32, stdin);
}

void menu() {
    printf("1. Sign up!\n");
    printf("2. Login\n");
    printf("3. Delete account\n");
    printf("4. Forgot password\n");
    printf("> ");
    char buf[8];
    fgets(buf, 8, stdin);
    int choice = atoi(buf);

    if (choice == 1) {
        signup();
    } else if (choice == 2) {
        login();
    } else if (choice == 3) {
        delete();
    } else if (choice == 4) {
        forgot();
    } else {
    	printf("um lmao thats not an option\n");
    }
}

void main() {
	setvbuf(stdout, 0, _IONBF,0);
	setvbuf(stdin, 0, _IONBF,0);
	setvbuf(stderr, 0, _IONBF,0);
	while(1) {
		menu();
	}
}
