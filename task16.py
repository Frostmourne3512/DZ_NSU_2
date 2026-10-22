a = input()
if len(a) == 4 and len(a) == len(set(a)) and int(a) not in range(1900,2051):
    print('OK')
else:
    print('ERROR')