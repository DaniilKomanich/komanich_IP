#!/usr/bin/env python
#-- coding: cp1251 --

def alphabet(numberKey, stringKey):
    a = ord('а')
    alphabet = ''
    for i in range(a, a + 33):
        alphabet = alphabet + ''.join(chr(i))
    for sym in stringKey:
        alphabet = alphabet.replace(sym, '')
        alphabet = stringKey + alphabet
        a = numberKey % len(alphabet)
    for i in range(numberKey):
        alphabet = alphabet[-a:] + alphabet[:-a]
    return alphabet


if __name__ == '__main__':
    startMessage = input("Введите текст: ")
    try: numberKey = int(input("Введите числовой ключ: "))
    except ValueError: print("Ошибка: только целые числа!"); raise SystemExit
    stringKey = str(input("Введите ключевое слово: "))

abc = alphabet(numberKey, stringKey)
message = ''
for sym in startMessage:
    if sym.isalpha():
        message += abc[(ord(sym) - 224)%33]
    else:
        message += sym
print(message)
print(abc)