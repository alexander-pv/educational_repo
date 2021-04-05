/* 
Given the size and the elements of array A, print all the elements in reverse order.

Input:
First line of input contains, N - size of the array.
Following N lines, each contains one integer, i{th} element of the array i.e. A[i].
*/

#include <stdio.h>

int main(){
	int N;
    
	// Reading array size and declaring static array
    scanf("%d", &N);
    int arr[N];
    // Reading and writing int to a declared static array
	for(int idx=0; idx<N; idx++)
		{
			scanf("%d", &arr[idx]);
		}
    // Printing static array in a reverse order
	for(int idx=N-1; idx>=0; idx--)
		{
			printf("%d\n", arr[idx]);
		}

	return 0;
}
