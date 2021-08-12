def find_unique_friends_names(names: list) -> list:
    real_friends = list() # [] means the same thing here
    for name in names:
        # Alternative solution:
        # is_already_added = name in real_friends
        # if len(name) == 4 and not is_already_added: 
        is_not_already_added = name not in real_friends
        if len(name) == 4 and is_not_already_added: # add condition that checks if `name` is not already in `real_friends` list
            real_friends.append(name) 
    return real_friends

# element_is_not_there = "Michał" not in ["Martin", "dasdasdahh", "Zosia"]
# print(element_is_not_there)
# result_to_verify = friends(["Ryan", "Ryan"])
# expected_result = ["Ryan"]
# print(result_to_verify == expected_result)


# "Michał" in duplicated_names -> this syntax returns True or False
duplicated_names = ["Ryan", "Ryan", "Ryan", "Michał", "Ryan"]
expected_result = ["Ryan", "Michał"]
result_to_verify = find_unique_friends_names(duplicated_names)
print(result_to_verify == expected_result)

# Do not override special variables/functions (shadowing)
# print = "hello"
# print("I'm Michael")

# test.assert_equals(result_to_verify, expected_result)
# test.assert_equals(friend(["Ryan", "Jimmy", "123", "4", "Cool Man"]), ["Ryan"])
# test.assert_equals(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]), ["Jimm", "Cari", "aret"])