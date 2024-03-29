import re
from num2words import num2words


# a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z,.
dic = {
    'эй': 'a',
    'а': 'a',
    'э': 'a',

    'би': 'b',
    'б': 'b',
    'бэ': 'b',
    'бе': 'b',

    'цэ': 'c',
    'це': 'c',
    'ц': 'c',
    'си': 'c',

    'ди': 'd',
    'дэ': 'd',
    'де': 'd',
    'д': 'd',

    'е': 'e',
    'и': 'e',

    'эф': 'f',
    'фэ': 'f',
    'фе': 'f',
    'ф': 'f',

    'ж': 'g',
    'жэ': 'g',
    'же': 'g',
    'джэ': 'g',
    'дже': 'g',
    'джи': 'g',
    'тжи': 'g',
    'тже': 'g',
    'тжэ': 'g',

    'аш': 'h',
    'х': 'h',
    'ш': 'h',
    'ше': 'h',
    'шэ': 'h',
    'ха': 'h',

    'ай': 'i',

    'джей': 'j',
    'дж': 'j',

    'к': 'k',
    'кэ': 'k',
    'ке': 'k',
    'ка': 'k',
    'кей': 'k',
    'кэй': 'k',

    'л': 'l',
    'эл': 'l',
    'ли': 'l',
    'лэ': 'l',
    'ле': 'l',
    'лы': 'l',

    'м': 'm',
    'мы': 'm',
    'мэ': 'm',
    'ме': 'm',
    'эм': 'm',
    'ем': 'm',

    'н': 'n',
    'эн': 'n',
    'ен': 'n',
    'ны': 'n',
    'нэ': 'n',
    'не': 'n',

    'о': 'o',
    'оу': 'o',

    'п': 'p',
    'пи': 'p',
    'пэ': 'p',
    'пе': 'p',

    'ку': 'q',
    'кью': 'q',

    'эр': 'r',
    'р': 'r',
    'ры': 'r',
    'ар': 'r',
    'ре': 'r',
    'рэ': 'r',

    'эс': 's',
    'с': 's',
    'сэ': 's',
    'се': 's',

    'т': 't',
    'ти': 't',
    'тэ': 't',
    'те': 't',

    'у': 'u',
    'ю': 'u',

    'ви': 'v',
    'вэ': 'v',
    'ве': 'v',
    'в': 'v',

    'даблю': 'w',
    'уэ': 'w',

    'икс': 'x',
    'кс': 'x',

    'игрик': 'y',
    'й': 'y',

    'з': 'z',
    'зэд': 'z',
    'зед': 'z',
    'зы': 'z'
}


def rusLetterToEng(string):
    if string in dic:
        return dic[string.lower()]
    return string

def replaceNumbersWithWords(text):
    # find all numbers in the text using regular expressions
    numbers = re.findall(r'\d+', text)
    
    # replace each number with its word equivalent
    for number in numbers:
        word = num2words(int(number))
        text = text.replace(number, word)
    
    return text