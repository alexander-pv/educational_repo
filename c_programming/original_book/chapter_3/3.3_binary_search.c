#include <stdio.h>

#define ARRAYLIM 1000

int binsearch(int x, int *v, int n);
int to_digits(int *s);


/* binsearch: поиск х в v[0] <= v[l] <= ... <= v[n-l] */
int binsearch(int x, int *v, int n) {

  int low, high, mid;

  low = 0;
  high = n - 1;
  while (low <= high) {
    mid = low + (high-low)/2;
    if (x < v[mid]) {
      high = mid - 1;
    }
    else if (x > v[mid]) {
      low = mid + 1;
    }
    else {
      return mid; /*найдено соответствие*/
    }
  }
  return -1; /*нет соответствия*/
}


int main(void) {

  int digits[ARRAYLIM];
  int n, value, ans;

  printf("Inputs:\n");
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d", &digits[i]);
    printf("%d ", digits[i]);
  }
  scanf("%d", &value);

  printf("\nn: %d\n", n);
  printf("value: %d\n", value);

  ans = binsearch(value, digits, n);

  printf("ans: %d\n", ans);


}
