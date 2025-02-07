int rd = 0;
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