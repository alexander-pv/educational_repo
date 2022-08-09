#include <stdio.h>

/*Подсчет символов во входном потоке*/
int main()
{
        long nc;

        nc = 0;
        while(getchar() != EOF) {
                ++nc;
                printf("%ld\n", nc);
        }


}
