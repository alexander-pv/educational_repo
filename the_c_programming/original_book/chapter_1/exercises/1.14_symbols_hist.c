#include <stdio.h>

/*
Напишите программу для вывода гистограммы частот, с которыми
встречаются во входном потоке различные символы.
*/

#define DICTLEN 1000


struct CharsDict {
  /*Зададим структуру хранения уникальных символов наподобие словаря на массивах*/

  int nsymbols;            /*Число уникальных символов*/
  int symbols[DICTLEN];   /*Массив символов*/
  int cntr[DICTLEN];      /*Массив счетчиков символов*/
};


int linear_search(int value, struct CharsDict workingDict) {

  int idx = -1;

  for (int k = 0; k < workingDict.nsymbols; k++) {
    if (workingDict.symbols[k] == value) {
      idx = k;
    }
  }
  return idx;
}


int display_dict(struct CharsDict workingDict) {

  for (int i = 0; i < workingDict.nsymbols; i++) {
    putchar(workingDict.symbols[i]);
    printf(":\t%d ", workingDict.cntr[i]);
    display_histogram(workingDict.cntr[i]);
  }

  return 0;
}


int display_histogram(int counter) {

  for (int i=0; i<counter; i++) {
    printf("*");
  }
  putchar('\n');
  return 0;
}


int main(void) {

  int c;
  int idx;
  struct CharsDict workingDict;
  workingDict.nsymbols = 0;

  for (int i = 0; i < DICTLEN; i++){
    workingDict.cntr[i] = 0;
  };

  while ( (c = getchar()) != EOF) {

    if (c != '\n' && c != '\t') {

      /*Выполним линейный поиск по массиву уникальных символов*/
      idx = linear_search(c, workingDict);

      if (idx == -1) {
        /*При отсутствии символа в словаре, добавить.*/
        workingDict.symbols[workingDict.nsymbols] = c;
        workingDict.cntr[workingDict.nsymbols] += 1;
        workingDict.nsymbols += 1;

      }
      else {
        /*Обновить счетчик символов в словаре*/
        workingDict.cntr[idx] += 1;
      }


    }
  }

  display_dict(workingDict);

  return 0;
}
