/* exploit.c  */

/* A program that creates a file containing code for launching shell */
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int rd = 0;

const char shellcode[] =
  "\x31\xc0"             /* xorl    %eax,%eax              */
  "\x50"                 /* pushl   %eax                   */
  "\x68""//sh"           /* pushl   $0x68732f2f            */
  "\x68""/bin"           /* pushl   $0x6e69622f            */
  "\x89\xe3"             /* movl    %esp,%ebx              */
  "\x50"                 /* pushl   %eax                   */
  "\x53"                 /* pushl   %ebx                   */
  "\x89\xe1"             /* movl    %esp,%ecx              */
  "\x99"                 /* cdql                           */
  "\xb0\x0b"             /* movb    $0x0b,%al              */
  "\xcd\x80"             /* int     $0x80                  */
;

/**
 * Function that calls an assembly instuction
 * to return the address of the top of the stack (i.e., ESP).
 * Note that ESP changes with function calls and returns.
 * Use this function to help compute the location of the
 * return address of the target vulnerable function frame.
 **/
unsigned long get_sp(void){
    __asm__("movl %esp,%eax");
}

/**
 * vulnerable function bof
 **/
void bof(char *str){
    /* Initialize the random seed */
    srand(233);
    /* 32-byte buffer is statically allocated by the compiler */
    char buffer[32];
    printf("Come into function bof\n");
    int guard;
    int guard1 = 0x41304130;
    int guard2 = rand();
    if (rand()&1){
        guard = guard1;
    }
    else{
        guard = guard2;
    }
    rd = guard;

    /* The following unsafe function call may cause a buffer overflow */
    strcpy(buffer, str);

    /* You need to bypass this check */
    if(guard != rd){
        printf("Good bye!\n");
        exit(0);
    }
}

/* You need to craft buffer data passed to function bof
 * To execute the shellcode
 *
 * The target is:
 * the execution flow will be guided into shellcode and
 * exits there without coming back to main function
 *
 * The shellcode has been implemented already, you only
 * need to
 * 1. prepare appropriate contents in the buffer
 * 2. overwrite the return address of bof function
 * on the stack to the address of shellcode.
 * */

int main(int argc, char **argv){
    char buffer[100];
    printf("Come into function main\n");

    /* You need to fill the buffer with appropriate contents here,
     * e.g., overwriting the return address and copy the shell code.
     * Note that the entire payload must be copied via the strcpy()
     * function in bof() (Line 48). If part of the payload like the
     * shellcode is not copied in bof(), e.g., you insert some
     * terminator characters to prevent the buffer in main function
     * from being overwritten so you can use some static location
     * in the main function fraame to store the shellcode, you will
     * not get full credit.
     * Using a function pointer to directly call shellcode is not
     * allowed. You can use the memset() and memcpy() functions.
     * Tip: Use GDB to examine the stack frame and register values.
     * */

    /* You should add the exploitation code below.
     * */


    /* bof() is called below.
     * Please DON'T CHANGE code after this line
     * */
    bof(buffer);

    printf("Exit from function bof\n");
    printf("You will succeed next time!\n");
}
