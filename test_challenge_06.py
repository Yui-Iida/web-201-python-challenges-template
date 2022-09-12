# Write a function in python that 
# takes an array of numbers and returns a
# sum of the square of all the numbers in the array.

def sum_of_squares(array_of_numbers):
    sum_of_squares = 0
    for num in array_of_numbers:
        sum_of_squares += num ** 2
    return sum_of_squares

def test_challenge_06_happy_case(): 
     assert sum_of_squares([1,2,3,4]) == 30


def test_challenge_06_happy_case2(): 
     assert sum_of_squares([3,5,9]) == 115