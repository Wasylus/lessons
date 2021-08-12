# player = 'Thomas'
# points = 33

# print(f'Last night, {player} scored {points} points.')




# print('I wrote %d programs today.' %3.75)

# print('I wrote %s programs today.' %3.75)

# print('I wrote %r programs today.' %'3.75')

# ex 7

def alarm_go_off():
    d = 24 # day is 24 hours
    h = 51  # hours till alarm
    t = (51 % 24) # time to add to 2pm after 51 hours

# when start is 12 am, and we add 51 h
# after 24h => 12 am, after next 24h => 12 am, after adding remainder which is 3h => 3 am


# 14 + 3 -> 17
def alarm_go_off():
    hours_in_day = 24
    hours_to_add = 51
    start_hour = 14 
    final_hour = start_hour + hours_to_add
    return final_hour % hours_in_day

# 120s -> our program -> 2min 0s
# 64s -> our program -> 1min 4s

def secs_to_min(num_seconds: int) -> str:
    num_minutes = num_seconds // 60
    seconds_remaining = num_seconds % 60
    formatted_repr = str(num_minutes) + "min " + str(seconds_remaining) + "sec"
    return formatted_repr

def secs_to_min(num_seconds: int) -> str:
    num_minutes = num_seconds // 60
    seconds_remaining = num_seconds % 60
    return f"{num_minutes}min {seconds_remaining}sec"
    # formatted_repr = "{}min {}sec".format(num_minutes, seconds_remaining)
    # "1min 4sec"
    # return formatted_repr

some_string = secs_to_min(64)
print(some_string.upper())
# print("ohhh i got some result", some_string)
# result = alarm_go_off()
# print(result)


def solution(letters):
    result = ""
    for l in letters:
        if l.isupper():
            # append space and l to final result
            # "H" -> " H"
            result += " " + l
        else:
            # "h" => "h"
            # append l (rewrite)
            # result.append(l)
            result += l
    return result

print(solution("helloWorld"))
    

def a_bigger(a, b):
    if a > b and a-b >= 2:
        return True
    return False

print(a_bigger(6, 2))
