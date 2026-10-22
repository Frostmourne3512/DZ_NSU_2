print('Вы поедете на бал?')
a = input().upper()
b = 'нет'.upper()
c = 'да'.upper()
if a == b or a == c:
    print('Неверно')
else:
    print('Верно')