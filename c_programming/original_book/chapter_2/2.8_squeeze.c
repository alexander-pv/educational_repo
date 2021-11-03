#include <stdio.h>

/*
Префиксные и постфиксные операции инкрементирования/декрементирования:

++i: переменная инкрементируется до того, как используется.
i++ переменная инкрементируется после того, как используется.

Пример использования постфиксной операции инкрементирования:
*/

#define MAXSTRARRAY 1000

int squeeze(char *s, int c);
int read_stream(char *s);

/*squeeze: удаляет все символы c из строки s*/
int squeeze(char *s, int c) {

  int i, j;

  for (i = j = 0; s[i] != '\0'; i++) {
      if (s[i] != c) {
        s[j++] = s[i];
      }
    }
  s[j] = '\0';

  return 0;
}

/*Чтение текста в потоке ввода*/
int read_stream(char *s) {

  int c, i;
  for (i = 0; i < MAXSTRARRAY-1 && (c = getchar()) != EOF; ++i) {
          s[i] = c;
  }
  s[i] = '\0';

  return i;
}


int main(void) {

  int array_len;
  char array[MAXSTRARRAY];
  char del_c =  '!';  /*Будем чистить текст на восклицательные знаки*/

  array_len = read_stream(array);
  squeeze(array, del_c);
  printf("Cleared text:\n%s", array);

}
