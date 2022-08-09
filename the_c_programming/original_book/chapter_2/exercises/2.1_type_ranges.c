#include <stdio.h>
#include <limits.h>
#include <float.h>
#include <math.h>

/*Напишите программу для определения диапазонов переменных типов
char, short, int и long (как signed, так и unsigned)
1) путем вывода соответствующих значений из заголовочных файлов,
2) с помощью непосредственного вычисления
*/

int get_type_ranges(void);
int calculate_type_ranges(void);

int get_type_ranges(void) {
  printf("\nget_type_ranges:");
  /*char*/
  printf("\nsigned char:\t[%d, %d]\nunsigned char:\t[0, %d]\n", SCHAR_MIN, SCHAR_MAX, UCHAR_MAX );
  /*int*/
  printf("\nsigned int:\t[%d, %d]\nunsigned int:\t[0, %ld]\n", INT_MIN, INT_MAX, UINT_MAX);
  /*short*/
  printf("\nsigned short:\t[%d, %d]\nunsigned short:\t[0, %d]\n", SHRT_MIN, SHRT_MAX, USHRT_MAX);
  /*long*/
  printf("\nsigned long:\t[%ld, %ld]\nunsigned long:\t[0, %llu]\n", LONG_MIN, LONG_MAX, ULONG_MAX);
  /*float*/
  printf("\nfloat:\t[%e, %e]", FLT_MIN, FLT_MAX);
  return 0;
}


int calculate_type_ranges(void) {
  printf("\n\ncalculate_type_ranges:");
  /*We add -1 because 1 bit is used for zero value*/
  /*char*/
  printf("\nsigned char:\t[-%d, %d]\nunsigned char:\t[0, %d]\n",
            (int) pow(2, 8)/2, (int) pow(2, 8)/2 - 1, (int) pow(2, 8) - 1 );
  /*int*/
  printf("\nsigned int:\t[-%ld, %ld]\nunsigned int:\t[0, %ld]\n",
          (long)  pow(2, 32)/2, (long) pow(2, 32)/2 - 1, (long) pow(2, 32) - 1);
  /*short*/
  printf("\nsigned short:\t[%ld, %ld]\nunsigned short:\t[0, %f]\n",
         (long) pow(2, 16)/2, (long) pow(2, 16)/2 - 1, (long) pow(2, 16) - 1);
  /*long*/
  printf("\nsigned long:\t[-%.0f, %.0f]\nunsigned long:\t[0, %.0f]\n",
          pow(2, 64)/2.0, pow(2, 64)/2.0 - 1.0,  pow(2, 64) - 1.0);


}


int main(void) {
  get_type_ranges();
  calculate_type_ranges();
  return 0;
}
