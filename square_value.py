def square_value_of_number(num):
    total = None
    # if type(num).is_integer:
    if type(num) is int:
        total = num * num
    return total 


def test_square_value_case_5():
    assert square_value_of_number(5) == 25
    
def test_square_value_case_10():
    assert square_value_of_number(10) == 100
    
def test_square_value_case_9():
    assert square_value_of_number("9") == None
    
    