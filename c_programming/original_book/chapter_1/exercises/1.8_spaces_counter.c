#include <stdio.h>

/*
   Напишите программу для подсчета пробелов,
   знаков табуляции и символов конца строки.
 */


int main(void) {

        int c;
        int spaces = 0;
        int tabs   = 0;
        int eols   = 0;

        while ( (c = getchar()) != EOF ) {
                if (c == ' ') {
                        ++spaces;
                }
                else if (c == '\t') {
                        ++tabs;
                }
                else if (c == '\n') {
                        ++eols;
                }

        }

        printf("Spaces: %d", spaces);
        printf("\nTabs: %d", tabs);
        printf("\nNew lines: %d\n", eols);

        return 0;
}
