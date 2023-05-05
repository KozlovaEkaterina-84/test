# Задача 1
a = 5
b = a * 4
c = a * a
import math
d = 2
e = math.sqrt(d)
f = a * e
print(b, c, f)
# Задача 2
a = 25
b = 60
c = 36
disc = b * b - 4 * a * c
import math
root = math.sqrt(disc)
x_1 = (-b + root) / (2 * a)
x_2 = (-b - root) / (2 * a)
print(x_1, x_2)
# Задача 3
string1 = 'Первый вариант 844'
string2 = 'Второй вариант 744'
print(string2[:2]+string1[2:], string1[:2]+string2[2:])
# Задача 4
string1 = r'C:\python\name.txt'
print(string1[3:9], string1[:1], string1[-8:-4])
# Задача 5
a, b = 3, 4
print("{}+{}={}".format(a, b, a+b))
print("{}*{}={}".format(a, b, a*b))
# Задача 6
string = 'впс еспдрна впинл ьднлoо'
print(string[0:-1:2])
# Задача 7
first_string = 'wtf'
second_string = 'brick quz jmpy veldt whangs fox'
result = second_string.find(first_string[0]), second_string.find(first_string[1]), second_string.find(first_string[2])
print(second_string[min(result):max(result)+1])