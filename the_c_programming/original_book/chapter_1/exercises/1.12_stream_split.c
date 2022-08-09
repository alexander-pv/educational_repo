#include <stdio.h>

/*
   Напишите программу для вывода входного потока по одному слову в строке
   Добавим сюда функционал задачи 1.9, убрав лишние пробелы, табуляци, точки, запятые.
 */
int main(void) {

        int c;
        int wasSpace = 0;

        c = getchar();
        while ( c != EOF ) {

                if (c == ' ' || c == '\t') {

                        if (wasSpace != 1) {
                                putchar('\n');
                                wasSpace = 1;
                        }
                }

                else {
                        if (c != '.' && c != ',') {
                                putchar(c);
                        }
                        wasSpace = 0;
                }


                c = getchar();
        }
        return 0;
}
