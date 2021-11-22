import math
import random

def RSA(p1, p2):
    n = p1 * p2
    phi = (p1 - 1) * (p2 - 1)
    e = 0
    for i in range(2, phi):
        if math.gcd(i, phi) == 1:
            e = i
            break
    d = 0
    for i in range(phi):
        m = 1+(i*phi)
        if m % e == 0:
            d = int(m / e)
            break
    return [e, n], [d, n]

def get_prime_number():
    while True:
        number = random.randint(100, 1000)
        if isPrime(number, 6) is True: return number

def power(x, y, p):
    res = 1
    x = x % p
    while (y > 0):
        if (y & 1):
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res

def miillerTest(d, n):
    a = 2 + random.randint(1, n - 4)
    x = power(a, d, n)
    if (x == 1 or x == n - 1):
        return True
    while (d != n - 1):
        x = (x * x) % n
        d *= 2
        if (x == 1):
            return False
        if (x == n - 1):
            return True
    return False

def isPrime(n, k):
    if (n <= 1 or n == 4):
        return False
    if (n <= 3):
        return True
    d = n - 1
    while (d % 2 == 0):
        d //= 2

    for i in range(k):
        if (miillerTest(d, n) == False):
            return False
    return True

def encrypt(message, public_key):
    encrypt_message = []
    for m in message:
        encrypt_message.append(pow(ord(m), public_key[0]) % public_key[1])
    return encrypt_message

def decrypt(message, private_key):
    decrypt_message = ''
    for m in message:
        decrypt_message += chr(pow(m, private_key[0]) % private_key[1])
    return decrypt_message

message = input('Боб хочет передать сообщение: ')

public_key, private_key = RSA(get_prime_number(), get_prime_number())

print('\nОткрытый показтель степени e')
print('Секретный показатель Алисы: d')
print('Результат произведения простых чисел p1 и p2: n')

print('\nОткрытый ключ Алисы [e, n]:', public_key, 'для того, чтобы Боб запер им свое сообщение')
print('Закрытый ключ Алисы [d, n]:', private_key, 'для расшифровки "запертого" сообщения Боба')

encrypted = encrypt(message, public_key)
print('\nЗашифрованное сообщение Боба: ', encrypted)
decrypted = decrypt(encrypted, private_key)
print('Дешифрированное сообщение Боба: ', decrypted)