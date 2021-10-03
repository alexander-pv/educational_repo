#include <stdio.h>

/*Копирование входного потока в выходной*/
int main()
{
        int c;

        c = getchar();
        while (c != EOF) {
                putchar(c);
                c = getchar();
        }

}
