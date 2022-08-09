#include <stdio.h>
#define MAXLINE 100

int my_getline(char line[], int max);
int strindex(char source[], char searchfor[]);
int simple_grep(char pattern[]);


/* my_getline: считывает строку в s, возвращает ее длину */
int my_getline(char s[], int lim)
{
  int c, i;

  i = 0;
  while (--lim > 0 && (c=getchar()) != EOF && c != '\n' ) {
    s[i++] = c;
  }
  if (c == '\n') {
    s[i++] = c;
  }
  s[i] = '\0';
  return i;
}


/* strindex: возвращает индекс строки t в s, -1 при отсутствии */
int strindex(char s[], char t[])
{
  int i, j, k;
  for (i = 0; s[i] != '\0'; i++) {
    for (j=i, k=0; t[k] != '\0' && s[j] == t[k]; j++, k++) {
      ;
    }
    if (k > 0 && t[k] == '\0'){
      return i;
    }
  }
  return -1;
}


int simple_grep(char pattern[])
{
  char line[MAXLINE];
  int found = 0;
  int row = 0;

  while (my_getline(line, MAXLINE) > 0) {
    if (strindex(line, pattern) >= 0) {
      printf("Row: %d: %s", ++row, line);
      found++;
    }
  }
return found;
}


int main(int argc, char *argv[])
{
  if (argc > 1) {
    int output = simple_grep(argv[1]);
    printf("\nOutput: %d\n", output);
  }
  return 0;
}
