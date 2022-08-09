#include <stdio.h>

#define IN 1   /*Внутри слова*/
#define OUT 0  /*Снаружи слова*/


/*Подсчет строк, слов, символов во входном потоке*/
int main(void) {

        int c, nl, nw, nc, state;

        state = OUT;
        nl = nw = nc = 0;
        while ( (c = getchar()) != EOF) {
                ++nc;
                if (c == '\n') {
                        ++nl;
                }
                if (c == ' ' || c == '\n' || c == '\t')
                        state = OUT;
                else if (state == OUT) {
                        state = IN;
                        ++nw;
                }
        }
        printf("Lines:\t%d\nWords:\t%d\nChars:\t%d\n", nl, nw, nc);
        return 0;
}
