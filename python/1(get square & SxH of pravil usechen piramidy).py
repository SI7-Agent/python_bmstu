print('Найти объём и полную площадь поверхности правильной четырехугольной усеченной пирамиды.')
a = float(input('Введите длину нижнего основания: '))
# ввод длины нижнего ребра
b = float(input('Введите длину верхнего основания: '))
# ввод длины верхнего ребра
height = float(input('Введите длину высоты: '))
# ввод длины высоты
from math import sqrt
# загрузка модуля извлечения корня
s1 = a**2
# вычисление площади нижнего основания
s2 = b**2
# вычисление площади верхнего основания
v = height/3*(s1+s2+sqrt(s1*s2))
# вычисление объёма
k = b/a
# вычисление коэффициента подобия оснований
height1 = k*height
#вычисление восстановленной высоты
a1 = a/2
# вычисление оставшегося катета
l1 = sqrt(height1**2+a1**2)
# вычисление востановленной апофемы
l = float(l1)/k
#вычисление апофемы
s3 = 4*l*(a+b)/2
# вычисление боковой поверхности пирамиды
print('*********************************************')
print('Полная площадь пирамиды:', ' ', round(s1+s2+s3, 4), sep='')
print('*********************************************')
print('Объём пирамиды:', ' ', round(v, 4), sep='')
print('*********************************************')