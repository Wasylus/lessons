# https://www.codewars.com/kata/55a2d7ebe362935a210000b2/train/python

# test.assert_equals(find_smallest_int([78, 56, 232, 12, 11, 43]), 11)
# test.assert_equals(find_smallest_int([78, 56, -2, 12, 8, -33]), -33)
# test.assert_equals(find_smallest_int([0, 1-2**64, 2**64]), 1-2**64)

# Oprations that we can use:
# comparison <
# visiting list elements
# remembering numbers (storing in variables)


# # will work only for 6 elements
def find_smallest_int(numbers):
    lowest = numbers[0]
    if lowest > numbers[1]:
        lowest = numbers[1]

    if lowest > numbers[2]:
        lowest = numbers[2]

    if lowest > numbers[2]:
        lowest = numbers[2]

    # lowest = 56, numbers[3] = 12, which is True
    if lowest > numbers[3]:
        # we found new lowest value
        # now 12 is the lowest
        lowest = numbers[3]

    # lowest = 12, numbers[4] = 11, which is True
    if lowest > numbers[4]:
        # we found new lowest value
        # now 11 is the lowest
        lowest = numbers[4]

    # lowest = 11, numbers[5] = 43
    if lowest > numbers[5]:
        lowest = numbers[5] 
    
    return lowest
# note after running this with full list including the negative numbers (-1, -123, -1231231) 
# the resul was still 11. Only when I reduced the list to 5 arrguments an error occured saying 
# list was out of range obviously because of lack of proper amount of arrguments.

# def find_smallest_int(numbers):
#     list_length = len(numbers)
#     lowest = numbers[0]
#     # range will return numbers from range 0 to its (argument - 1)
#     for index in range(list_length):
#         if lowest > numbers[index]:
#             lowest = numbers[index]
#     return lowest

# final code
# def find_smallest_int(numbers: list) -> int:
#     smallest = numbers[0]
#     for potentially_smallest in numbers:
#         if smallest > potentially_smallest:
#             smallest = potentially_smallest
#     return smallest


list_from_boss = [78, 56, 232, 12, 11, 43]
lowset_value = find_smallest_int(list_from_boss)
print(lowset_value)
    

