# de-hours-with-experts
Data Engineering Hours With Experts Coding Challenge!

## Problem

For a given number, return the next largest number that can be created by rearranging that number's digits.

If no larger number can be created, return -1

Example inputs/outputs are shown below:

|Input|Output|
|----|----|
|12|21|
|21|-1|
|12345678|12345687|
|34535762|34536257|
|45590051|45590105|
|987654321|-1|

You can create your solution in Java, Scala, or Python. Some files and tests have been created for you as a starting point. Instructions for importing the Java and Scala projects into Intellij are included.

## Solution in Python
```
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
```

## Things not to worry about
 * Validating command line arguments - you can just assume each program takes 1 argument which is always a valid number


