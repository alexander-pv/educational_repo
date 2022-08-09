#include <stdio.h>

/*Подсчет символов во входном потоке 2v*/
int main()
{
        double nc;

        for (nc = 0; getchar() != EOF; ++nc)
                printf("%.0f\n", nc);

}
