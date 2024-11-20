
/* compute the the nth fibonacci number

fibonacci define recursively as f(n) = f(n-1)+f(n-2) where f(0) = 0 ,f(1)=1

written by Viibug
at 2024/7/29
      
*/
#include<stdio.h>

#define MAX 1000

int FibonacciRecursive(int n){

    if(n<=1){

	return n;
    }

    else{

	printf("Computing the F%d recursively\n",n);
	return FibonacciRecursive(n-1)+FibonacciRecursive(n-2);

    }

}
//------------------------------------------

long long FibonacciIterative(int n){

    if(n<=1)return n;
    
    long long fibonacci_num[n];
    //set the 1st and 2nd fibonacci number
    fibonacci_num[0] = 0;
    fibonacci_num[1] =1;


    // loop start at 2 to run n-1 time
    for(int i=2;i<=n;i++){

	//etch ith fibonacci numebr is the sum of the previose 2 numbers
	fibonacci_num[i] = (long long) fibonacci_num[i-1]+fibonacci_num[i-2];
    }

    
    return fibonacci_num[n];
    
}

//------------------------------------------------------------------------------------------------

// we do not need to store all the element of the array we need only the privouse 2 one

long long FibonacciIterative2(int n){

    if(n<=1)return n;
    
    //long long pre_1,pre_2,curr;
    long long previous,oldprevious,current;

    // pre_1 = 0;
    //pre_2 = 1;
    previous = 0;
    current = 1;
    

    for(int i=2;i<=n;i++){

	oldprevious = previous;
	previous = current;
	current = oldprevious + current;
	//curr = pre_1+pre_2; // 0+1 =1
	//pre_1 = pre_2;     // pre_1 = 1
	//pre_2 = curr;      // pre_2 = 1
    }

    return current;

}

//--------------------------------------------------------------------------------------------------------

// we can make the recusive solution mutch batter by store the value when we computed and retrevite when we need it

long long table[MAX];
long long FibonacciRecursiveMemorization(int n){

   

    if(table[n]==-1){

	if(n<=1){

	    table[n] = n;
	}
	else{
	    table[n] = FibonacciRecursiveMemorization(n-1)+FibonacciRecursiveMemorization(n-2);
	}

       
    }
    return table[n];


     





}



int main(void){


    int n;
    long long result;
    printf("Enter N :");
    scanf("%d",&n);
    //result  = FibonacciRecursive(n);
    //result = FibonacciIterative2(n);

    for(int i=0;i<MAX;i++){

	table[i] = -1;

    }
    result = FibonacciRecursiveMemorization(n);
    printf("%lld\n",result);

    return 0;

}
      
