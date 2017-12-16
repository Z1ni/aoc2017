#include <stdio.h>
#include <stdbool.h>

int main(void) {
    unsigned long long a = 873;
    unsigned long long b = 583;
    unsigned int same = 0;
    bool new_round = true;

    for (unsigned int i = 0; i < 5000000; i++) {
        new_round = true;
        if (i % 1000000 == 0) {
            // Progress indicator
            printf("%u\n", i);
        }
        while (new_round || a % 4 != 0) {
            if (new_round) {
                new_round = false;
            }
            a = (a * 16807) % 0x7FFFFFFF;
        }
        new_round = true;
        while (new_round || b % 8 != 0) {
            if (new_round) {
                new_round = false;
            }
            b = (b * 48271) % 0x7FFFFFFF;
        }
        if ((a & 0xFFFF) == (b & 0xFFFF)) {
            same++;
        }
    }
    printf("%d\n", same);

    return 0;
}