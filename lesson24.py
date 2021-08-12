# print 3 separate lines
print("line1\nline2\nline3")

first_line = "------------\n"
last_line = first_line

box = first_line + "|something|\n" + last_line
print(box)


# continue from on the same line
print("line1", end=" ")
print("same line")