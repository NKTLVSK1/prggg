#Задача А
print("Привет, Яндекс!")    


#Задача B
print("Как Вас зовут?")
print("Привет,",  input())


#Задача C
print((input() + '\n') * 3)


#Задача D
print(int(int(input()) - 2.5 * 38))


#Задача E
price = int(input())
weight = int(input())
money = int(input())
print(money - price * weight)


#Задача F
item = input()
price = int(input())
weight = int(input())
money = int(input())
print('Чек', f'{item} - {weight}кг - {price}руб/кг', sep='\n')
print(f'Итого: {int(price * weight)}руб')
print(f'Внесено: {money}руб')
print(f'Сдача: {int(money - price * weight)}руб')


#Задача G
print(('Купи слона!' + '\n') * int(input()))


#Задача H
number = int(input())
punish = input()
print((f'Я больше никогда не буду писать "{punish}"!\n') * number)


#Задача I
print(int(input()) * int(input()) // 2)


#Задача J
name = input()
locker = input()
print(f'Группа №{locker[0]}.')
print(f'{locker[2]}. {name}.')
print(f'Шкафчик: {locker}.')
print(f'Кроватка: {locker[1]}.')


#Задача K
number = input()
print(f'{number[1]}{number[0]}{number[3]}{number[2]}')


#Задача L
num1 = list(map(int, input().rjust(3, '0')))
num2 = list(map(int, input().rjust(3, '0')))
num_0 = str((num1[0] + num2[0]) % 10)
num_1 = str((num1[1] + num2[1]) % 10)
num_2 = str((num1[2] + num2[2]) % 10)
print((num_0 + num_1 + num_2).lstrip('0'))


#Задача M
children = int(input())
candies = int(input())
print(candies // children)
print(candies % children)


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