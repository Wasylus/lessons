# Test.assert_equals(factorial(0), 1, "factorial for 0 is 1");
# Test.assert_equals(factorial(1), 1, "factorial for 1 is 1");
# Test.assert_equals(factorial(2), 2, "factorial for 2 is 2");
# Test.assert_equals(factorial(3), 6, "factorial for 3 is 6");




# 20! = 6 * 5 * 4 * 3 * 2 * 1 = 720
# 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720
# 5! = 5 * 4 * 3 * 2 * 1 = 120
# 4! = 4 * 3 * 2 * 1 = 24 
# 3! = 3 * 2 * 1 = 6

# we don't want 0 and we want 4 but it's not there...
# range(4) -> [0, 1, 2
# we want this, because `stop` argument is exclusive, 
# we must artifically add 1 to reach `n`
# range(1, 5) -> [1, 2, 3, 4]
# range(1, n+1) -> [1, 2, 3, 4, ..., n]

# submitted solution
def factorial(n: int) -> int:
    if n < 0 or n > 12:
        raise ValueError

    product = 1  
    # range(1, 5+1) => [1, 2, 3, 4, 5]
    for factor in range(1, n + 1): 
        product = factor * product 

    return product

# Custom setting for recursion depth
# import sys
# sys.setrecursionlimit(2000)

def factorial(n):
    """
    5! = 5 * 4! = 5 * 4 * 3! = 5 * 4 * 3 * 2! =
    5 * 4 * 3 * 2 * 1 
    """
    # debug
    # print(n)
    # if n < 0 or n > 12:
    #     raise ValueError
    if n <= 1:
        return 1
    else:
        # result = n * factorial(n - 1)
        # print(f"{n} lvl, value: {result}")
        return n * factorial(n - 1)

factorial(5)
# def boss1():
#     try:
#         factorial(-100)
#     except ValueError:
#         raise

# def boss():
#     try:
#         boss1()
#     except ValueError:
#         raise

# boss()

# factorial(4)
# print(factorial(0))
# print("----------------")
# print(factorial(1))
# print("----------------")
# print(factorial(4))

# Stateful, mutation
# The difference between reversed() and .reverse()
# a = [1,2,3,4]
# b = a.reverse()
# print(a) # [4,3,2,1]
# print(b) # None

# Stateless
# print('-----------------------------')
# a = [1, 2, 3, 4]
# b = list(reversed(a))
# print(a)
# print(b)