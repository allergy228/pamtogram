import string

def is_pangram(sentence):
    sentence = sentence.lower()
    for char in string.ascii_lowercase:
        if char not in sentence:
            return False
    return True

text = "The quick brown fox jumps over the lazy dog"
if is_pangram(text):
    print("Строка является панграммой.")
else:
    print("Строка не является панграммой.")
