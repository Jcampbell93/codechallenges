
# Find the odd int
# Given an array of integers, find the one that appears an odd number of times.
#
# There will always be only one integer that appears an odd number of times.
#
# Examples
# [7] should return 7, because it occurs 1 time (which is odd).
# [0] should return 0, because it occurs 1 time (which is odd).
# [1,1,2] should return 2, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

numbers = [1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]

count = 0


def is_even(number: int) -> bool:
    return (number % 2) == 0


def count_the_numbers(numbers):
    for current_number in numbers:

        current_number_count = 0

        for checking_number in numbers:
            if checking_number == current_number:
                current_number_count += 1


       # print(current_number, 'occurs', current_number_count)
        if not is_even(current_number_count):
            print('The number with the odd amount of occurrences is', current_number)
            return

count_the_numbers(numbers)


def count_the_numbers_two(numbers: []):
    processed_numbers = {}

    for current_number in numbers:
        if str(current_number) in processed_numbers:
            processed_numbers[str(current_number)] += 1
        else:
            processed_numbers[str(current_number)] = 1

    for checking_number in numbers:
        if not processed_numbers[str(checking_number)] % 2 == 0:
            print('The odd number is', checking_number)


count_the_numbers_two(numbers)
