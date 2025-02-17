#Задача A
def print_hello(name):
    print(f'Hello, {name}!')

#Задача B
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

#Задача C
def number_length(number):
    return len(str(abs(number)))

#Задача D
def month(number, language):
    MONTH = {
        'en': [
            'January', 'February', 'March',
            'April', 'May', 'June',
            'July', 'August', 'September',
            'October', 'November', 'December'
        ],
        'ru': [
            'Январь', 'Февраль', 'Март',
            'Апрель', 'Май', 'Июнь',
            'Июль', 'Август', 'Сентябрь',
            'Октябрь', 'Ноябрь', 'Декабрь'
        ]
    }
    return MONTH[language][number - 1]

#Задача E
def split_numbers(line):
    return tuple(map(int, line.split()))

#Задача F
lst = []


def modern_print(string):
    print(string) if string not in lst else None
    lst.append(string)

#Задача G
def can_eat(horse, shape):
    return abs(horse[0] - shape[0]) + abs(horse[1] - shape[1]) == 3

#Задача H
def is_palindrome(n):
    return str(n) == str(n)[::-1] if isinstance(n, int) else n == n[::-1]

#Задача I
def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
            return False
    return n != 1

#Задача J
def merge(a, b):
    c = list(a) + list(b)
    n = len(c)
    for i in range(n):
        for j in range(0, n - i - 1):
            if c[j] > c[j + 1]:
                c[j], c[j + 1] = c[j + 1], c[j]
    return tuple(c)

