


# def num_to_day_of_week(num):
#     if num == 0:
#         return "monday"
#     if num == 1:
#         return "tuesday"
#     if num == 2:
#         return "wednesday"
#     if num == 3:
#         return "thursday"

# def num_to_day_of_week(num):
#     result = None
#     if num == 0:
#         result = "monday"
#     if num == 1:
#         result = "tuesday"
#     if num == 2:
#         result = "wednesday"
#     if num == 3:
#         result = "thursday"
#     if num == 4:
#         result = "friday"
#     return result

# def num_to_day_of_week(num):
#     result = "there's no such day of week for that number"
#     if num == 0:
#         result = "monday"
#     elif num == 1:
#         result = "tuesday"
#     elif num == 2:
#         result = "wednesday"
#     elif num == 3:
#         result = "thursday"
#     elif num == 4:
#         result = "friday"
#     return result

# # def num_to_day_of_week(num):
# #     if num == 0:
# #         result = "monday"
# #     elif num == 1:
# #         result =  "tuesday"
# #     elif num == 2:
# #         result = "wednesday"
# #     elif num == 3:
# #         result = "thursday"
# #     elif num == 4:
# #         result = "friday"
# #     # There's no variable called result
#     return result

# def num_to_day_of_week(num):
#     if num == 5:
#         return "monday"
#     if num == 3:
#         return "tuesday"
#     if num == 7:
#         return "wednesday"
#     if num == 8:
#         return "thursday"


# def num_to_day_of_week(num):
#     days_of_week = ["monday", "tuesday", "wednesday"]
#     return days_of_week[num - 1]

# def num_to_day_of_week(num):
#     return ["monday", "tuesday", "wednesday"][num]


# def num_to_day_of_week(num):
#     num_to_dow = {
#         5: "monday",
#         3: "tuesday",
#         7: "wednesday",
#         8: "thursday"
#     }
#     return num_to_dow[num]



# print(num_to_day_of_week(800))


def is_even(num):
    return num % 2 == 0

def find_first_even_number(numbers):
    for n in numbers:
        result = is_even(n)
        # print("is number {} even? {}".format(n, result))
        if result is True:
            return n

# def find_first_even_number(numbers: list) -> int:
#     for n in numbers:
#         if is_even(n):
#             return n

def find_last_even_number(numbers: list) -> int:
    last_even = None
    for n in numbers:
        if is_even(n):
            last_even = n
    return last_even

# result = is_even(2)
# print(result)

last_even = find_last_even_number([1, 3, 2, 5, 6])
print(last_even)
  


