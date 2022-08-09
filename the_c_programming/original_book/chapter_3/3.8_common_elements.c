#include <stdio.h>
#include <string.h>

/*
За немногими исключениями наподобие приведенного здесь примера код,
основанный на переходах с помощью оператора goto,
труднее понимать и дорабатывать, чем код без этих операторов.
Хотя мы и не утверждаем этого категорически, все же оператор
goto следует стараться употреблять как можно реже или вообще никогда.
*/

int find_common(char s1[], char s2[]);

int find_common(char s1[], char s2[]) {

  int n, m;
  n = strlen(s1),
  m = strlen(s2);
  printf("\nInputs lengths: %d %d\n", n, m);
  int i, j;
  for (i = 0; i < n; i++) {
    for (j = 0; j< m; j++) {
      printf("Searching: %c %c\n", (char)s1[i], (char)s2[j]);
        if (s1[i] == s2[j]) {
          goto found;
        }
    }

}
found: printf("Common elements were found! Positions: %d %d\n", i, j);
return 0;
}

int main(int argc, char *argv[]) {
  printf("\nargv Inputs: %s %s", argv[1], argv[2]);
  find_common(argv[1], argv[2]);
}
