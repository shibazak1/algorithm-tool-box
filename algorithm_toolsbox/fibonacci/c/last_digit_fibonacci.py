# finding the last digit of fibonacci number
#we will use the modulo operator n%10
#every decimal number can be represented as multiple of 10^x 123 = 1*10^2 + 2*10 +3*10^0
#so when we divided by 10 the result is how many group of 10 + the reminder which is last digit
# d = q*10 + r (r=last digit)

#written by viibug
#2024/7/31


def LastDigitFibonacci(n):

    if n<=1:
        return n
    fibonacci_list = [0]*(n+1)
    fibonacci_list[0]=0
    fibonacci_list[1]=1

    for i in range(2,n+1):
        fibonacci_list[i]= fibonacci_list[i-1]+fibonacci_list[i-2]

    return fibonacci_list[n]%10



#----------------------------------------------------------------------------------------------------
# when the number get bigger is hard to store it in int type even with the build in integer type in python
# the loop will get slower

#so rather then computing the nth fibonacci then take the modulo we take the modulo of every intermidait operation
# (a + b) mod 10 = a mod 10 + b mod 10 ==> a=2 ,b=3g

def LastDigitFibonacci2(n):

    if n<=1:
        return n
    fibonacci_list = [0]*(n+1)
    fibonacci_list[0] = 0
    fibonacci_list[1] = 1

    for i in range(2,n+1):
        fibonacci_list[i] = fibonacci_list[i-1]+fibonacci_list[i-2] % 10

    return fibonacci_list[n]%10




n = int(input("enter : n "))
print(f"Last digit F{n} = {LastDigitFibonacci2(n)}")
