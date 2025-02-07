// A C program to demonstrate stack overflow
#include <stdio.h>

void func3() {
    char temp[100]={0};
    char courseid[8];
    char buffer[12];

    printf("Input our course number\n");
    scanf("%s", courseid);
    printf("Input anything you want without space\n");
    scanf("%s", buffer);

    printf("==============\nPrint out what you have\n");
    printf("Course number: %s\n", courseid);
    printf("Info: %s\n", buffer);
}

int main() {
    func3();
}

