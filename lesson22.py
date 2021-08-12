# test.assert_equals(nth_fib(3), 1, "3-rd Fibo")
# test.assert_equals(nth_fib(4), 2, "4-th Fibo")
# test.assert_equals(nth_fib(5), 3, "5-th Fibo")
# test.assert_equals(nth_fib(6), 5, "6-th Fibo")
# test.assert_equals(nth_fib(7), 8, "7-th Fibo")


# def fib(n):
#     pass
# def fib(n):
#     raise NotImplementedError
# test.assert_equals(fib(1), 0, "1-st Fibo")

# test.assert_equals(fib(2), 1, "2-nd Fibo")
# F(1) F(2) F(3) F(4) F(5)
# 0,   1,   1,   2,    3,   5, 8, 13, 21, 34, 55, 89, 144

# def nth_fib(n: int) -> int:
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     print(n)
#     return nth_fib(n-1) + nth_fib(n-2)

# def nth_fib(n: int) -> int:
#     if n == 1 or n == 2:
#         return n - 1
#     return nth_fib(n-1) + nth_fib(n-2)

def nth_fib(n: int) -> int:
    if n < 1:
        raise ValueError
    if n <= 2:
        return n - 1
    print(n)
    return nth_fib(n-1) + nth_fib(n-2)

# n = int(input("Give me some n:"))

nth_result = nth_fib(2)
print(nth_result)