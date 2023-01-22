# Convert a string to a new string where each character in the new string is "(" # if that character appears only once in the original string, or ")" if that character appears more than once in the original string.
# Ignore capitalization when determining if a character is a duplicate.
#
# Examples
#
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))(("
# Notes
#
# Assertion messages may be unclear about what they display in some languages.
# If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!
#

example_one = "supper"


def letter_conversion(letter_count: int) -> chr:
    if letter_count > 1:
        return ')'
    return '('


def recurring_letter(word: str):
    casted_letters = ""
    for letter in word:
        letter_count = 0
        for current_letter in word:
            if current_letter == letter:
                letter_count += 1
        casted_letters = casted_letters + letter_conversion(letter_count)
    print(str(casted_letters))
        # print(letter_conversion(letter_count))
        # print('The letter', letter, 'appears', letter_count)


recurring_letter(example_one)



