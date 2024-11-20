# givin m ,n find  ->  (Fm+F(m+1)+F(m+2)+....+F(n))mod 10

# we know that S(m) = S(n)-S(n-m)

#S(n) = F(0)+F(1)+F(3)+....+F(n-1)+F(n)

#s(n-m)=F(0)+F(1)+..+F(m-1)

#S(m) = ...................F(m)+F(m+1)+....+F(n)

#written by viibug
#at 2024/8/14

#----------------------------------------------------------------------------------------------#
#                                 Last Digit Of Parail Sum of Fibonacci                        #
#----------------------------------------------------------------------------------------------#


def LastDigitFibonnacci(n):

    current,nxt = 0,1

    for _ in range(n):

        current,nxt = nxt,(nxt+current)%10

    return current



def last_digit_sum(n):

    return (LastDigitFibonnacci((n+2)%60)+9)%10



m,n = map(int,input("Enter  m , n : ").split())

print(last_digit_sum(n))
print(last_digit_sum(m-1))
print((last_digit_sum(n) - last_digit_sum(m-1))%10)
