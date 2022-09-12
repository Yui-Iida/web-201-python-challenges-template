# Supermarket billing: Write a function in python that 
# takes a shopping list (dictionary of items and price) and returns the total.
# extension: apply discount accordingly:
# if total is greater than 50 Euros 5% discount.
# if total is greater than 60 Euros 6% discount.
# if total is greater than 70 Euros 7% discount and so on.

def calculate_bill(shopping_list):
    total = 0
    for cost in shopping_list.values():
        total = total + cost
        if(total >= 50):
            total = total * 0.95
    return total
        

def test_challenge_07_happy_case(): 
    shopping_list1 = {'apples':11.20, 'bananas':2.2, 'eggs':30.00}
    assert calculate_bill(shopping_list1) == 43.4


def test_challenge_07_happy_case2(): 
    shopping_list2 = {'apples':50, 'bananas':60, 'eggs':50}
    # (50 + 60 + 50) * 0.95 = 152
    assert calculate_bill(shopping_list2) == 152