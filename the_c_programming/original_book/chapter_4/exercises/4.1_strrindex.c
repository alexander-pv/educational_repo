#include <stdio.h>
#include <string.h>
#define MAXLEN 1000


/*
Напишите функцию strrindex (s, t), которая возвращает индекс
самого правого вхождения строки t в s, либо -1, если такой строки в s нет.
*/


int strrindex(char s[], char t[]);

int strrindex(char s[], char t[])
{
  int s_pos, t_pos;
  int len_s, len_t;
  int i, j;

  t_pos = 0;
  len_s = strlen(s);
  len_t = strlen(t);

  for (i = 0; i < len_s && t_pos < len_t; i++) {
    for (j = t_pos; j < len_t; j++) {
      if (s[i] == t[j]){
        s_pos = i;
        t_pos++;
      }
      else {
        t_pos = 0;
      }
      break;
    }
  }
  return ((len_t == t_pos) ? s_pos: -1);
}

int main(int argc, char *argv[])
{
  int output;
  if (argc >= 3){
    output = strrindex(argv[1], argv[2]);
    printf("\nOutput: %d\n", output);
  }
  return 0;
}
