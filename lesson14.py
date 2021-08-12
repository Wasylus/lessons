
# exe3

# a > b opposite a < b

# 0 1 2 3 4 5 6 7 8 9
#----------------------------------
# a >= b  oppsite a <= b (bad solution)
a = 6
b = 5
# True              True <- should be False (we want the opposite)
#------------------------------------
# a >= b opposite a < b (good solution)
a = 5
b = 5
# True              False 

a > 7
# 8, 9

a <= 7
# 0, 1, 2, 3, 4, 5, 6, 7


# 3. a >= 18  and  day == 3 oppsite not (a < 18 and day == 3)
# 3. a >= 18  and  day == 3 oppsite  not(a >= 18) or not(day == 3)
# 3. a >= 18  and  day == 3 oppsite  a < 18 or day != 3

# 4. a >= 18  and  day != 3 oppsite a < 18 or day == 3
# 4. a >= 18  and  day != 3 oppsite not ( a >= 18 or day != 3)
# 4. a >= 18  and  day != 3 oppsite not (a >= 18) or not(day != 3)

# exe4
# 3 == 3
# True
# 3 != 3
# False
# 3 >= 4
# False
# not (3 < 4)
# False

# # exe5

# FFF = True
# FFT = True
# FTF = True


# (not (p and q)) or r
# (not True) or r
# False or r
# False or True
# True

# FTT = True

# (not (P and Q)) or r
# (not True) or r
# False or r
# False or True
# True

# TFF = True

# (not (P and Q)) or r
# (not True) or r
# False or True
# True

# TFT = True 

# (not (P and Q)) or r
# (not True) or r
# False or True
# True

# TTF = True

# (not (P and Q)) or r
# (not True) or r
# False or False
# False

# TTT = True

# (not (P and Q)) or r
# (not True) or True
# False or True
# True



# exe6
def mark_to_grade(mark: float) -> str: 
    # Second        Upper_Second         # First
    # [60, ..., 69] [70 71 72 73 74] [75 76 77 78 79 80)
    if mark >= 75:
        return "First"
    # Make it correct
    elif mark >= 70:
        return "Upper Second"
    elif mark >= 60:
        return "Second"
    elif mark >= 50:
        return "Third"
    elif mark >= 45:
        return "F1 Supp"
    elif mark >= 40:
        return "F2"
    else:
        return "F3"



xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]
for mark in xs:
    grade = mark_to_grade(mark)
    print(grade)