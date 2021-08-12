# test.assert_equals(nth_fib(1), 0, "1-st Fibo")
# test.assert_equals(nth_fib(2), 1, "2-nd Fibo")
# test.assert_equals(nth_fib(4), 2, "4-th Fibo")
# test.assert_equals(nth_fib(5), 3, "5-th Fibo")
# test.assert_equals(nth_fib(6), 5, "6-th Fibo")
# test.assert_equals(nth_fib(7), 8, "7-th Fibo")
# test.assert_equals(nth_fib(3), 1, "3-rd Fibo")

# def nth_fib(n: int) -> int:
#     former = 0
#     latter = 1 
#     if n == 1:
#         return former
#     elif n == 2:
#         return latter
#     for _ in range(n - 2):
#         nth = former + latter
#         former = latter
#         latter = nth
#     return nth    


def nth_fib(n: int) -> int:
    former = 0
    latter = 1 
    if n == 1:
        return former
    elif n == 2:
        return latter
    # we don't care about iteration index
    for _ in range(n - 2): # for n=4, [0, 1]
        # 8 = 3      + 5
        nth = former + latter
        # former = 5
        former = latter
        # latter = 8
        latter = nth
    return nth    

#          f  l  n
#             f  l  n
#                f  l  n
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
def nth_fib(n: int) -> int:
    loop_counter = 0
    former = 0
    latter = 1 
    if n == 1:
        return former
    elif n == 2:
        return latter
    # we need some kind of index/counter variable
    # to control how many times the loop executes
    while loop_counter < n - 2:
        # 8 = 3      + 5
        nth = former + latter
        # former = 5
        former = latter
        # latter = 8
        latter = nth
        # we need to manually take care of increasing that counter
        loop_counter += 1
    return nth    

nth_result = nth_fib(8)
print(nth_result)

# start at 6, end at 1 (excluding), with step -2
# print(list(range(6, 1, -2)))
