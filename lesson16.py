# import codewars_test as test
# from solution import people_with_age_drink

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it("should return 'drink toddy' when age is less than 14")
#     def _():
#         test.assert_equals(None, 'drink toddy', "Wrong result for 13")
#         test.assert_equals(people_with_age_drink(0), 'drink toddy', "Wrong result for 0")

#     @test.it("should return 'drink coke' when age is between 14(inclusive) and 18(exclusive)")
#     def _():
#         test.assert_equals(people_with_age_drink(17), 'drink coke')
#         test.assert_equals(people_with_age_drink(15), 'drink coke')
#         test.assert_equals(people_with_age_drink(14), 'drink coke')
        
#     @test.it("should return 'drink beer' when age is between 18(inclusive) and 21(exclusive)")
#     def _(): 
#         test.assert_equals(people_with_age_drink(20), 'drink beer')
#         test.assert_equals(people_with_age_drink(18), 'drink beer')
        
#     @test.it("should return 'drink whisky' when age is greater than or equal to 21")
#     def _():
#         test.assert_equals(people_with_age_drink(22), 'drink whisky')
#         test.assert_equals(people_with_age_drink(21), 'drink whisky')

# Ctrl + f Ctrl + h (find and replace)
def what_to_drink(age: int) -> str:
    if age < 14:
        return "drink toddy"
    elif age < 18:
        return "drink coke"
    elif age < 21:
        return "drink beer"
    else: 
        return "drink whisky"
    
def what_to_drink(age: int) -> str:
    # return once, extract common things ("drink "), easier to introduce changes for all cases
    if age < 14:
       drink_type = "toddy"
    elif age < 18:
        drink_type = "coke"
    elif age < 21:
        drink_type = "beer"
    else: 
        drink_type = "whisky"
    return "drink " + drink_type


# age = int(input("How old are you? "))
result = what_to_drink(12)
print(result)