jack = "All work and no play make Jack a dull boy"

words = ["All", "work", "and"]
print(words)

first_word = "All"
second_word = "work"
third_word = "and"

print(first_word, second_word, third_word, end=" endddd")


# Excercise 2.
result = 6 * (1 - 2)
print(result)


# Excercise 3.
# print("hello")

# Exercise 4.


# Exercise 5.
# def earning_compound_interest(t: int) -> float:
#     p = 10000
#     r = 0.08
#     n = 12
#     return p * (1 + r / n)**(n * t)

def earning_compound_interest(p: int, t: int, r: float, n: int) -> float:
    # may want to reduce to one statement
    A = p * (1 + r / n)**(n * t)
    return A
    

result_without_kwargs = earning_compound_interest(10000, 6, 0.08, 12)
result_with_kwargs = earning_compound_interest(t=6, r=0.08, n=12, p=10000)

are_equal = result_without_kwargs == result_with_kwargs
print(are_equal)


print()
# print(result, type(result))