/*
Given a 2D array A, your task is to convert all rows to columns and columns to rows.

Input:
First line contains 2 space separated integers, N - total rows, M - total columns.
Each of the next N lines will contain M space separated integers.

Output:
Print M lines each containing N space separated integers.
*/
#include <stdio.h>

int main() {
	int N, M;              // Rows, columns
	scanf("%d", &N);
	scanf("%d", &M);
	int t_array[M][N];     // Transposed array of integers

    //Reading data into array and save it in transposed way
	for (int i=0; i<N; i++) {
	    for (int j=0; j<M; j++) {
	        scanf("%d", &t_array[j][i]);
	        //printf("Array index: [%d, %d]. Value: %d\n", i, j, array[i][j]);*/
	    }
	}
	//Printing transposed array
	for (int i=0; i<M; i++) {
	    for (int j=0; j<N; j++) {
	        //Make a row as a string with whitespaces
            printf("%d ", t_array[i][j]);
	    }
	    printf("\n");
	}

	return 0;
}
