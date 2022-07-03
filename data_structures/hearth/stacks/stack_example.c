/*
You are given a stack of N integers.
In one operation, you can either pop an element from the stack or push any popped element into the stack.
You need to maximize the top element of the stack after performing exactly K operations.
If the stack becomes empty after performing K operations and there is no other way for the stack to be non-empty, print -1.

Input format :
    The first line of input consists of two space-separated integers N and K.
    The second line of input consists N space-separated integers denoting the elements of the stack.
    The first element represents the top of the stack and the last element represents the bottom of the stack.

Output format :
    Print the maximum possible top element of the stack after performing exactly K operations.

*/

#include <stdio.h>

int main() {

    int MAX_SIZE;          // Init stack limit
    scanf("%d", &MAX_SIZE);
    int top = -1;          // Init stack top
    int stack[MAX_SIZE];   // Init stack
    int ops;               // Init K operations
    scanf("%d", &ops);
    int _value;            // Temp place for value reading and pushing it to stack
    int max_value=0;       // To store max value

    // Set stack logic in functions
    int isEmpty() {

       if(top == -1)
          return 1;
       else
          return 0;
    }

    int isFull() {

       if(top == MAX_SIZE)
          return 1;
       else
          return 0;
    }

    int peek() {
       return stack[top];
    }

    int pop() {
       int value;

       if(!isEmpty()) {
          value = stack[top];
          top = top - 1;
          return value;
       } else {
          printf("Stack is empty.\n");
       }
    }

    int push(int value) {

       if(!isFull()) {
          top = top + 1;
          stack[top] = value;
       } else {
          printf("Stack is full.\n");
       }
    }

    // Reading data into temp array
    int tmp_array[MAX_SIZE];
    for (int i=0; i<MAX_SIZE; i++) {
        scanf("%d", &tmp_array[i]);
    }
    // Pushing data into right order to stack
    for (int i=MAX_SIZE; i>=0; i--) {
        push(tmp_array[i]);
    }
    //Seeking max value with K operations
    for (int i=0; i<ops; i++) {
        if (peek()>max_value){
            max_value = pop();
        }

    }
    printf("%d\n", max_value);

}
