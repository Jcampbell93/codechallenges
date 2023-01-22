# Clock shows h hours, m minutes and s seconds after midnight.
#

# from time import gmtime, strftime
# print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

# Your task is to write a function which returns the time since midnight in milliseconds.
#
# Example:
# h = 0
# m = 1
# s = 1
#
# result = 61000
# Input constraints:
#
# 0 <= h <= 23
# 0 <= m <= 59
# 0 <= s <= 59
# 1 Hour = 3600000 ms
# 1 Minute = 60000 ms
# 1 second = 1000 ms
hours = 23
minutes = 59
seconds = 59


def past(h, m, s):
    hour_ms = h * 3600000
    minute_ms = m * 60000
    second_ms = s * 1000

    return hour_ms + minute_ms + second_ms


print(past(hours, minutes, seconds))
