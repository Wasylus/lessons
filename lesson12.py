
# print(int(bmi))

# # 1. What if bmi is 13 
 # # 2. What if bmi is 33


# if bmi <= 18:
#   print("Your BMI is 18, you are underweight.")
# elif bmi >= 22:
#   print("Your BMI is 22, you have a normal weight.")
# elif bmi >= 28:
#   print("Your BMI is 28, you are slightly overweight.")
# elif bmi >= 33:
#   print("Your BMI is 33, you are obese.")
#   print("Your BMI is 40, you are clinically obese.")

# result = int(bmi)
# print(result)
def calculate_bmi(weight: float, height: float) -> float:
    return weight / height ** 2

def bmi_to_str(bmi: int) -> str:
    if bmi < 18: 
        return "underweight"
    elif bmi < 25:
        return "normal weight"
    elif bmi < 30:
        return "overweight"
    elif bmi < 35:
        return "obese"
    else: 
        return "clinically obese"

# Homework: check math.ceil, math.floor, math.round
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = calculate_bmi(weight, height)
bmi_repr = bmi_to_str(bmi)
msg = f"Your bmi is {int(bmi)}, you are {bmi_repr}"
print(msg)