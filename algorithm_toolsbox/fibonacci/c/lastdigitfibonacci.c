// c version of last digit fibonacci

// written by viibug

//2024/7/31

#include<stdio.h>

int LastDigitFibonacci(int n){

    if(n<=1)return n;

    
    int arr[n];
    arr[0] = 0;
    arr[1] =1;
    for(int i=2;i<=n;i++){

	arr[i] = arr[i-1]+arr[i-2]%10;

    }
    return arr[n]%10;

}




int main(void){


    int n,result;
    printf("Enter n : ");
    scanf("%d",&n);

    result = LastDigitFibonacci(n);
    printf("the last digit of f%d is %d \n",n,result);

    







}
