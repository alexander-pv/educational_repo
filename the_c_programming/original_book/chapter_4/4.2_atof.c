#include <ctype.h>
#include <stdio.h>

#define MAXLINE 100


int my_getline(char line[], int max);
double atof(char s[]);


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

/* atof: преобразование строки s в число типа double */
double atof(char s[])
{
  double val, power;
  int i, sign;

  for (i = 0; isspace(s[i]); i++) {
    ;
  }
  sign = (s[i] == '-') ? -1 : 1;
  if (s[i] == '+' || s[i] == '-'){
    i++;
  }
  for (val = 0.0; isdigit(s[i]); i++) {
    val = 10.0 * val + (s[i] - '0');
  }
  if (s[i] == '.'){
    i++;
  }
  for  (power = 1.0; isdigit(s[i]); i++) {
    val = 10.0 * val + (s[i] - '0');
    power *= 10;
  }
  return sign * val / power;
}


int main(void)
{
  double sum = 0;
  char line[MAXLINE];
  while(my_getline(line, MAXLINE) > 0){
    sum += atof(line);
  }
  printf("\nResult: %g\n", sum);
return 0;
}
