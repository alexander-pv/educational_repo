#include <stdio.h>

/*
   Напишите программу для копирования входного потока в выходной с
   заменой знаков табуляции на \t, символов возврата назад (Backspace) на \Ь, а
   обратных косых черт — на \\. \
   Это сделает табуляции и символы возврата легко читаемыми в потоке.
 */

int main(void) {

        int c;

        c = getchar();
        while ( c != EOF ) {

                if (c == '\t') {
                        printf("%s", "\\t");
                }
                else if (c == '\b') {
                        printf("%s", "\\b");
                }
                else if (c == '/') {
                        printf("%s", "\\");
                }
                else {
                        putchar(c);
                }


                c = getchar();
        }




        return 0;
}
