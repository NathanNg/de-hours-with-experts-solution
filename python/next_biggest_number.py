#!/usr/bin/python3
import sys

def main():
    next_biggest_number(sys.argv[1])


def next_biggest_number(num):
    
    #Change the input into an array of numbers
    digits = [int(n) for n in str(num)]

    #If the sorted digits from largest to smallest equal
    #to the original digits or the digits are the same
    #then return not possible
    if sorted(digits, reverse=True) == digits:
        return -1
    
    #Loop in reverse to check if the rightmost number is greater than rightmost - 1
    #find the index and break
    for i in reversed(range(len(digits))):
        if digits[i] > digits[i-1]:
            break

    #Get first set of digits go from start to i
    first = digits[:i]
    #Get second set of digits go from i to end
    second = digits[i:]

    #Loop in reverse to check if the last digit of first set of number is smaller than second set of number
    #with 1 number a time
    #then swap the number
    for k in reversed(range(len(second))):
        if second[k] > first[-1]:
            tmp = second[k]
            second[k] = first[-1]
            first[-1] = tmp
            break
    
    #Join first and second sets of digits
    result = map(str, (first + sorted(second)) ) 

    #return the number as integer
    return int("".join(result))

if __name__ == "__main__":
    main()

