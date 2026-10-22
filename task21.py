a = input()
b = input()
x1 = int(ord(a[0]) - ord('a')) + 1
x2 = int(ord(b[0]) - ord('a')) + 1
if x1 <= 8 and x2 <= 8 and int(a[1]) <= 8 and int(b[1]) <= 8:
    if abs(x2 - x1) == 2 and abs(int(b[1]) - int(a[1])) == 1 or abs(x2 - x1) == 1 and abs(int(b[1]) - int(a[1])) == 2:
        print('Correct')
else:
    print('Incorrect')