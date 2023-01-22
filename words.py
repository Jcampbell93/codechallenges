# Sentence Smash
# Write a function that takes an array of words and smashes them together into a sentence and returns the sentence.
# You can ignore any need to sanitize words or add punctuation,
# but you should add spaces between each word.
# Be careful, there shouldn't be a space at the beginning or the end of the sentence!
#
# Example
# ['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'

words = ['hello', 'world', 'this', 'is', 'great']

def smash(words):
    result = ''
    for word in words:
        words_count = len(words)
        if word != words[words_count - 1]:
            result = result + word + " "
        else:
            result = result + word
    return result

print(smash(words))

