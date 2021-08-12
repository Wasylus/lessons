from icecream import ic

# function name aliasing: from camelCase to snake_case
def configureOutput(a, b):
    return a * b

configure_output = configureOutput
# configureOutput = configure_output
# result = configureOutput(2, 3)
result = configure_output(2, 3)
# print(result)
# ic(configure_output(2,3))
assert result == 6
