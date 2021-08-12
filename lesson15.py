# test.assert_equals(validate_pin("1"),False, "Wrong output for '1'")
# test.assert_equals(validate_pin("12"),False, "Wrong output for '12'")
# test.assert_equals(validate_pin("123"),False, "Wrong output for '123'")
# test.assert_equals(validate_pin("12345"),False, "Wrong output for '12345'")
# test.assert_equals(validate_pin("1234567"),False, "Wrong output for '1234567'")
# test.assert_equals(validate_pin("-1234"),False, "Wrong output for '-1234'")
# test.assert_equals(validate_pin("-12345"),False, "Wrong output for '-12345'")
# test.assert_equals(validate_pin("1.234"),False, "Wrong output for '1.234'")
# test.assert_equals(validate_pin("00000000"),False, "Wrong output for '00000000'")


# example_pin = "00#0"
# print(example_pin)


# def validate_pin(pin: str) -> bool:
#     # 3 failing tests
#     if len(pin) == 4:
#         return True
#     elif len(pin) == 6:
#         return True
#     else:
#         return False

# def is_valid_int(some_string: str) -> int:
#     try:
#         return int(some_string)
#     except:
#         return False

# def has_digits_only(some_string: str) -> bool:
#     # inefficient, visits all even though we may find invalid at the beginning
#     digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     found_invalid_character = False
#     for character in some_string:
#         if character not in digits:
#             found_invalid_character = True
#     return not found_invalid_character


def has_digits_only(some_string: str) -> bool:
    # "return early" approach is better
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for character in some_string:
        if character not in digits:
            return False
    return True


# ctrl + alt + arrow down
# print(has_digits_only("123"))
# print(has_digits_only("-123"))
# print(has_digits_only("1.23"))
# print(has_digits_only("123a44"))
# print(has_digits_only("a231231231231231231231231"))

# def validate_pin(pin: str) -> bool:
#     if has_digits_only(pin):
#         if len(pin) == 4:
#             return True
#         elif len(pin) == 6:
#             return True
#         else:
#             return False
#     else:
#         return False


# def validate_pin(pin: str) -> bool:
#     if has_digits_only(pin):
#         if len(pin) == 4 or len(pin) == 6:
#             return True
#         else:
#             return False
#     else:
#         return False


# def validate_pin(pin: str) -> bool:
#     if has_digits_only(pin):
#         length = len(pin)
#         if length == 4 or length == 6:
#             return True
#         else:
#             return False
#     else:
#         return False

# def validate_pin(pin: str) -> bool:
    # if has_digits_only(pin):
        # if len(pin) in [4, 6]:
            # return True
        # else:
            # return False
    # else:
        # return False

# def validate_pin(pin: str) -> bool:
#     if has_digits_only(pin):
#         return len(pin) in [4, 6]
#     else:
#         return False


def validate_pin(pin: str) -> bool:
    if not pin.isdigit():
        return False
    return len(pin) in [4, 6]

def validate_pin(pin: str) -> bool:
    if pin.isdigit():
        return len(pin) in [4, 6]
    return False

# return early approach
# def sdasdas(asda):
#     # check if problem A exists
#         return
#     # check if problem B exists
#         return
#     # check if problem C exists
#         return
#     # check if problem D exists
#         return
#     do whatever we want, no problems found 

# is_valid = validate_pin("12345")
is_valid = validate_pin("-12345")
# is_valid = validate_pin("-12345")
# is_valid = validate_pin("1.234")
print(is_valid)
# Find a module/method that tells us whether a string has digits only (substitute for our impl of has_digits_only)


# .isdigit():
