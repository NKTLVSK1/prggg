#Задача А
for i in range(1, (x := int(input())) + 1):
    for j in range(1, x + 1):
        if j < x:
            print(i * j, end=' ')
        else:
            print(i * j)     


#Задача B
for i in range(1, (x := int(input())) + 1):
    for j in range(1, x + 1):
        print(f'{j} * {i} = {i * j}')


#Задача C
for z in range(1, x := int(input()) + 1):
    if z in (sum(range(i)) for i in range(x)):
        print(z)
    else:
        print(z, end=' ')


#Задача D
summ = 0
for _ in range(int(input())):
    summ += sum(map(int, list(input())))
print(summ)


#Задача E
counter, temp = 0, 0
for _ in range(int(input())):
    while (x := input()) != 'ВСЁ':
        if x == 'зайка':
            temp += 1
    if temp:
        counter += 1
        temp = 0
print(counter)


#Задача F
n, a = int(input()), int(input())
for _ in range(n - 1):
    b = int(input())
    while b:
        a, b = b, a % b
print(a)


#Задача G
for i in range(int(input())):
    for j in range(3 + i, 0, -1):
        print(f'До старта {j} секунд(ы)')
    print(f'Старт {i + 1}!!!')


#Задача H
name, summ = '', 0
for _ in range(int(input())):
    temp_name, temp_summ = input(), sum(map(int, input()))
    if temp_summ >= summ:
        name, summ = temp_name, temp_summ
print(name)


#Задача I
number = ''
for _ in range(int(input())):
    number += max(input())
print(number)


#Задача J
for i in range(1, (n := int(input())) - 1):
    if i == 1:
        print('А Б В')
    for j in range(1, n - i):
        print(f'{i} {j} {n - i - j}')


#Задача K
counter = 0
for i in range(int(input())):
    j = 2
    if (n := int(input())) > 1:
        counter += 1
        if n == 2:
            counter += 1
        while n % j:
            if j > n ** 0.5:
                break
            j += 1
        else:
            counter -= 1
print(counter)


#Задача L
n, k = int(input()), int(input())
width = len(str(n * k))
for i in range(1, n + 1):
    for j in range(k * (i - 1) + 1, k * i + 1):
        if j == k * i:
            print(str(j).rjust(width, ' '))
        else:
            print(str(j).rjust(width, ' '), end=' ')


#Задача M
n, k = int(input()), int(input())
width = len(str(n * k))
for i in range(1, n + 1):
    for j in range(i, i + n * (k - 1) + 1, n):
        if j == i + n * (k - 1):
            print(str(j).rjust(width, ' '))
        else:
            print(str(j).rjust(width, ' '), end=' ')


#Задача N
red = int(input())
green = int(input())
blue = int(input())
print(red + blue + 1)


#Задача O
hours = int(input())
minutes = int(input())
delivery_time = int(input())
new_minutes = str((minutes + delivery_time) % 60)
new_hours = str((hours + (minutes + delivery_time) // 60) % 24)
print(f'{new_hours.rjust(2, "0")}:{new_minutes.rjust(2, "0")}')


#Задача P
stock = int(input())
market = int(input())
speed = int(input())
time = abs(market - stock) / speed
print(f'{time:.2f}')


#Задача Q
earnings = int(input())
last = int(input(), 2)
print(earnings + last)


#Задача R
cost = int(input(), 2)
bill = int(input())
print(bill - cost)


#Задача S
item, price, weight, money = input(), int(input()), int(input()), int(input())
headings = ['Товар:', 'Цена:', 'Итого:', 'Внесено:', 'Сдача:']
values = [item, f'{weight}кг * {price}руб/кг', f'{weight * price}руб', f'{money}руб', f'{money - weight * price}руб']
print('Чек'.center(35, '='))
for i in range(len(headings)):
    print(f"{headings[i] : <10}{values[i] : >25}")
print('=' * 35)


#Задача T
weight, price, price_1, price_2 = int(input()), int(input()), int(input()), int(input())
weight_1 = int((price - price_2) * weight / (price_1 - price_2))
weight_2 = weight - weight_1
print(weight_1, weight_2)