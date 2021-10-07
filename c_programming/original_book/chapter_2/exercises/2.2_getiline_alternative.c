#include <stdio.h>


/*Напишите цикл, эквивалентный приведенному выше циклу for, не
используя операции && и | |.
Цикл:
for (i=0; i< lim-1 && (c=getchar()) != ' \n' && с != EOF; ++i)
s[i] = c;
*/

#define MAXLINE 1000

int getline_alt(char line[], int linelimit);


int getline_alt(char s[], int lim) {

  int c;

  for (int i = 0; i < lim - 1; ++i){
    switch (c = getchar()) {
      case '\n':
                s[i] = '\0';
                i = lim;
                break;
      case EOF :
                s[i] = '\0';
                i = lim;
                break;
      default:
                s[i] = c;
                break;
    }
  }
return 0;
}


int main(void) {

  char line[MAXLINE];
  getline_alt(line, MAXLINE);
  printf("%s\n", line);

return 0;
}
