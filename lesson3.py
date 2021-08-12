# def is_odd(num):
#     # 4 % 2 = 0
#     # 5 % 2 = 1
#     # parzyste = even
#     # nieparzyste = odd
#     if ((num % 2) == 0):
#         print("is even")
#     else:
#         print("is odd")

# def is_odd(num: int) -> bool:
#     # parzyste = even
#     # nieparzyste = odd
#     if num % 2 == 0:
#         return False
#     else:
#         return True
        




def is_odd(num: int) -> bool:
    return num % 2 != 0


result = is_odd(1)
print(result)

# def is_even(num: int) -> bool:
#     remainder = num % 2
#     return remainder == 0

def is_even(num):
    return not is_odd(num)

result = is_even(9)
print(result)