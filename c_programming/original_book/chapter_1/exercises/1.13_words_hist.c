#include <stdio.h>
/*
Напишите программу для вывода гистограммы длин слов во входном потоке
*/

#define HISTSPACELEN 10


int display_histogram(int counter) {
  /*
  Вывод горизонтальной гистограммы заданного символа
  */
  for (int i=0; i < (HISTSPACELEN - counter); i++) {
    printf(" ");
  }
  for (int i=0; i<counter; i++) {
    printf("*");
  }
  return 0;
}


int split_stream_with_hist(void) {
  /*
  Вывод входного потока по одному слову в строке.
  Для каждого слова добавляется гистограмма его длины.
  */
  int c;
  int wasSpace = 0;
  int histCounter = 0;
  c = getchar();

  while ( c != EOF ) {


          if (c == ' ' || c == '\t' || c == '\n') {
                  if (wasSpace != 1) {
                      display_histogram(histCounter);
                      histCounter = 0;
                      putchar('\n');
                      wasSpace = 1;
                  }
          }
          else {
                  if (c != '.' && c != ',') {
                      putchar(c);
                      histCounter += 1;
                  }
                  wasSpace = 0;
          }
          c = getchar();

  }
  return 0;
}


int main(void) {
  split_stream_with_hist();
  return 0;
}
