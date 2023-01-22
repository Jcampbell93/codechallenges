# A pangram is a sentence that contains every single letter of the alphabet at least once.
# For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
# because it uses the letters A-Z at least once (case is irrelevant).
#
# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
#

import string

full_alphabet = list(string.ascii_letters)
lowercase_alphabet = full_alphabet[:26]

# print(lowercase_alphabet)

test_pangram = "The quick brown fox jumps over the lazy dog"  # IS PANGRAM


def is_pangram(string):
    for alphabet_letter in lowercase_alphabet:
        letter_found = False
        for string_letter in string:
            if alphabet_letter.lower() == string_letter.lower():
                letter_found = True
                break
        if not letter_found:
            return False

    return True



print(is_pangram(test_pangram))



def is_pangram_two(string):
    for alphabet_letter in lowercase_alphabet:
        for string_letter in string:
            if alphabet_letter.lower() != string_letter.lower():
                continue


    return True

