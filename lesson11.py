print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

SMALL = "S"
MEDIUM = "M"
LARGE = "L"

YES = "Y"
NO = "N"

PIZZA_SIZE_TO_BASE_PRICE = {
  SMALL: 15, 
  MEDIUM: 20,
  LARGE: 25
}

PRICE_FOR_PEPPERONI = {
  SMALL: 2,
  MEDIUM: 3,
  LARGE: 3
}

# There are even more approaches:
# enum
# match case statement

# we want to be case insensitive
size = size.upper()

# Approach II using dictionaries
# PRICE_FOR_PEPPERONI.get(size, 1000)
bill = PIZZA_SIZE_TO_BASE_PRICE[size]
bill += PRICE_FOR_PEPPERONI[size]

# Approach I using if-elif-else and constants
# PRICE_FOR_SMALL = 15
# PRICE_FOR_MEDIUM = 20
# PRICE_FOR_LARGE = 25
PRICE_FOR_CHEESE = 1

# bill = 0
# if size == SMALL:
#   bill = PRICE_FOR_SMALL
# elif size == MEDIUM:
#   bill = PRICE_FOR_MEDIUM
# elif size == LARGE:
#   bill = PRICE_FOR_LARGE
# else:
#     exit()
# if add_pepperoni == YES:
#     if size == SMALL:
#         bill += 2
#     elif size == MEDIUM or size == LARGE:
#         bill += 3
#     else:
#         bill += 4

if extra_cheese == YES:
  bill += PRICE_FOR_CHEESE

final_bill = f"Your final bill is: ${bill}."
print(final_bill)


