# -*- coding: cp1251 -*-
from random import randint


#������� �� ��� ���
def yes_or_no():
    try:
        answer = input(str("����������� ��� ���������� - yes/no:"))
        if answer == 'yes' or answer == 'yes':
           return answer
        else:
           print('������ ����� �������������.')
           return yes_or_no()  
    except ValueError:
        print('������ ����� �����')
        return yes_or_no()    

#������� ����� �����
def input_number():
    try:
        number = int(input("������� ������������� ����� �����:"))
        if number > 0 and number != 0:
           return number
        else:
           print('������ ����� �����')
           return input_number()  
    except ValueError:
        print('������ ����� �����')
        return input_number()    


print('=====================================')
print('======= ����. ������ �����. =========')
print('=====================================')
diapason = 100
try_count = 10
print(f'�������� �� 1 �� {diapason}. ���������� �������: {try_count}')
print('=====================================')
print('=====================================')

print('������ �������� ���������?')
if yes_or_no() == 'yes':
    print('=====================================')
    print('������� ����� ���������.')
    diapason = input_number()
    print('=====================================')
    print('������� ����� �������.')
    try_count = input_number()
    print('=====================================')
    print('=====================================')
    print(f'������� ��������� ����: �������� �� 1 �� {diapason}. ���������� �������: {try_count}')
    


#���������� ��������� ����� � ���������
secret_number = randint(1,diapason)

try_count_g = 0
while True:
    user_number = input_number()
    try_count_g += 1
    try_count -= 1

    if user_number > secret_number:
        print(f'���������� ����� ������. ������� ��������: {try_count}' )
    elif user_number < secret_number:
        print(f'���������� ����� ������. ������� ��������: {try_count}')
    elif user_number == secret_number:
        print(f'�����!. ���� ��������: {secret_number}. ������� ���������: {try_count_g}')
        break
    
    #��������� ���-�� �������
    if try_count == 0:
        print('�� ���������, ������� �����������.')
    

    
        

#result = math.factorial(int(number))
#print("��������� �����", number, "�����", result)



