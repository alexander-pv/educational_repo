#include <stdio.h>

#define MAXLINE 1000 /*Максимальная длина строки в потоке*/


int custom_getline(char line[], int maxline);
void copy(char to[], char from[]);


/*Вывод самой длинной строки в потоке*/
int main(void) {

  int len;                /*Длина текущей строки*/
  int max;                /*Текущая максимальная длина*/
  char line[MAXLINE];     /*Текущая введенная строка*/
  char longest[MAXLINE];  /*Самая длинная строка из введенных*/

  max = 0;
  while ((len = custom_getline(line, MAXLINE)) > 0)
    if (len > max){
      max = len;
      copy(longest, line);
    }
  if (max > 0) {
    printf("%s", longest);
    printf("Max length: %d\n", max);
  }

  return 0;
}

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

/*copy копирует строку from в to, длина  to считается достаточной*/
void copy(char to[], char from[]) {
  int i = 0;
  while ( (to[i] = from[i]) != '\0')
    ++i;
}
