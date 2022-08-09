#include <stdio.h>

/*
Напишите альтернативную версию функции squeeze (si, s2),
которая бы удаляла из строки si все символы, встречающиеся в строке s2.
*/

#define MAXSTRARRAY 1000

int squeeze_str(char *s1, char *s2);
int read_stream(char *s);

/*squeeze_str: удаляет все символы строки s2 из строки s1*/
int squeeze_str(char *s1, char *s2) {

  /*Проходимся по массиву знаков текста один раз. Для каждого знака
    проходимся по массиву запрещающих символов. Если найден запрещающий символ -
    выходим из цикла проверки, поставив флаг isFound = 1.
    Если !isFound, т.е. ничего не найдено, пеерписываем символ.
  */
  int i, j, k;
  int isFound;

    for (i = j = 0; s1[i] != '\0'; i++) {

      isFound = 0;
      for (k = 0; s2[k] != '\0'; k++) {

        if (s1[i] == s2[k]) {

         isFound = 1;
         break;

        }
      }

      if (!isFound) {
        s1[j++] = s1[i];
      }
    }

  s1[j] = '\0';

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
  char del_array[] =  {'!', '&', '*', '\0'};

  array_len = read_stream(array);
  printf("\nInput text:\n%s", array);
  squeeze_str(array, del_array);
  printf("\nCleared text:\n%s", array);

}
