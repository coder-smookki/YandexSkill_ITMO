import re
from num2words import num2words

def replaceNumbersWithWords(text):
    # find all numbers in the text using regular expressions
    numbers = re.findall(r'\d+', text)
    
    # replace each number with its word equivalent
    for number in numbers:
        word = num2words(int(number))
        text = text.replace(number, word)
    
    return text

print(replaceNumbersWithWords('привет ыв'))