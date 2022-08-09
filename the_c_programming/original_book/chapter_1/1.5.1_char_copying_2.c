#include <stdio.h>

/*Копирование входного потока в выходной 2v*/
int main()
{
        int c;

        c = getchar();
        while ( (c = getchar()) != EOF ) {
                putchar(c);
                printf("EOF constant is: %d\n", EOF);
        }

}
