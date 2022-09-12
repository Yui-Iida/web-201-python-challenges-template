# Write a function in Python that accepts a list of 
# any length that contains a mix of non-negative 
# integers and strings. The function should return 
# a list with only the integers in the original 
# list in the same order.

def extract_integers(mixed_list):
    number_list = []
    for item in mixed_list:
        if(type(item) == int):
        # if(int(item) == True):
             number_list.append(item)
    return number_list

def test_challenge_05_happy_case(): 
     assert extract_integers([1, 'apple', 2, 'banana',3, 4]) == [1,2,3,4]   
     
def test_challenge_05_happy_case2(): 
     assert extract_integers([7, 'cat', 99, 'bird',105, 4]) == [7,99,105,4]   