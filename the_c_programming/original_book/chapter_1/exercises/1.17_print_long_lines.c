#include <stdio.h>

#define MAXLINE 1000  /*Максимальная длина строки в потоке*/
#define PRINT_TH 80   /*Порог длины строки, после которой осуществляется вывод*/

/*
Напишите программу для вывода всех строк входного потока,
имеющих длину более 80 символов.
*/


int custom_getline(char line[], int maxline);


/*custom_getline считывает строку в s, возвращает ее длину*/
int custom_getline(char s[], int lim) {
  int c, i;

  for (i = 0; i < lim-1 && (c = getchar()) != EOF && c != '\n'; ++i)
  s[i] = c;
  if (c == '\n') {
    s[i] = c;
    ++i;
  }
  s[i] = '\0';
  return i;
}


int main(void) {

  int len;                /*Длина текущей строки*/
  char line[MAXLINE];     /*Текущая введенная строка*/

  while ((len = custom_getline(line, MAXLINE)) > 0)
    if (len > PRINT_TH){
      printf("[%d]\t%s", len, line);
    }
return 0;
}
