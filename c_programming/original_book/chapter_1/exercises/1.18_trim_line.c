#include <stdio.h>

#define MAXLINE 1000 /*Максимальная длина строки в потоке*/

/*
Напишите программу для удаления лишних пробелов и табуляций в
хвосте каждой поступающей строки входного потока, которая бы также удаляла
полностью пустые строки.
*/


int trimline(char s[], int lim);


/*trimline считывает строку, удаляет пробелы и табуляции в хвосте, пустые строки*/
int trimline(char s[], int lim) {
  int c, i;
  int wasSpace = -1; /*-1-start*/

  for (i = 0; i < lim-1 && (c = getchar()) != EOF && c != '\n'; ++i) {

  if (c == ' ' || c == '\t') {
    wasSpace = 1;
    --i;
  }

  if ( c != ' ' && c != '\t' && c != '\n') {
    if (wasSpace == 1) {
      s[i] = ' ';
      ++i;
      wasSpace = 0;
    }
    s[i] = c;
  }

  }

  s[i] = '\0';
  return i;
}


int main(void) {

    int len;
    char line[MAXLINE];

    while ((len = trimline(line, MAXLINE)) > 0) {
      printf("[%s]\n", line);
    }
return 0;
}
