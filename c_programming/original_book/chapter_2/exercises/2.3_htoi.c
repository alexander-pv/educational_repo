#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

/*
   Напишите функцию htoi(s), которая преобразует строку шестна-
   дцатеричных цифр (учитывая необязательные элементы 0х или 0Х) в ее целочисленный
   эквивалент. В число допустимых цифр входят десятичные цифры от 0 до 9, а также
   буквы a-f, A-F.
 */

#define MAXLINE 1000

int custom_getline(char line[], int maxline);
int is_hex_number(char line[]);
int hex2digit(char hexdigit);
int htoi(char line[]);


/*custom_getline считывает строку в s, возвращает ее длину*/
int custom_getline(char s[], int lim) {

      int c, i;

      for (i = 0; i < lim-1 && (c = getchar()) != EOF && c != '\n'; ++i) {
              s[i] = c;
      }

      if (c == '\n') {
              s[i] = c;
              ++i;
      }
      s[i] = '\0';
      return i;
}


/*Check that the string - char array is actually a hexadecimal number*/
int is_hex_number(char line[]) {

      int cntr = 0;
      int is_hex = 0;
      int i;

      for (i = 0; line[i] != '\0'; ++i) {
              if ( isxdigit(line[i]) ) {
                      ++cntr;
              }
      }
      /*We remove 1 non-hex symb '\0' from i variable*/
      if ( cntr == i - 2) {
              is_hex =  1;
      }

      return is_hex;
}


/*Return decimal digit from hexadecimal digit*/
int hex2digit(char hexdigit) {

      int dec;

      switch (tolower(hexdigit)) {
      case 'a': dec = 10;
              break;
      case 'b': dec = 11;
              break;
      case 'c': dec = 12;
              break;
      case 'd': dec = 13;
              break;
      case 'e': dec = 14;
              break;
      case 'f': dec = 15;
              break;
      default: dec = hexdigit - '0';
      }
      return dec;
}


/*Convert hexadecimal to decimal number*/
int htoi(char s[]) {

      int decimal = 0;
      int start_id = 2;
      int order = strlen(s) - 2 * start_id;

      for (int i = 0; s[i] != '\n'; ++i) {
              if (i >= start_id) {
                      decimal += hex2digit(s[i]) * pow(16, order);
                      --order;

              }

      }
      return decimal;
}


int main(void) {

      int str_length = 0;
      char line[MAXLINE];

      str_length = custom_getline(line, MAXLINE);

      if ( is_hex_number(line) ) {
              printf("\nThe input is a hexadecimal number: %s", line);
              printf("Converted hex to decimal: %d\n", htoi(line));
      }
      else {
              printf("\nThe input is not a hexadecimal number: %s", line);
      }

      return 0;
}
