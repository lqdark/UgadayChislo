# -*- coding: cp1251 -*-
from random import randint


#функция да или нет
def yes_or_no():
    try:
        answer = input(str("Подтвердите или откажитесь - yes/no:"))
        if answer == 'yes' or answer == 'yes':
           return answer
        else:
           print('Ошибка ввода подтверждения.')
           return yes_or_no()  
    except ValueError:
        print('Ошибка ввода числа')
        return yes_or_no()    

#функция ввода числа
def input_number():
    try:
        number = int(input("Введите положительное целое число:"))
        if number > 0 and number != 0:
           return number
        else:
           print('Ошибка ввода числа')
           return input_number()  
    except ValueError:
        print('Ошибка ввода числа')
        return input_number()    


print('=====================================')
print('======= Игра. Угадай число. =========')
print('=====================================')
diapason = 100
try_count = 10
print(f'Диапазон от 1 до {diapason}. Количество попыток: {try_count}')
print('=====================================')
print('=====================================')

print('Хотите поменять параметры?')
if yes_or_no() == 'yes':
    print('=====================================')
    print('Введите число диапазона.')
    diapason = input_number()
    print('=====================================')
    print('Введите число попыток.')
    try_count = input_number()
    print('=====================================')
    print('=====================================')
    print(f'Текущие настройки игры: Диапазон от 1 до {diapason}. Количество попыток: {try_count}')
    


#генерируем случайное число в диапазоне
secret_number = randint(1,diapason)

try_count_g = 0
while True:
    user_number = input_number()
    try_count_g += 1
    try_count -= 1

    if user_number > secret_number:
        print(f'Загаданное число меньше. Попыток осталось: {try_count}' )
    elif user_number < secret_number:
        print(f'Загаданное число больше. Попыток осталось: {try_count}')
    elif user_number == secret_number:
        print(f'Бинго!. Было загадано: {secret_number}. Попыток потрачено: {try_count_g}')
        break
    
    #учитываем кол-во попыток
    if try_count == 0:
        print('Вы проиграли, попытки закончились.')
    

    
        

#result = math.factorial(int(number))
#print("Факториал числа", number, "равен", result)



