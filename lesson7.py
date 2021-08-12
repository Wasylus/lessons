# def if_demo(s):
#   if s == 'Hello' or s == 'Hi':
#     s = s + ' nice to meet you'
#   else:
#     s = s + ' woo hoo!'
#   return s

def is_a_bigger_than_b(a, b):
  if a > b:
    return True
  return False

def is_a_bigger_than_b(a, b):
  if a - b > 0:
    return True
  return False

def is_a_bigger_than_b(a, b):
  return a > b

print(is_a_bigger_than_b(4, 2))
print(4 > 2)

def print_names(names):
  for name in names:
    print(name)

def find_needle(haystack: list) -> str:
  index = 0
  for element in haystack:
    # here visit a single list element
    if element == "needle":
      message = "found needle at index "
      return message + str(index)
    
    index += 1    

print(find_needle(["hello", "adsasd", "gggg", "needle"]))
# def find_needle(haystack: list) -> str:
#   list_length = len(haystack)  # 4
#   for index in range(list_length): # [0, 1, 2, 3]
#     if haystack[index] == "needle": # get element at index position
#       message = "found needle at index "
#       return message + str(index)

# def find_needle(haystack: list) -> str:
#   for index in range(len(haystack)): # [0, 1, 2, 3]
#     if haystack[index] == "needle": # get element at index position
#       message = "found needle at index "
#       return message + str(index)


# def find_needle(haystack: list) -> str:
#   index = 0
#   # while loop exits when index is 4, because 4 < 4 gives False
#   while index < len(haystack): 
#     # print("starting loop iteration with index: ", index)
#     if haystack[index] == "needle": # get element at index position
#       message = "found needle at index "
#       return message + str(index)
#     index += 1
#     # print("i'm prepared for next iteration, index:", index)
#   return None

# def find_needle(haystack: list) -> str:
#   # 0, "hello"
#   # 1, "asdasda"
#   # 2, "gggg"
#   for idx, element in enumerate(haystack):
#     if element == "needle":
#       msg = element + "helohelo"
#       return f"Found neeedle at {idx}, with message {msg}"
#   return None

# def find_needles(haystack: list) -> str:
#   results = []
#   for idx, element in enumerate(haystack):
#     if element == "needle":
#       # remember `idx` in our tmp memory called `result`
#       results.append(idx)
#     # to show that we visit each element until the end
#     # else:
#     #   results.append("it's not a needle")
#   # result is returned after we visit every single element on haystack list
#   return results

# our_list = [1, 2, 3, "g", 41.5]
# print(our_list[4])
# our_list.append("new element")
# print(our_list)

# print(find_needle(["hello", "adsasd", "gggg", "it's not a needle"]))
# print(find_needles([123.123, "needle", "needle", "anything"]))
  
a: list = [111, 222, 333, 444]
element_at_index_three = a[3] 
