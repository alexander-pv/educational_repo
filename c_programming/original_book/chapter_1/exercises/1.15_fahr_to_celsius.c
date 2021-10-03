#include <stdio.h>

/*
Перепишите программу преобразования температур из раздела 1.2
так, чтобы само преобразование выполнялось функцией.
*/

float fahr2cel(float fahr_val);
int read_digit(void);

float fahr2cel(float fahr_val) {
  /*Формула перевода температуры*/
  return (5.0/9.0) * (fahr_val-32.0);
}

int read_digit(void) {
  /*Чтение значения температуры по Фаренгейту в стандартном потоке ввода*/
  int c;
  int d = 0;

  while ( (c = getchar()) != EOF) {
    if (c >= '0' && c <= '9')
      d = 10 * d + (c - '0');
  }
  return d;
}


int main(void) {

  float fahr_input;

  fahr_input = (float) read_digit();
  printf("\nFahrenheit: %.2fF->Celsius: %.2fC\n\n", fahr_input, fahr2cel(fahr_input));
  return 0;
}
