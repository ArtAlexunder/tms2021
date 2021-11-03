# Expression ax^2 + bx + c = 0

print('Expression ax^2 + bx + c = 0')
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

D = b ** 2 - 4 * a * c
if D > 0:
    x1 = (-b + (D ** 0.5)) / (2 * a)
    x2 = (-b - (D ** 0.5)) / (2 * a)
    print(f'Два действительных корня. x1 = {x1}, x2 = {x2}')
elif D == 0:
    x = -b / (2 * a)
    print(f'Один действительный корень. x = {x}')
elif D < 0:
    print('Нет действительных корней')
else:
    print('Error')
