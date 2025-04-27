```c

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void githubGreeting() {
    const char *binaryGreeting[] = {
        "01001010","01110101","01110011","01110100","00100000",
        "00101000","01100100","01100101","00101001","01100011",
        "01101111","01100100","01101001","01101110","01100111", 
    "00101110"
    };

    for (int i = 0; i < 16; ++i) {
        long v = strtol(binaryGreeting[i], NULL, 2);
        putchar((char)v);
    }
    putchar('\n');
}

void githubGreetingTok() {
    char buffer[235];
    strcpy(buffer, 
      "00111100 01001010 01110101 01110011 01110100 00100000 "
      "00101000 01100100 01100101 00101001 01100011 "
      "01101111 01100100 01101001 01101110 01100111 "
      "00100000 01110100 01101111 01101011 01100101 " 
      "01101110 01110011 00101110 00101010 00111110 "
    );

    const char *delim = " ";
    char *token = strtok(buffer, delim);
    while (token) {
        long v = strtol(token, NULL, 2);
        putchar((char)v);
        token = strtok(NULL, delim);
    }
    putchar('\n');
}

int main() {
    printf("Executing your github greeting function -> please wait...\n");
    githubGreeting();
    githubGreetingTok();
    return 0;
}
```
