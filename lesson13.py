def xor(a: bool, b: bool) -> bool:
    if a == False and b == False:
        return False
    elif a == True and b == False:
        return True
    elif a == False and b == True:
        return True
    elif a == True and b == True:
        return False

def xor(a: bool, b: bool) -> bool:
    if not a and not b:
        return False
    elif a and not b:
        return True
    elif not a and b:
        return True
    elif a and b:
        return False
    
def xor(a: bool, b: bool) -> bool:
    # Handles cases:
    # 1. False == False which is True 
    # 4. True == True which is also True
    if a == b: 
        return False
    else:
        return True


def xor(a: bool, b: bool) -> bool:
    # Handles cases:
    # 2. True != False which is True 
    # 3. False != True which is also True
    if a != b: 
        return True
    return False

def xor(a: bool, b: bool) -> bool:
    return a != b
    # Alternative solution
    # return a is not b
    
# 1. false xor false == false // since both are false
# 2. true xor false == true // exactly one of the two expressions are true
# 3. false xor true == true // exactly one of the two expressions are true
# 4. true xor true == false // Both are true.  "xor" only returns true if EXACTLY one of the two expressions evaluate to true.
print(xor(False, False))
print(xor(True, False))
print(xor(False, True))
print(xor(True, True))

# bool('asdasd') == True
# bool('') == False
# bool() == False


# a == False
# if a is True then the expression is: False
# if a is False then the expression is: True
# `a==False` is equivalent to `not a`