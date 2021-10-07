#include <stdio.h>

#define MAXLINE 1000 /*Максимальная длина строки в потоке*/


/*
Напишите функцию reverse (s), которая переписывает свой
строковый аргумент s в обратном порядке. Воспользуйтесь ею для написания программы,
которая бы выполняла такое обращение над каждой строкой входного потока по очереди.
*/


int custom_getline(char line[], int maxline);
int reverse(char s[], char s_reversed[], int s_len);


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


/*reverse возвращает массив символов в обратном порядке*/
int reverse(char s[], char s_reversed[], int s_len) {

  s_reversed[s_len] = '\0';
  --s_len;
  for (int i = 0; s[i] != '\n'; ++i) {
    s_reversed[s_len] = s[i];
    --s_len;
  }

return 0;
}


int main(void) {

  int len;
  char line[MAXLINE];
  char reversed[MAXLINE];

  while ((len = custom_getline(line, MAXLINE)) > 0){
    --len; /*We remove '\0' and '\n' from length counter*/
    reverse(line, reversed, len);
    printf("\nLine: %sReversed: %s\n", line, reversed);
  }


}
