N = 100
lst=list(range(N))
print(lst)
print(lst.__sizeof__()) #840
it=iter(lst)
print(next(it).__sizeof__()) #24 constanta
print(it.__sizeof__()) #32 constanta
g=(i for i in range(100000000000000000000000000000000000))
print(g) #<generator object <genexpr> at 0x0000019BE3E04380>
print(g.__sizeof__()) #184 constanta

print(dir(g)) #имеет методы '__iter__',  '__next__
print(dir(it)) #            '__iter__',  '__next__
print(dir(dir(lst))) #       '__iter__',

#$###################
g=(i for i in range(10000000000)) #время всё равно затрачивает

print(sum(g))
g=(i for i in range(100))
print(max(g))
g=(i for i in range(100))
print(len(g)) #TypeError: object of type 'generator' has no len()
############ 9.1 Выражения-генераторы
# Подвиг 1. Запишите выражение для генератора, который бы возвращал целые числа от 2 до 10 000 с шагом 1
# (то есть, 2, 3, 4, ..., 10 000). Присвойте этот генератор переменной gen.


gen = (int(i) for i in range(2, 10001))
################################################################
# Подвиг 2. На вход программы поступают два целых числа a и b (a < b), записанные в одну строчку через пробел.
# На их основе запишите генератор для формирования квадратов чисел в диапазоне [a; b].# Преобразуйте этот генератор
# в кортеж чисел (без использования операторов циклов) и присвойте эту коллекцию переменной tp.
#a, b = map(int, input().split())
a, b =2,5
tp=tuple(pow(i,2) for i in range(a,b+1))
print(tp)

#Подвиг 3. На вход программы поступают два целых числа a и b (a < b), записанные в одну строчку через пробел.
# Определите генератор, который бы выдавал модули целых чисел из диапазона [a; b]. В цикле выведите первые пять
# значений этого генератора. Каждое значение с новой строки. (Гарантируется, что пять значений имеются).
a, b = map(int, input().split())
abs_gen = (abs(i) for i in range(a, b + 1))

for i in range(5):
    print(next(abs_gen))

[print(next(abs_gen)) for _ in range(5)]
print(*[next(abs_gen) for i in range(5)], sep='\n')
######################
[print(abs(v)) for i, v in enumerate(range(a, b + 1)) if i < 5]

################# Подвиг 6. Вводится целое положительное число a. Необходимо определить генератор, который бы
# возвращал модули чисел в диапазоне [-a; a], а затем еще один, который бы вычислял кубы чисел
# (возведение в степень 3), возвращаемых первым генератором.Вывести в одну строчку через пробел первые четыре значения.
# (Полагается, что генератор выдает, как минимум четыре значения).

a = 3
gen_exp = (abs(i) for i in range(-a, a+1))
gen_cube = (pow(i, 3) for i in gen_exp)
print(*[next(gen_cube) for _ in range(4)], sep=' ') #27 8 1 0

### ##################
a = 3
def dec_gen(func):
    def wrapper(*args, **kwargs):
        gen_cube = (pow(i, 3) for i in func(*args, **kwargs))
        return gen_cube
    return wrapper

@dec_gen
def gen_exp(a):
    gen_m = (abs(i) for i in range(-a, a + 1))
    return gen_m

# var 1
# print(*gen_exp(a)) #27 8 1 0 1 8 27

cub = gen_exp(a)
print(*[next(cub) for _ in range(4)], sep=' ')  # 27 8 1 0
#
### ##############  ####
a = 3
gen_num = (pow(j, 3) for i in range(-a, a) for j in [abs(i)])

for i, v in enumerate(gen_num):
    print(v,end=' ')
    if i == 3:
        break

for _ in range(4):
    print(*[next(gen_num)],end=' ')

################################
#Подвиг 7. Используя символы малых букв латинского алфавита (строка ascii_lowercase):from string
# import ascii_lowercase запишите генератор, который бы возвращал все сочетания из двух букв латинского
# алфавита. Выведите первые 50 сочетаний на экран в строку через пробел.Например, первые семь начальных
# сочетаний имеют вид: aa ab ac ad ae af ag
from string import ascii_lowercase as al
gen_alphabet = (i + j for i in al for j in al)
print(*[next(gen_alphabet) for _ in range(50)])

[print(next(gen_alphabet), end=' ') for _ in range(50)]
#генератор списков отрабатывает независимо от того присваивается ли его результат переменной или нет. соответственно
# в данном случае для указанного количества итераций в генераторе списков отрабатывает функция принт. ради интереса
# если присвоить значение этого генератора переменной (к примеру - a = [данный генератор]) результат выполнения
# кода будет точно такой же - распечатаются первые 50 пар букв) только если после этого вызвать print(a) то выведет
# сперва так же 50 пар букв, а затем список из 50 значений None т.к. функция принт в генераторе сперва
# выполнится(выведет на экран все значения) и после каждого вывода будет возвращать в генератор None. проще говоря
# при такой записи как в данном решении на экран выводятся не значения самого генератора списков(напомню -
# они все равны None), а результат выполнения функции print() внутри генератора на каждой итерации его работы

### ##################
[print(v, end=' ') for i, v in enumerate(i + j for i in ascii_lowercase for j in ascii_lowercase) if i < 50]


### ##################
lst = list(i + p for i in ascii_lowercase for p in ascii_lowercase)
print(lst[:50])
print(len(lst))  # 676
#только используя данное решение, производится 707 операций, а при использовании выражения-генератора - 207.
# нормальная такая разница, да?) дело в том, что через list comprehension сперва полностью формируется этот список,
# а затем с него берется срез. с этого имеем следующее:  1) куча ненужных вычислений 2) куча засраной памяти т.к.
# полностью формируется никому не нужный список абсолютно всех сочетаний букв. если бы по условию задания требовалось
# генерировать не пары букв, а сочетания по 5 букв и так же вывести первые 50, это решение с треском провалилось бы.

###########
from string import ascii_lowercase
import itertools

letters = itertools.product(ascii_lowercase, repeat=2) #Возвращаемое значение: итератор
#Чтобы вычислить декартово произведение последовательности с самим собой, укажите количество повторений в
# необязательном ключевом аргументе repeat. Например выражение product(A, repeat=4) означает то же самое, что и
# product(A, A, A, A).
#repeat=2 как вложенный цикл for i in ...for j in ...)
for _ in range(50):
    print(''.join(next(letters)), end=' ')


#Подвиг 8. Имеется список из названий городов:cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
# Необходимо записать генератор, который бы используя этот список, выдавал 1 000 000 наименований городов по циклу.
# То есть, дойдя до конца списка, возвращался в начало и повторял перебор. И так, для выдачи миллиона названий.
# Вывести на экран первые 20 наименований городов с помощью генератора в одну строчку через пробел.
cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
n = 1000000
gen_cities = (i for _ in range(n) for i in cities) #в генераторе 6 млн сидит
#gen_cities = (i for i in cities*n)
print(*(next(gen_cities) for _ in range(20)), end=' ')

############
cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
n = 1000000
gen_cities = (cities[i % len(cities)] for i in range(n))
#Если при вычислении остатка от деления делимое меньше делителя, то частное равняется делимому: 5 % 6 = 5
# А если делимое и делитель равны, то частное 0, ну а потом считается стандартный остаток от деления.
# Так можно перебирать индексы хоть до бесконечности.
print(*(next(gen_cities) for i in range(20)))

#####################
from itertools import cycle
gen = cycle(cities)
[print(next(gen), end = ' ') for _ in range(20)]

##########
from itertools import chain, repeat
c, r = divmod(1_000_000, len(cities))
gen = chain(repeat(cities, c), (lst[i] for i in range(r)))
lst = [next(gen) for _ in range(n)]

### Подвиг 9. Имеется график функции f(x) = 0.5x^2 - 2. Необходимо записать генератор, который бы выдавал значения
# этой функции для аргумента x в диапазоне [a; b] с шагом 0.01. Величины a, b вводятся с клавиатуры в одну строчку
# через пробел как целые числа (a< b). Вывести на экран первые 20 значений функции с точностью до сотых, взятых из
# генератора.P.S. Значения функции вычислять командой:  f(x) = 0.5 * pow(x, 2) - 2.0
a, b = map(int, input().split())
gen_func = (0.5 * pow(i / 100, 2) - 2.0 for i in range(a*100, (b+1) * 100))

#print(*(round(next(gen_func),2) for _ in range(20)) , end=' ')
for i in range(20):
    print(round(next(gen_func),2),end=' ')

########################################################################
gen_func = (round(0.5 * pow(i / 100, 2) - 2.0,2) for i in range(a*100, (b+1) * 100))
print(*(next(gen_func) for _ in range(20)) , end=' ')
################################################################
import numpy
a, b = map(int, input().split())
def f(x):
    return 0.5 * pow(x, 2) - 2.0
gen = (f(x) for x in numpy.arange(a, b + 1, 0.01))
for _ in range(20):
    print(round(next(gen), 2), end=' ')


##################
# Подвиг 1. Вводится натуральное число N. Необходимо определить функцию-генератор с именем get_sum,
# которая бы возвращала текущую сумму чисел последовательности длины N в диапазоне целых чисел [1; N].
# Например:# # - для первого числа 1 сумма равна 1;
# - для второго числа 2 сумма равна 1+2 = 3
# ....# - для N-го числа сумма равна 1+2+...+(N-1)+N
def get_sum(N):
    t = 0
    g = (i for i in range(1, N + 1))
    for i in g:
        t += i
        yield t

N = 5
# print(*get_sum())
print(*tuple(get_sum(N)))
######################
def get_sum(N):
    t = 0
    g = (i for i in range(1, N + 1))
    for i in g:
        yield (t := t + i)
######################
def get_sum(n):
    for i in range(1, n + 1):
        yield i * (i + 1) // 2 #формула подходит только для шага 1 =).
######################
def get_sum(N):
    for i in range(1,N+1):
        yield sum(range(i+1))

#################
#Подвиг 2. Мы с вами в заданиях несколько раз генерировали последовательность чисел Фибоначчи, которая
# строится по правилу: каждое последующее число равно сумме двух предыдущих. Для разнообразия давайте
# будем генерировать каждое последующее как сумму трех предыдущих чисел. При этом первые три числа равны
# 1 и имеем такую последовательность:1, 1, 1, 3, 5, 9, 17, 31, 57, ...Не знаю, есть ли у нее название,
# поэтому, в рамках уроков, я скромно назову ее последовательностью Балакирева. Итак, на вход программы
# поступает натуральное число N (N > 5) и необходимо определить функцию-генератор, которая бы возвращала
# N первых чисел последовательности Балакирева (включая первые три единицы).

N = 7
def get_balakirev():
    lst = [1, 1, 1]
    print(*lst, end=' ')
    for i in range(N - len(lst)):
        total = sum(lst[-3:])
        lst.append(total)
        yield total

print(*get_balakirev())

#################
def get_balakirev():
    # a = b = c = 1
    a,b,c = 1,1,1
    for _ in range(N):
        yield a
        a, b, c = b, c, a+b+c


print(*get_balakirev())
#################
N = 7
def get_balakirev():
    a = b = c = 1
    while True:
        yield a
        a, b, c = b, c, a + b + c

b = get_balakirev()
for i in range(N):
    print(next(b), end=' ')
#- именно через бесконечный цикл. суть задания как раз в том чтобы создать функцию, которая будет
# бесконечно генерировать последовательность, и затем вызвать функцию столько раз, сколько нужно
# получить значений, а не передавать в генератор количество значений которое нужно получить. во всех
# решениях где N передается в функцию, теряется в принципе смысл елдить, оно там ничего не дает и проще
# было реализовать в рекурсии
################# рекурсиями
def gen(N):
    def seq(i):
        return seq(i - 1) + seq(i - 2) + seq(i - 3) if i > 3 else 1

    for i in range(1, N + 1):
        yield seq(i)
print(*gen(N))

#################
#Подвиг 3. Вводится натуральное число N (N > 8). Необходимо определить функцию-генератор, которая бы выдавала пароль
# длиной N символов из случайных букв, цифр и некоторых других знаков. Для получения последовательности допустимых
# символов для генерации паролей в программе импортированы две строки: ascii_lowercase, ascii_uppercase (см. листинг
# ниже), на основе которых формируется общий список:
# from string import ascii_lowercase Строчные буквы 'abcdefghijklmnopqrstuvwxyz',
# ascii_uppercase Прописные буквы 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
# Функция-генератор должна при каждом вызове возвращать новый пароль из случайно выбранных символов chars длиной N
# и делать это бесконечно, то есть, вызывать ее можно бесконечное число раз. Сгенерировать случайный индекс indx в
# диапазоне [a; b] для символа можно с помощью функции randint модуля random:import random
# random.seed(1)indx = random.randint(a, b)Сгенерируйте с помощью этой функции первые пять паролей и выведите их в
# столбик (каждый с новой строки).

import random
from string import ascii_lowercase, ascii_uppercase

chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
print(chars) #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!?@#$*
# установка зерна датчика случайных чисел (не менять)
random.seed(1) #Функция random.seed() в Python используется для инициализации случайных чисел. По умолчанию генератор
# случайных чисел использует текущее системное время. Если вы дважды используете одно и то же начальное значение,
# вы получите один и тот же результат, что означает случайное число дважды (с)
#достаточно запомнить какое-то своё любимое число, которое будет ключом в seed() и всегда можно получить свой
# какой-угодно сложный пароль.
# password ='pavel'
# random.seed('pavel')
#то псевдо рандом)) он всегда с чего то генерирует число по какому то алгоритму, и метод seed как раз задает
# отправную точку) поэтому и получается каждый раз одно и то же.
N = 10
def gen_pass():
    while True:
        w = ''
        for i in range(N):
            indx = random.randint(0,len(chars)-1) #randint – включает правую границу
            # randint(a, b) берёт числа из диапазона включительно [a, b].
            w += chars[indx]
            yield w

pas = gen_pass()
for _ in range(5):
    print(next(pas))
#################
# from random import  choice, seed #v2
import random
from string import ascii_lowercase, ascii_uppercase
random.seed(1)
# seed(1) v 2
chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
N = 10
def gen_pass():
    while True:
        yield ''.join(random.choice(chars) for _ in range(N)) #возвращает один случайный элемент из непустой последови

pas = gen_pass()
for _ in range(5):
    print(next(pas))
################################
    def gen_pass():
        for _ in range(N):
            yield random.choice(chars)

for _ in range(5):
    print(''.join(gen_pass())) #в join можно подать любую последовательность (включая генератор).
################################

#Подвиг 4. Вводится натуральное число N. Используя строки из латинских букв ascii_lowercase и ascii_uppercase:
# from string import ascii_lowercase, ascii_uppercase
# chars = ascii_lowercase + ascii_uppercase
# задайте функцию-генератор, которая бы возвращала случайно сформированные email-адреса с доменом mail.ru и
# длиной в N символов. Например, при N=6, получим адрес: SCrUZo@mail.ru
# Для формирования случайного индекса для строки chars используйте функцию randint модуля random:
# Функция-генератор должна возвращать бесконечное число таких адресов, то есть, генерировать постоянно.
# Выведите первые пять сгенерированных email и выведите их в столбик (каждый с новой строки).
from string import ascii_lowercase, ascii_uppercase
import random
chars = ascii_lowercase + ascii_uppercase
#print(chars) #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
random.seed(1)
N = 8
def gen_mail():
    while True:
        w = ''
        for i in range(N):
            indx = random.randint(0, len(chars) - 1)
            w += chars[indx]
        yield w + '@mail.ru'

g = gen_mail()
for _ in range(5):
    print(next(g))
#################
#Подвиг 5. Определите функцию-генератор, которая бы возвращала простые числа. (Простое число - это натуральное число,
# которое делится только на себя и на 1). Выведите с помощью этой функции первые 20 простых чисел (начиная с 2)
# в одну строчку через пробел.
################################
def gen_num():
    n = 1
    while True: #бесконечный цикл можно открыть с помомшью конструкции while True:
        n += 1
        if all(n % i for i in range(2, int(n**0.5)+1)): #n ** 0.5 это квадратный корень, предельное число,
    # после которого можно прерывать цикл range(2, limit) выдает последовательность n % i - остатки от деления нацело
    # all - даст True только если интерпретирует все элементы как True, в данном случае, все ненулевые,
    # то есть, не делящиеся нацело  Если хоть одно число делится, результат будет False
            yield n

num = gen_num() # !!!Нужно сначала создать объект, присвоить ему значение генератора и итерироваться уже объекту,
# а не по самой функции.
print(next(gen_num())) # функция-генератор инициализируется 1 раз
print(next(gen_num())) # выдаёт каждый раз при вызове 2 Если так вызывать, то это каждый раз новый генератор
for i in range(20):
    print(next(num), end=' ') # функция-генератор инициализируется 20 (на каждой итерации)
    #видимо пока у нас нет ссылки на генератор, он удаляется, и при следующем вызове функции, создаётся новый с
    # двойкой по умолчанию, который отработав удаляется т.к. у нас же на него нет ссылки :).
################################
def gen_num():
    n = 2
    yield n
    while True:
        n += 1
        for i in range(2, n):
            if n % i == 0:
                break
        else: #если число на что-то поделилось нацело - срабатывает break и блок else пропускается, если же делителей
            # не нашлось - цикл завершится и else вернет число.
            yield n

num = gen_num()
for i in range(20):
    print(next(num), end=' ')
#################
def gen_num():
    n = 1
    while True:
        n += 1
        if not any(n % i == 0 for i in range(2, n)):
            yield n
#################
def gen_num():
    n = 1
    while True:
        n += 1
        if all(n % i for i in range(2, n)):
            yield n
#################
from sympy import prime

def gen_num():
    n = 1
    while True:
        yield prime(n) #sympy.prime(), n  здесь это просто номер простого числа,
        n += 1
#################
def is_prime(n): #Решил разбить задачу на две функции: функцию-предикат (определяет является ли число простым) и
    # функцию-генератор.
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def gen_num():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

#################
import re

def isprime(n):
    return re.compile(r'^1?$|^(11+)\1+$').match('1' * n) is None

print(*[x for x in range(100) if isprime(x)][:20])
#################
#################    9.3 Функция map
#Подвиг 1. На вход поступает список из вещественных чисел, записанных в строку через пробел. С помощью функции map
# преобразовать числа в строке в их вещественное представление и отобразить первые три числа. (Полагается, что
# минимум три вещественных числа имеются). Реализовать извлечение чисел через функцию next. Результат отобразить в
print(*[*map(float,input().split())][:3])
#################
m = map(float, input().split())
print(*(next(m) for _ in range(3)))
################
#Подвиг 2. На вход поступает строка из целых чисел, записанных через пробел. С помощью функции map преобразовать
# эту строку в список целых чисел, взятых по модулю. Сформируйте именно список lst из таких чисел. Отобразите его
# на экране в виде набора чисел, идущих через пробел.
lst = list( map( abs,  map(int, input().split())))
print(*lst)
#################
lst = list(map(lambda x: abs(int(x)), input().split()))
print(*lst)
#################
#Подвиг 3. Вводится таблица целых чисел. Используя функцию map и генератор списков, преобразуйте список строк lst_in
# (см. листинг) в двумерный список с именем lst2D, содержащий целые числа.
#################
import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst2D = [*map(lambda x: [*map(int, x.split())], lst_in)] #две map()
# lst2D = list(map(lambda x: [*map(int, x.split())], lst_in)) #две map()
lst2D = [[int(i) for i in x.split()] for x in lst_in] #два генератора
# lst2D = [*map(lambda x: [int(i) for i in x.split()], lst_in)] #генератор в map() и map в генераторе
# lst2D = [[*map(int, x.split())] for x in lst_in] # map()  в генераторе
# lst2D = list(list(map(int, i.split())) for i in lst_in) # map()  в генераторе
print(lst2D)
###############################
#Подвиг 4. На вход программы поступает строка в формате:ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N
# Необходимо с помощью функции map преобразовать ее в кортеж tp вида:
# tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N', 'значение_N'))
# s_lst = s.split()
# print(s_lst)  # ['house=дом', 'car=машина', 'men=человек', 'tree=дерево']
s_lst = ['house=дом', 'car=машина', 'men=человек', 'tree=дерево']
tp = tuple((i.split('=')[0], i.split('=')[1]) for i in s_lst)
print(tp)  #
#################
tp = tuple((j[0], j[1]) for i in s_lst for j in [i.split('=')])
#################
tp = tuple(map(lambda x: (x.split('=')[0], x.split('=')[1]), s_lst))
#################
tp = tuple(map(lambda x: tuple(x.split('=')), s_lst))
##################################
tp = tuple(map(tuple, [i.split('=') for i in s_lst]))
##################################
tp = tuple(map(tuple, (i.split('=') for i in s_lst)))
##################################
#Подвиг 5. (Для учебных целей). Вводится строка. Необходимо в ней заменить кириллические символы на соответствующие
# латинские обозначения (без учета регистра букв), а все остальные символы - на символ дефиса (-). Для этого в
# программе определен словарь (см. листинг). Используя его, запишите функцию map, которая бы выдавала
# преобразованные фрагменты для входной строки. На основе этой функции сформируйте строку, состоящую из
# преобразованных фрагментов (фрагменты в строке должны идти друг за другом без пробелов).
t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

s = 'Привет Питон'
string = ''.join(map(str, (t[i] if i in t else '-' for i in s.lower())))
print(string) #privet-piton
##################################
string = ''.join(t[i] if i in t else '-' for i in s.lower())
##################################
string = ''.join(map(lambda x: t.get(x, '-'),  s.lower()))
##################################
string = ''.join(map(lambda x: t.setdefault(x, '-'), s.lower()))
##################################
string = ''.join(map(lambda x: t[x] if x in t else '-',  s.lower()))
##################################
#Подвиг 6. Вводятся названия городов в одну строчку через пробел. Необходимо определить функцию map, которая бы
# возвращала названия городов только длиной более 5 символов. Вместо остальных названий - строку с дефисом ("-").
# Сформировать список из полученных значений и отобразить его на экране в одну строчку через пробел.
s = 'Москва Уфа Вологда Тула Владивосток Хабаровск'
string = ' '.join(map(lambda x: x if len(x) > 5 else '-', s.split()))
print(string)
##################################
def string_def(x):
    return x if len(x) > 5 else '-'

string = ' '.join(map(string_def, s.split()))
print(string)


##################################  9.4 Функция filter #######
#алгоритма проверки числа на простоту
def is_prime(n):
    if n <= 1:
        return False
    d = 2
    # while d * d <= n: #свойство p^2 = n. p = n^(1/2)
    while d < n:
        if n % d == 0 or n % 2 == 0:
            return False
        d += 1
    return True

num = filter(is_prime, (i for i in range(30)))
print(*num) #2 3 5 7 11 13 17 19 23 29
print(list(num)) #[]
##################################
#Подвиг 1. Вводятся названия городов в одну строчку через пробел. Необходимо определить функцию
# filter, которая бы возвращала только названия длиной более 5 символов. Извлеките первые
# три полученных значения с помощью функции next и отобразите их на экране в одну строчку
# через пробел.
s = 'Тула Ульяновск Хабаровск Владивосток Омск Уфа'
city = filter(lambda x: len(x) > 5, s.split())

for i in range(3):
    print(next(city),end=' ')
# [print(*city, end='') for _ in range(3)]
# print(*(next(city) for i in range(3)))
##################################
#Подвиг 2. Вводится список предметов в виде списка:название_1: вес_1название_N: вес_NС помощью функции map,
# необходимо сначала преобразовать этот список строк в кортеж, элементами которого также являются кортежи:
# (('название_1', 'вес_1'), ..., ('название_N', 'вес_N'))А, затем, отфильтровать (исключить) все предметы с
# весом менее 500, используя функцию filter. Вывести на экран список оставшихся предметов (только их названия)
# в одну строчку через пробел.
import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
def ress(n):
    # print(n)
    if int(n[1]) >= 500:
        return True
    else:
        return False
# print(lst_in)  # ['зонт=1000', 'палатка=10000', 'спички=22', 'котелок=543']
tp = tuple(map(lambda x: tuple(x.split('=')), lst_in))
# print(tp)  # (('зонт', '1000'), ('палатка', '10000'), ('спички', '22'), ('котелок', '543'))
res = list(filter(ress, (i for i in tp)))

print(*(i[0] for i in res), end=' ') #зонт палатка котелок
# for i in res:
#     print(i[0])
##################################
res = list(filter(lambda x:  int(x[1]) >= 500, (i for i in tp))) #filter фильтрует (отбирает) вложенные кортежи
# согласно условию, а не изменяет их. Вот вы и получили все вложенные кортежи прошедшие условие вашей фильтрации.
# Вы путаете механизмы действия функций map и filter
print(*(i[0] for i in res), end=' ')  # зонт палатка котелок
##################################
lst_in = list(map(str.strip, sys.stdin.readlines()))
tp = tuple(map(lambda x: tuple(x.split('=')), lst_in))
res = filter(lambda x: int(x[1]) >= 500, tp)
g = map(lambda x: x[0], res)
print(*g)
##################################
#Подвиг 3. Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только
# двузначные числа. Реализовать программу с использованием функции filter. Результат отобразить на экране
# в виде последовательности оставшихся чисел в одну строчку через пробел.
# n = ['8', '11', '0', '-23', '140', '1']
res = filter(lambda x: len(str(abs(int(x)))) == 2, n)
print(*res)
##################################
n = '8 11 0 -23 140 1'
res = filter(lambda x: 9 < (abs(int(x))) < 100, n.split())
print(*res)
##################################
res = filter(lambda x: len(x.strip('-'))==2, n.split())
##################################
res = filter(lambda x: len(x.replace('-','')) == 2, n.split())
##################################
#Подвиг 4. Саша и Галя коллекционируют монетки. Каждый из них решил записать номиналы монеток из своей
# коллекции. Получилось два списка. Эти списки поступают на вход программы в виде двух строк из целых чисел,
# записанных через пробел. Необходимо выделить значения, присутствующие в обоих списках и оставить среди них
# только четные. Результат вывести на экран в виде строки полученных чисел в порядке их возрастания через
# пробел.
l1 = '1 5 2 7 10 25 50 100'
l2 = '5 2 3 7 10 25 55'
lst = sorted(filter(lambda x: x in l2 and int(x) % 2 == 0, l1.split()), reverse=True)
print(*lst)
##################################
lst = filter(lambda x: int(x) % 2 == 0, sorted(set(l1.split()) & set(l2.split()),reverse=True))
print(*lst)
##################################
lst = filter(lambda x: not int(x)%2, set(l1.split()) & set(l2.split()))
##################################
#Подвиг 5. Вводится список email-адресов в одну строчку через пробел. Среди них нужно оставить только
# корректно записанные адреса. Будем полагать, что к таким относятся те, что используют латинские буквы,
# цифры и символ подчеркивания. А также в адресе должен быть символ "@", а после него символ точки "."
# (между ними, конечно же, могут быть и другие символы).Результат отобразить в виде строки email-адресов,
# записанных через пробел.
# Sample Input:abc@it.ru dfd3.ru@mail biba123@list.ru sc_lib@list.ru $fg9@fd.com
import string
symbols = string.ascii_lowercase+ string.digits+'_'+'@.'
s=input().lower()
# ad = filter(lambda x: x.isalnum(), s.split()) isalnum() не подходит, поскольку этот метод проускает кирилличные буквы
ad = filter(lambda x: '.' in x.split('@')[1] and all(i in symbols for i in x), s.split())
print(*ad)
##################################
ad = filter(lambda x: x.find('@') < x.find('.') and all(i in symbols for i in x), s.split())
##################################
#9.5 Функция zip
#Подвиг 1. Вводятся два списка целых чисел. Необходимо попарно перебрать их элементы и перемножить между собой. При
# реализации программы используйте функции zip и map. Выведите на экран первые три значения, используя функцию next.
# Значения выводятся в строчку через пробел.
lst_1 = '-7 8 11 -1 3'.split()
lst_2 = '1 2 3 4 5 6 7 8 9 10'.split()

lst_1=input().split()
lst_2=input().split()
result = map(lambda x: int(x[0]) * int(x[1]), zip(lst_1, lst_2))
for i in range(3):
    print(next(result), end=' ')

##################################
#Подвиг 2. Вводится неравномерная таблица целых чисел. С помощью функции zip выровнить эту таблицу, приведя ее к
# прямоугольному виду, отбросив выходящие элементы. Вывести результат на экран в виде такой же таблицы чисел.
import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
tr = zip(*lst_in)
res = zip(*tr)
for i in res:
    print(*i, sep='')

##################################
for i in zip(*zip(*lst_in)):
    print(*i, sep='')
##################################
#Подвиг 3. Вводится таблица целых чисел. Необходимо сначала эту таблицу представить
# двумерным списком чисел, а затем, с помощью функции zip выполнить транспонирование этой
# таблицы (то есть, строки заменить на соответствующие столбцы). Результат вывести на экран
# в виде таблицы чисел
lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ['1 2 3 4', '5 6 7 8', '9 8 7 6']
lst = list(map(int, i.split()) for i in lst_in)
for i in zip(*lst):
    print(*i)
##################################
#Подвиг 4. Вводится строка из слов, записанных через пробел. Необходимо на их основе
# составить прямоугольную таблицу из трех столбцов и N строк (число строк столько, сколько
# получится). Лишнее (выходящее) слово - отбросить.
s='Москва Уфа Тула Самара Омск Воронеж Владивосток Лондон Калининград Севастополь'.split()
lst=[]
k=0
for i in range(3):
    lst.append(list(s[k:k+3]))
    k+=3
[print(*i) for i in lst]
##################################
s = 'Москва Уфа Тула Самара Омск Воронеж Владивосток Лондон Калининград Севастополь'.split()
it = iter(s)
print(*zip(it, it, it)) #('Москва', 'Уфа', 'Тула') ('Самара', 'Омск', 'Воронеж') ('Владивосток', 'Лондон', 'Калининград'
##################################
x = iter([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(*zip(x, x, x)) #(1, 2, 3) (4, 5, 6) (7, 8, 9)
##################################
print(*zip(*[iter(s)]*3))
##################################
#Подвиг 5. Вводится строка. Требуется, используя введенную строку, сформировать N=10 пар кортежей в
# формате:(символ, порядковый индекс)Первый индекс имеет значение 0. Строка может быть короче
# 10 символов, а может быть и длиннее. То есть, число пар может быть 10 и менее. Используя функцию
# zip сформируйте указанные кортежи и сохраните в список с именем lst.
s = 'Python дай мне силы пройти этот курс до конца!'
N = 10
lst = list(zip(s, range(N)))
################################## 9.6 Сортировка с помощью sort и sorted
s = '-2 -1 8 11 4 5 '
lst = list(map(int, s.split()))
tp = tuple(lst)
lst.sort()
tp_lst = tuple(sorted(tp))

##################################
s = '-2 -1 8 11 4 5 '
def get_sort(x):
    try:
        x.sort()
        return x
    except AttributeError:
        return type(x)(sorted(x)) #приведение результата сортировки sorted(x) к типу, определенному через type(x)

lst = list(map(int, s.split()))
tp_lst = tuple(map(int, s.split()))

lst = get_sort(lst)
tp_lst = get_sort(tp_lst)
##################################
#Подвиг 3. На вход функции с именем get_sort поступает словарь, например, такой:Необходимо отсортировать словарь
# d по убыванию ключей (лексикографическая сортировка строк) и возвратить список из соответствующих значений ключей
# словаря. Например, для указанного словаря d, результатом должен быть список:
d = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}
def get_sort(d):
    d = sorted(d.items(), reverse=True)
    #[('tree', 'дерево'), ('horse', 'лошадь'), ('dog', 'собака'), ('cat', 'кот'), ('book', 'книга')]
    return list(dict(d).values())

d_sort = get_sort(d)
print(d_sort) #['дерево', 'лошадь', 'собака', 'кот', 'книга']
##################################
def get_sort(d):
    d = dict(sorted(d.items(), reverse=True))
    return list(d[v] for v in d)
##################################
def get_sort(d):
    return list(d[v] for v in sorted(d, reverse=True))
##################################
def get_sort(d):
    return list(map(lambda x: x[1], sorted(d.items(), reverse=True)))
    #[('tree', 'дерево'), ('horse', 'лошадь'), ('dog', 'собака'), ('cat', 'кот'), ('book', 'книга')]
##################################
def get_sort(d):
    return [val for key, val in sorted(d.items(), reverse=True)]
##################################
#Подвиг 4. На вход программы поступает список целых чисел, записанных в одну строчку через пробел. Необходимо выбрать
# из них четыре наибольших уникальных значения. Результат вывести на экран в порядке их убывания в одну строчку
# через пробел.
s = '10 5 4 -3 2 0 5 10 3'
s=input()
it = iter(sorted(set(map(int, s.split())), reverse=True))
for i in range(4):
    print(next(it), end=' ')
##################################
lst = list(sorted(set(map(int, s.split())), reverse=True))[:4]
##################################
#Подвиг 5. На вход программы поступают два списка целых чисел (каждый в отдельной строке), записанных в одну строчку
# через пробел. Длины списков могут быть разными. Необходимо первый список отсортировать по возрастанию, а второй -
# по убыванию. Полученные пары из обоих списков сложить друг с другом и получить новый список чисел.
l1 = '7 6 4 2 6 7 9 10 4'
l2 = '-4 5 10 4 5 65'
l1 = sorted(list(map(int, l1.split())))
l2 = sorted(list(map(int, l2.split())), reverse=True)
result = list(map(lambda x: x[0] + x[1], zip(l1, l2)))
print(*result)
##################################
result = list(map(sum, zip(l1, l2)))
##################################
#Подвиг 6. На вход программы поступает список товаров в формате:название_1:цена_1...название_N:цена_N
# Необходимо преобразовать этот список в словарь, ключами которого выступают цены (целые числа), а значениями -
# соответствующие названия товаров. Необходимо написать функцию, которая бы принимала на входе словарь и возвращала
# список из наименований трех наиболее дешевых товаров.Вызовите эту функцию и отобразите на экране полученный список
# в порядке возрастания цены в одну строчку через пробел.
import sys
def get_dict(d):
    return map(lambda x: x[1], sorted(d.items())[:3])

lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst_in = ['смартфон:120000', 'яблоко:2', 'сумка:560', 'брюки:2500', 'линейка:10', 'бумага:500']
d = {int(i.split(':')[1]): i.split(':')[0] for i in lst_in}

res = get_dict(d)
print(*res)

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

##################################

#################