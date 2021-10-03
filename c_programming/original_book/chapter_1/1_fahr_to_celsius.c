#include <stdio.h>


/* Bывод таблицы температур по Фаренгейту и Цельсию для fahr = 0, 20, . .., 300 */
int main()
{
        float fahr, celsius;
        int lower, upper, step;

        lower = 0; /* нижняя граница температур в таблице */
        upper = 300; /* верхняя граница */
        step = 10; /* величина шага */

        fahr = lower;
        printf("Fahr\tCelsius\n");
        while (fahr <= upper) {
                celsius = (5.0/9.0) * (fahr-32.0); /*Celsius=(5/9) * (Fahr-32) */
                printf("%3.0f\t%6.1f\n", fahr, celsius);
                fahr = fahr + step;
        }


}
