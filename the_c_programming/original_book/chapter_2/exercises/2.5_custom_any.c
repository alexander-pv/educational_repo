#include <stdio.h>

/*
Напишите функцию any (s1, s2), возвращающую номер первой
позиции в строке s1, в которой находится какой-либо из символов строки s2, либо -1,
если строка si не содержит ни одного символа из s2.
*/

#define MAXSTRARRAY 1000
#define SYMBOLSLEN 10

int any(char *s1, char *s2);


int any(char *s1, char *s2) {

  int i, j;
  int index = -1;

  for (i = 0; s1[i] != '\0'; i++) {

      for (j = 0; s2[j] != '\0'; j++) {

          if (s1[i] == s2[j]) {
            index = i;
            break;
          }
      }

      if (index != -1) {
        break;
      }

  }

  return index;
}



int main(void) {

  char string_buffer[MAXSTRARRAY];
  char symbols[SYMBOLSLEN];
  int ans;

  scanf("%s", string_buffer);
  scanf("%s", symbols);
  printf("\nstring_buffer: %s", string_buffer);
  printf("\nsymbols: %s", symbols);
  ans = any(&string_buffer, &symbols);
  printf("\nans = %d\n", ans);

}
