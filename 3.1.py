#Задача А
for _ in range(int(input())):
    if (word := input())[0] not in 'абв':
        print('NO')
        break
else:
    print('YES')      


#Задача B
for i in input():
    print(i)


#Задача C
length = int(input())
for _ in range(int(input())):
    line = input()
    print(line[:length - 3].ljust(length, ".") if len(line) > length else line)


#Задача D
while (n := input()):
    if not n.endswith('@@@'):
        if n.startswith('##'):
            print(n[2:])
        else:
            print(n)


#Задача E
print('YES' if (line := input()) == line[::-1] else 'NO')


#Задача F
counter = 0
for _ in range(int(input())):
    counter += input().count("зайка")
print(counter)


#Задача G
print(sum(map(int, input().split())))


#Задача H
for _ in range(int(input())):
    if "зайка" in (place := input()):
        print(place.index("зайка") + 1)
    else:
        print("Заек нет =(")


#Задача I
while (n := input()):
    if not n.startswith('#'):
        print(n[:(n.index('#') if '#' in n else len(n))])


#Задача J
data = []
while (n := input()) != 'ФИНИШ':
    data.extend(n.lower().split())
max_count, data = 0, ''.join(data)
for symbol in set(data):
    max_count = max(max_count, data.count(symbol))
print(min([i for i in set(data) if data.count(i) == max_count]))


#Задача K
headings = []
for _ in range(int(input())):
    headings.append(input())
word = input()
for heading in headings:
    if word.lower() in heading.lower():
        print(heading)


#Задача L
order = ('Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая')
for i in range(int(input())):
    print(order[i % len(order)])


#Задача M
data = []
for _ in range(int(input())):
    data.append(int(input()))
number = int(input())
for i in data:
    print(i ** number)


#Задача N
data = list(map(int, input().split()))
number = int(input())
for i in data:
    print(i ** number, end=' ')


#Задача O
numbers = list(map(int, input().split()))
a = numbers[0]
while len(numbers) > 1:
    b = numbers[1]
    while b:
        a, b = b, a % b
    numbers.pop(1)
print(a)

#Задача P
length, line = int(input()), []
for _ in range(int(input())):
    line.append(input())
for i in line:
    if length > 3:
        print(i[:length - 3] + "..." if len(i) >= length - 3 else (i + "..." if length == 4 else i))
        length -= len(i)


#Задача Q
line = ''.join(input().lower().split())
print('YES' if line == line[::-1] else 'NO')


#Задача R
line = input()
temp_line, repeat = line[0], 1
for i in line[1:]:
    if i == temp_line:
        repeat += 1
    else:
        print(temp_line, repeat)
        temp_line, repeat = i, 1
print(temp_line, repeat)


#Задача S
data = list(input().split())
result = [int(data[0])]
for i in data[1:]:
    if i.isdigit():
        result.append(int(i))
    else:
        a = result.pop()
        exec("result[-1] " + i + "= a")
print(result[0])


#Задача T
def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1


data = list(input().split())
result = [int(data[0])]
for i in data[1:]:
    if i.isdigit():
        result.append(int(i))
    elif i == "/":
        a = result.pop()
        result[-1] //= a
    elif i == "~":
        result[-1] = -result[-1]
    elif i == "#":
        result.append(result[-1])
    elif i == "!":
        result[-1] = factorial(result[-1])
    elif i == "@":
        result.append(result.pop(-3))
    else:
        a = result.pop()
        exec("result[-1] " + i + "= a")
print(result[0])