# https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python

# def _():
#     test.assert_equals(likes([]), 'no one likes this')
#     test.assert_equals(likes(['Peter']), 'Peter likes this')
#     test.assert_equals(likes(['Michał']), 'Michał likes this')
#     test.assert_equals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
#     test.assert_equals(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
#     test.assert_equals(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')

# names should be of type list
# and we return something of type string
def likes(names: list) -> str:
    # if names has 0 elements
    #    then return some string
    if len(names) == 0:
        return "no one like this"
    if len(names) == 1:
        name = names[0]
        return name + " likes this"
    # Jacob and Alex (use [0] and [1])
    if len(names) == 3:
        return name + "likes this"
        # String concatenation
        # Try f-string (f"{}")
        # Try .format 
        # MUST RETURN HERE, example: "Max, Jacob and Alex" (use [0] [1] [2])
    pass
    if len(names) >= 4:
        return "Alex, Jacob and 2 others like this"
        # Alex, Jacob and 2 others like this
        # if there are a hundred names then return:
        # "SomeName, SomeOtherName and 98 others like this"

        # if there are 120 names then return:
        # "SomeName, SomeOtherName and 118 others like this"
        # first_name = names[0]
        # second_name = names[1]
        # MUST RETURN HERE
        

    return None

# print([111, 222, 333, 444][1]) 
    
fb_message = likes(['Alex', 'Jacob', 'Mark', 'Max'])
print(fb_message)