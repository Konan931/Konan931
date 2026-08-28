#include <stdio.h>
#include <stdlib.h>

#include "../include/my_binary_greetings.h"

static const char *const binary_greeting[] = MY_BINARY_GREETINGS;
static const char *const binary_greeting_tokens[] = MY_BINARY_GREETINGS_TOK;

static void print_binary_words(
    const char *const words[],
    const size_t word_count
) {
    for (size_t i = 0; i < word_count; ++i) {
        const long value = strtol(words[i], NULL, 2);
        putchar((char)value);
    }
    putchar('\n');
}

void githubGreeting(void) {
    print_binary_words(
        binary_greeting,
        sizeof binary_greeting / sizeof binary_greeting[0]
    );
}

void githubGreetingTok(void) {
    print_binary_words(
        binary_greeting_tokens,
        sizeof binary_greeting_tokens / sizeof binary_greeting_tokens[0]
    );
}

int main(void) {
    puts("Executing this little github greeting -> please wait (and stay calm)...");
    githubGreeting();
    githubGreetingTok();
    return 0;
}
