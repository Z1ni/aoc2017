#include <stdio.h>

int main(void) {
    unsigned long long a = 873;
    unsigned long long b = 583;
    unsigned int same = 0;

    for (unsigned int i = 0; i < 40000000; i++) {
        if (i % 1000000 == 0) {
            // Progress indicator
            printf("%u\n", i);
        }
        a = (a * 16807) % 0x7FFFFFFF;
        b = (b * 48271) % 0x7FFFFFFF;
        if ((a & 0xFFFF) == (b & 0xFFFF)) {
            same++;
        }
    }
    printf("%d\n", same);

    return 0;
}