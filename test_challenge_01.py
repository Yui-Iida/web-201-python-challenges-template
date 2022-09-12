# Create a function in Python that accepts a single word and 
# returns the number of vowels in that word. 
# In this function, only a, e, i, o, and u 
# should be counted as vowels — not y.

def count_vowels(word):
    count_vowels = 0
    VOWELS = "aeiou"
    for letter in word:
        if letter in VOWELS: 
            count_vowels += 1
    return count_vowels
    

def test_challenge_01_myname_case(): 
     assert count_vowels('yui iida') == 5

def test_challenge_01_python_case(): 
     assert count_vowels('Create a function in Python') == 9

