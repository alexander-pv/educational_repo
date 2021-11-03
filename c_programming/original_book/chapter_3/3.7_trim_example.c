#include <stdio.h>
#include <string.h>

#define MAXLEN 1000

int trim(char s[]);

/* trim: удаляет символы пустого пространства из конца строки */
int trim(char s[]) {

   int n;

   for (n = strlen(s)-1; n>=0; n--) {
     if (s[n] != ' ' && s[n] != '\t' && s[n] != '\n') {
       break;
     }
   }
   s[n+1] = '\0';

   return n;
}


int main(void) {

  char str[MAXLEN];

  scanf("%s", str);
  printf("\nInput: %sEND", str);
  trim(str);
  printf("\nOutput: %sEND", str);


}
