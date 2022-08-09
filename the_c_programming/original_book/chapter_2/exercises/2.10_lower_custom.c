#include <stdio.h>

/*
Перепишите функцию lower, которая преобразует буквы в верхнем
регистре к нижнему, с использованием условного выражения a ? b: c
вместо конструкции if-else.
*/

#define MAXSTRARRAY 1000

int lower(int c);


int lower(int c) {
  c = (c >= 'A' && c <= 'Z') ? c + 'a' - 'A': c;
  return c;
}


int main(void) {

  char str_buffer[MAXSTRARRAY];
  scanf("%s", str_buffer);
  printf("\nInput: %s", str_buffer);

  for (int i = 0; (str_buffer[i] = lower(str_buffer[i])) != '\0'; i++) {
    ;
  }

  printf("\nOutput: %s\n", str_buffer);


}
