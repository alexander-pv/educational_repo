#include <stdio.h>

/*
   Напишите программу для копирования входного потока в выходной с
   заменой каждой строки, состоящей из одного или нескольких пробелов, одним пробелом.
 */

int main(void){

        int c;
        int wasSpace = 0;

        c = getchar();
        while ( c != EOF ) {

                /*wasSpace indicator*/
                if (c == ' ') {

                        if (wasSpace != 1) {
                                putchar(c);
                                wasSpace = 1;
                        }
                }

                else {
                        putchar(c);
                        wasSpace = 0;
                }

                /*Get next char*/
                c = getchar();
        }


        return 0;
}
