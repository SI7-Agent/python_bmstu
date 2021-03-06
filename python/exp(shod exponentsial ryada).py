eps = float(input('Введите число eps: '))
step = int(input('Введите шаг значений: '))
x = int(input('Введите кол-во итераций: '))
q = float(input('Под знаком ln: '))
a = float(input('Число а: '))

from math import *

i = 0
n = 0
t = a**n * log(q)**n/factorial(n)
sum = t

print('\t', '\u250c', '\u2500' * 15, '\u252c', '\u2500' * 15, '\u252c', '\u2500' * 31, '\u252c', '\u2500' * 31,
      '\u2510', sep = '')
print('\t', '{:s}{:^13s}{:s}{:^13s}{:s}{:^26s}{:s}{:^27s}{:s}' \
      .format('\u2502', 'N', '\u2502', 'x текущее', '\u2502', 'текущий член ряда', '\u2502',
              'текущее значение суммы', '\u2502', ), sep = '')

while abs(t) > eps:
    if i%step == 0:
        print('\t', '\u251c', '\u2500' * 15, '\u253c', '\u2500' * 15,\
              '\u253c', '\u2500' * 31, '\u253c', '\u2500' * 31, '\u2524', sep = '')
        print('\t', '{:s}{:^13d}{:s}{:^13.2f}{:s}{:^26f}{:s}{:^27f}{:s}'.format('\u2502', i + 1,\
              '\u2502', n, '\u2502', t, '\u2502', sum, '\u2502'), '\n', sep = '', end = '')
    n += 1
    w = a * log(q) / (factorial(n) / factorial(n - 1))
    t *= w
    sum += t
    i += 1
    if n > x or i > x:
        break

if abs(t) <= eps:
    print('\t', '\u251c', '\u2500' * 15, '\u253c', '\u2500' * 15, '\u253c', '\u2500' * 31, '\u253c', '\u2500' * 31,
        '\u2524', sep = '')
    print('\t', '{:s}{:^13d}{:s}{:^13.2f}{:s}{:^26f}{:s}{:^27f}{:s}' \
          .format('\u2502', i + 1, '\u2502', n, '\u2502', t, '\u2502', sum, '\u2502'), '\n', sep='', end='')
    print('\t', '\u2514', '\u2500' * 15, '\u2534', '\u2500' * 15, '\u2534', \
          '\u2500' * 31, '\u2534', '\u2500' * 31, '\u2518', sep = '')
    print('Ряд сошелся на ', i+1, '-ом', ' элементе', sep = '')
    print()
    print('Сумма элементов: ', '{:.7f}'.format(sum))

else:

    print('\t', '\u2514', '\u2500' * 15, '\u2534', '\u2500' * 15, '\u2534', \
          '\u2500' * 31, '\u2534', '\u2500' * 31, '\u2518', sep='')
    print('Ряд не сходится за ', x, ' итераций')
