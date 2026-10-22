a = int(input())
if a > 29:
    b = a // 29
    a = a - b * 29
else:
    b = 0
if b > 17:
    c = b // 17
    b = b - c * 17
else:
    c = 0
if b == 0 and c == 0:
    print(f'Количество кнатов {a}', sep='\n')
if b == 0 and c != 0:
    print(f'Количество галлеонов {c}',f'Количество кнатов {a}', sep='\n')
if c == 0 and b != 0:
    print(f'Количество сиклей {b}', f'Количество кнатов {a}', sep='\n')
if a != 0 and b != 0 and c != 0:
    print(f'Количество галлеонов {c}', f'Количество сиклей {b}', f'Количество кнатов {a}',sep='\n')