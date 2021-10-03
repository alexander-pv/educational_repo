#include <stdio.h>


/* Bывод таблицы температур по Фаренгейту и Цельсию */
int main()
{
        float fahr, celsius;
        int lower, upper, step;

        lower = 0; /* нижняя граница температур в таблице */
        upper = 200; /* верхняя граница */
        step = 10; /* величина шага */

        celsius = lower;
        printf("Fahr\tCelsius\n");
        while (celsius <= upper) {
                fahr = 32.0 + (9.0/5.0) * celsius;
                printf("%3.1f\t%6.1f\n", fahr, celsius);
                celsius = celsius + step;
        }


}
