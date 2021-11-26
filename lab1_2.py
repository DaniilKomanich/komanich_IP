# -*- coding: cp1251 -*-
alpabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
monograms_list = 'оеаинтсрвлкмдпуяыьгзбчйхжшюцщэфъё'

def freq():
    frequencies = {}
    for k in alpabet:
        frequencies[k] = 0

    for sym in message:
        if sym != ' ':
            frequencies[sym] += 1
    return frequencies

def monograms(frequencies, message):
    crypt_monograms = ''
    for key, value in frequencies.items():
        i = 0
        while i < len(crypt_monograms) and value <= frequencies[crypt_monograms[i]]:
            i += 1
        crypt_monograms = crypt_monograms[:i] + key + crypt_monograms[i:]

    decrypt_message1 = ''
    for sym in message:
        if sym == ' ':
            decrypt_message1 += sym
        else:
            decrypt_message1 += monograms_list[crypt_monograms.find(sym)]
    try:
        f = open("book_monograms.txt", "w")
        try:
            f.write("Расшифроввка текста по монограммам: ")
            f.writelines(decrypt_message1)
        finally:
            f.close()
    except IOError:
        pass
    return crypt_monograms

def bigrams(text):
    bigrams = {}
    for i in range(len(text)-1):
        if text[i] == ' ' or text[i+1] == ' ':
            continue
        if text[i:i+2] not in bigrams.keys():
            bigrams[text[i:i+2]] = 1
        else:
            bigrams[text[i:i+2]] += 1
    return bigrams

def crypt_bigrams(message):
    crypt_bigrams = {}
    for i in range(len(message)-1):
        if message[i] == ' ' or message[i+1] == ' ':
            continue
        if message[i:i+2] not in crypt_bigrams.keys():
            crypt_bigrams[message[i:i+2]] = 1
        else:
            crypt_bigrams[message[i:i+2]] += 1
    return crypt_bigrams

def bigrams2(bigrams):
    bigrams2 = []
    for i in range(10):
        maxx = 0
        bigram = ''
        for key, value in bigrams.items():
            if value > maxx:
                bigram = key
                maxx = value
        bigrams2.append(bigram)
        bigrams.pop(bigram)
    return bigrams2

def cr_bigrams2(crypt_bigrams):
    crypt_bigrams2 = []
    for i in range(10):
        maxx = 0
        bigram = ''
        for key, value in crypt_bigrams.items():
            if value > maxx:
                bigram = key
                maxx = value
        crypt_bigrams2.append(bigram)
        crypt_bigrams.pop(bigram)
    return crypt_bigrams2

def move_two_letters(s, a, b):
    if a > b:
        r = a
        a = b
        b = r
    s1 = s[:a]
    s2 = s[a+1:b]
    s3 = s[b+1:]
    return s1 + s[b] + s2 + s[a] + s3

def decrypt_2(crypt_bigrams10, crypt_monograms, bigrams10):
    moved_letters = []
    for i in range(len(bigrams10)):
        let1 = crypt_monograms.find(crypt_bigrams10[i][0])
        let2 = monograms_list.find(bigrams10[i][0])

        if let1 != let2 and crypt_bigrams10[i][0] not in moved_letters:
            crypt_monograms = move_two_letters(crypt_monograms, let1, let2)
            moved_letters.append(crypt_monograms[let1])
            moved_letters.append(crypt_monograms[let2])

        let1 = crypt_monograms.find(crypt_bigrams10[i][1])
        let2 = monograms_list.find(bigrams10[i][1])

        if let1 != let2 and crypt_bigrams10[i][1] not in moved_letters:
            crypt_monograms = move_two_letters(crypt_monograms, let1, let2)
            moved_letters.append(crypt_monograms[let1])
            moved_letters.append(crypt_monograms[let2])

    crypt_monograms.find('о'), monograms_list.find('л')

    decrypt_message2 = ''
    for sym in message:
        if sym == ' ':
            decrypt_message2 += sym
        else:
            decrypt_message2 += monograms_list[crypt_monograms.find(sym)]
    try:
        f = open("book_bigrams.txt", "w")
        try:
            f.write("Расшифровка текста по биграммам: ")
            f.writelines(decrypt_message2)
        finally:
            f.close()
    except IOError:
        pass

def caesar(alpabet, text):
    message = ''
    for sym in text:
        if sym.isalpha():
            message += alpabet[(alpabet.find(sym) + key) % 33]
        else:
            message += sym
    return message

if __name__ == '__main__':
    with open('book.txt', 'r', encoding="utf-8") as f:
        text = f.read()
        text = "".join(c for c in text if c == ' ' or c == 'n' or c.isalpha()).lower()
        print(text)
        key = int(input('Введите числовой ключ: '))
        c = 0
    message = caesar(alpabet, text)
    frequencies = freq()
    cr_mono = monograms(frequencies, message)
    bigrams = bigrams(text)
    cr_bigr = crypt_bigrams(message)
    bigr2 = bigrams2(bigrams)
    crypt_bigrams2 = cr_bigrams2(cr_bigr)
    decrypt_2(crypt_bigrams2,cr_mono, bigr2)