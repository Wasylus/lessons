# Offtopic:
# 1. How to swap values of two variables using a temporary variable
a = 1
b = 2
tmp = b  # 2 is our backup

# We can just swap them, not being afraid of losing original value of `b`, because we have a backup in `tmp`
b = a
# now `b` is 1
a = tmp
# now `a` is 2

# 2. How to swap values of two variables using a tuple (in one line)
# Explanation: https://stackoverflow.com/a/14836456
a, b = b, a
# which is the same as:  (but more explicit)
(a, b) = (b, a)