#include <stdio.h>

int main(void) {

  int c;

  c = getchar();
  while ( c != EOF ){

    if (c == '\t') {
      printf("%s", "\\t");
    }
    else if (c == '\b'){
      printf("%s", "\\b");
    }
    else if (c == '/'){
      printf("%s", "\\");
    }
    else {
      putchar(c);
    }


    c = getchar();
  }




return 0;
}
