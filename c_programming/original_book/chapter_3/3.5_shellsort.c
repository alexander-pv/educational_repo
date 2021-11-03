#include <stdio.h>

/*
Сортировка массива по алгоритму Шелла

Основная идея алгоритма, разработанного Д.Л. Шеллом (D.L. Shell) в 1959 году,
заключается в том, что на первом этапе сортировки сравниваются далеко
отстоящие друг от друга элементы, а не соседние, как в более простых методах.
Это позволяет быстро ранжировать большие массы
неупорядоченных элементов, чтобы на следующих этапах оставалось меньше работы.
Интервал между сравниваемыми элементами постепенно уменьшается до единицы,
и в этот  момент сортировка сводится к обмену соседних элементов
— методу пузырьков.
*/

#define ARRAYLIM 1000

void shellsort(int *v, int n);
int scan_array(int *v, int n);
int print_array(int *v, int n);


/* shellsort: сортирует v[0]...v[n-1] в порядке возрастания */
void shellsort(int *v, int n) {
  int gap, i, j, temp;

  for (gap = n/2; gap > 0; gap /= 2) {
    for (i = gap; i < n; i++) {
      for (j = i - gap; j >= 0 && v[j] > v[j + gap]; j-=gap) {
        temp = v[j];
        v[j] = v[j+gap];
        v[j+gap]=temp;
      }
    }
  }
}


/*Вывод массива чисел*/
int print_array(int *v, int n) {

  printf("\n");
  for (int i = 0; i < n; i++) {
    printf("%d ", v[i]);
  }
  printf("\n");
  return 0;
}


/*Чтение массива чисел из потока ввода*/
int scan_array(int *v, int n) {
  for (int i = 0; i < n; i++) {
    scanf("%d", &v[i]);
  }
  return 0;
}


int main(void) {

  int digits[ARRAYLIM];
  int n;

  printf("\nshellsort algorithm example:");
  scanf("%d", &n);
  scan_array(&digits[0], n);

  printf("\nInputs:");
  printf("\nn: %d", n);
  print_array(&digits[0], n);

  printf("Output:");
  shellsort(&digits[0], n);
  print_array(&digits[0], n);

  return 0;
}
