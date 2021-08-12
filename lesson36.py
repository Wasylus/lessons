from typing import List, Union, Any



NumericValue = Union[int, float] 
NumericalList = List[NumericValue]


[
    [1,2,3], 
    [4,24, [
        'staasdasda'
        ]],
    [11,22,3444], 
]

# original_book = [1, 1, 2, 3, 1, 2, 3, 4]
# forbidden_pages = [1, 3]
# new_book = [2, 2, 4]
# alegory: book, page
class My_List():
    def filter_out(source: NumericalList, values: NumericalList) -> NumericalList:
        for page in original_book:
            # if (page == 1) or (page == 3):
            if page in forbidden_pages:
                continue
            else:
                new_book.append(page)
                return new_book:

            

        """
        This function takes a `source` list and removes elements that are present in `values` list,
        Then it returns that list.
        """

        pass




# class List(object):
#     def remove_(self, integers: list, values: list) -> list:
#         new_list = []
#         for e in integers:
#             if e not in values:
#                 new_list.append(e)
#             # unnecessary code
#             # else:  # e in values
#             #     # we shouldnt put that nunber into new_list
#             #     pass
#         return new_list

l = List()
integer_list = [1, 1, 2, 3, 1, 2, 3, 4]
values_list = [1, 3]
returned_result = l.remove_(integer_list, values_list)

# Simplest way (need to manually check if we see a good result)
print(returned_result) 

# Let's say it's similar to a test case, we'll see True or False in the output
test_passed: bool = returned_result == [2, 2, 4]
print(test_passed)

# Better way: exception will contain all information about failure
assert returned_result == [2, 2, 4]
