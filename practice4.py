from operator import truediv
from unittest import result


def max_num(*numbers):
    max = 0
    i = 0
    for i in range(len(numbers)):
        if numbers[i] > max:
            max = numbers[i]
    
    return max

def mult_list(*numbers):
    result = numbers[0]
    i = 1
    for i in range(len(numbers)):
        result = result * numbers[i]
    
    return result

def rev_string(word):
 
    return word[::-1]

def num_within(number,begin,end):
    if number > begin and number < end:
        return True
    else:
        return False

def pascal(n):
    for i in range(1,n+1):
        for j in range(0, n-i+1):
            print(' ', end='')

        C = 1
        for j in range(1,i+1):
            print(' ', C, sep='', end='')

            C = C * (i-j) // j
        print()


print(max_num(1,2,3,4,5,6,7,8,9,5,6,2,5,85,2,47,8))

print(mult_list(1,2,3,2,2,2,0))

print(rev_string("hello"))

print(num_within(10,2,5))

pascal(5)