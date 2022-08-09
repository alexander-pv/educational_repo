#include <stdio.h>
#include <string.h>

#define MAXLEN 1000

int reverse(char s[]);
void itoa(int n, char s[]);


/* reverse: обращает порядок символов в строке s */
int reverse(char s[]) {

  int c, i, j;

  for (i = 0, j = strlen(s) - 1; i < j; i++, j--) {
    c = s[i];
    s[i] = s[j];
    s[j] = c;
  }

return 0;
}


/* itoa: преобразует число п в строку символов s */
void itoa(int n, char s[]) {

  int i, sign;

  if ((sign = n) < 0) { /* записываем знак */
    n = -n;              /* делаем число положительным */
  }
  i = 0;

  do {
    /* генерируем цифры в обратном порядке */
    s[i++] = n % 10 + '0';
  } while ((n /= 10) > 0);

  if (sign < 0) {
    s[i++] = '-';
  }
  s[i] = '\0';
  reverse(s);
}


int main(void) {

  int n = 1250;
  char str[MAXLEN];

  itoa(n, str);
  printf("\n%s\n", str);

  return 0;
}
