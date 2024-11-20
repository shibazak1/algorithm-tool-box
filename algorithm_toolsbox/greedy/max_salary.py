
"""
Largest Concatenate Problem
Compile the largest number by concatenating the given numbers.

Input: A sequence of positive integers.

Output: The largest number that can be obtained by concatenating the given integers in some order.

-------------------------------------------------------------------------------------------------
Input format. The first line of the input contains an integer n. The second
line contains integers a1 , . . . , an .

Output format. The largest number that can be composed out of a1 , . . . , an .
Constraints. 1 ≤ n ≤ 100; 1 ≤ ai ≤ 103 for all 1 ≤ i ≤ n.
"""
#(3,23) 323 > 233
def IsBetter(a,b):

    if a + b >= b + a:
        return a
    return b


def LargestConcatenate(nums):

    largest_number = ""
    while len(nums)>0:

        max_num = nums[0]
        for num in nums:
            max_num = IsBetter(max_num,num)
        largest_number += max_num
        nums.remove(max_num)
            
    return largest_number
#---------------------------------------------------------------------------

def largest_number(numbers):
    
    for j in numbers:
        print("outer iteration num = ",j)
        for i in range(len(numbers)-1):
            print("number is = ",numbers)
            if numbers[i] + numbers[i+1] < numbers[i+1] + numbers[i]:
                temp = numbers[i]
                numbers[i] = numbers[i+1]
                numbers[i+1] = temp
                print("number is = ",numbers)
            print("iteration num ",i)
    return int("".join(numbers))
        



#---------------------------------------------------------------------------


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number(input_numbers))
