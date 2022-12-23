####### 7.1 Что такое функции. Их объявление и вызов #######

# Подвиг 4. Запишите функцию без аргументов, которая считывает с клавиатуры имя и фамилию, записанные в одну строку
# через пробел, и выводит на экран сообщение (без кавычек):"Уважаемый, <имя> <фамилия>! Вы верно выполнили это задание!"

def f(fio):
    # fio=input()
    print(f'Уважаемый, {fio}! Вы верно выполнили это задание!')


f(input())


def f():
    return (f'Уважаемый, {n} {sn}! Вы верно выполнили это задание!')


n, sn = input().split()
print(f())


# Подвиг 5. Объявите функцию, которая имеет один параметр - вес предмета и выводит на экран сообщение (без кавычек):
# "Предмет имеет вес: x кг."
def f(x):
    print(f'Предмет имеет вес: {x} кг.')


f(float(input()))


# Подвиг 6. Объявите функцию, которая принимает список, находит максимальное, минимальное и сумму значений этого списка
# и выводит результат в виде строки (без кавычек):"Min = v_min, max = v_max, sum = v_sum"
# где v_min, v_max, v_sum - вычисленные значения минимального, максимального и суммы значений списка.
# После объявления функции прочитайте (с помощью функции input) список целых чисел, записанных в одну строку через
# пробел, и вызовите функцию с этим списком.

def f(lst):
    # v_min = min(lst)

    v_max = max(lst)
    v_sum = sum(lst)
    print(f'Min = {min(lst)}, max = {v_max}, sum = {v_sum}')


f(list(map(int, input().split())))


def f(arg):
    return f'Min = {min(arg)}, max = {max(arg)}, sum = {sum(arg)}'


print(f([int(i) for i in input().split()]))


# Подвиг 7. Объявите функцию с двумя параметрами width и height (ширина и высота прямоугольника), которая выводит
# сообщение (без кавычек):"Периметр прямоугольника, равен x"где x - вычисленный периметр прямоугольника.
# После объявления функции прочитайте (с помощью функции input) два целых числа, записанных в одну строку через пробел,
# и вызовите функцию с этими значениями.
def f(width, height):
    print(f'Периметр прямоугольника, равен {2 * (width + height)}')


f(*map(int, input().split()))

# Подвиг 8. Напишите функцию, которая проверяет корректность переданного ей email-адреса в виде строки. Будем полагать,
# что адрес верен, если он обязательно содержит символы '@' и '.', а все остальные символы могут принимать значения:
# 'a-z', 'A-Z', '0-9' и '_'. Если email верен, то функция выводит ДА, иначе - НЕТ.После объявления функции прочитайте
# (с помощью функции input) строку с email-адресом и вызовите функцию с этим аргументом.

import re


def f(arg):
    match = re.findall(r'[(d) (a-z) (A-Z) (\_\@\.)]', arg)
    s = ''.join(match)
    print(s)
    if s == arg and '@' in arg and '.' in arg:
        # if s == arg and arg.count('@') == 1 and arg.count('.'):

        print('ДА')
    else:
        print('НЕТ')


f(input())

t = {'A', 'E', 'I', 'O', 'U', 'Y', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V',
     'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_', 'a', 'e', 'i', 'o', 'u', 'y', 'b', 'c',
     'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', '@', '.'}


def f(arg):
    # print(arg)
    for i in arg:
        if i not in t or '@' not in arg or '.' not in arg:
            print('НЕТ')
            break
    else:
        print('ДА')


f(input())


def f(arg):
    s = set("abcdefghijklmnopqrstuvwxyz0123456789_@.")
    s2 = {"@", "."}
    print("ДА") if s2 <= arg <= s else print("НЕТ")


f(set(input().lower()))


def check_mail(mail):
    allow = set("abcdefghijklmnopqrstuvwxyz0123456789_.")
    mail_set = set("".join(mail.split("@", 1)))
    print("ДА") if {"."} < mail_set <= allow else print("НЕТ")


check_mail(input().lower())

t = {'A', 'E', 'I', 'O', 'U', 'Y', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V',
     'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_', 'a', 'e', 'i', 'o', 'u', 'y', 'b', 'c',
     'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', '@', "."}


def foo(email):
    print('ДА') if '@' in email and '.' in email and set(email) <= t else print('НЕТ')


foo(input())

import re


def check_email(email):
    regex = r'[A-Za-z0-9_]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}'
    print('ДА' if re.fullmatch(regex, email) else 'НЕТ')


check_email(input())


def f(arg):
    if '@' in arg and '.' in arg:
        flag = True
        arg = arg.replace('@', '').replace('.', '')
        for i in arg:
            if not ('a' <= i <= 'z' or 'A' <= i <= 'Z' or '0' <= i <= '9' or i == '_'):
                flag = False
                break
    else:
        flag = False
    print('ДА' if flag else 'НЕТ')


f(input())

from string import ascii_letters as asc, digits as ds


def f(arg):
    str = asc + ds + '@_.'
    if '@' in arg and '.' in arg:
        flag = all(i in str for i in arg)
    print('ДА' if flag else 'НЕТ')


f(input())


def f(arg):
    print('ДА' if set(lst) >= set(arg) and '@' in arg and '.' in arg else 'НЕТ')


dct_w = [chr(i) for i in range(ord('a'), ord('z'))]
dct_W = [chr(i) for i in range(ord('A'), ord('A'))]
dct_n = [str(i) for i in range(10)]
lst = dct_w + dct_W + dct_n + ['@', '_', '.']
f(input())


def f(arg):
    res = 'НЕТ'
    s = set(arg)
    ns = set(i for i in range(10))
    alfa = set(chr(i) for i in range(ord('a'), ord('z') + 1))
    if '@' in s and '.' in s:
        s -= ns | alfa | {'@', '.', '_'}
        if not s:  # len(s)==0:
            res = 'ДА'
    print(res)


f(input().lower())

from string import *

s = 'sc_lib@list.ru'
asc = ascii_letters + digits + '@._'
print(['НЕТ', 'ДА'][all(i in asc for i in s) and s.count('@') == s.count('.') == 1])
print(['НЕТ', 'ДА'][all(map(lambda x: x in asc, s)) and s.count('@') == s.count('.') == 1])

import re


def f(arg):
    mail = re.findall(r'[a-z0-9]*_[a-z0-9]*@{1}[a-z0-9]*.[a-z]*', arg)  # Возвращаемое значение:список совпадений.
    # возвращает все неперекрывающиеся совпадения
    # шаблона pattern в строке string в виде списка строк или список кортежей
    print('ДА' if mail == [arg] else 'НЕТ')

    mail_val = re.fullmatch("[a-z0-9]*_[a-z0-9]*@{1}[a-z]*.[a-z]*", arg)  # вернет объект сопоставления, если вся
    # строка string соответствует шаблону регулярного выражения pattern.вернет None, если строка не соответствует шаблону
    print(mail_val)  # <re.Match object; span=(0, 14), match='sc_lib@list.ru'>
    print('ДА' if mail_val else 'НЕТ')


f('sc_lib@List.ru'.lower())

import re


def is_email(s: str):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(regex, s):  # re.search(pattern, string, flags=0)
        # search() вернет None, если ни одна позиция в строке string не соответствует шаблону
        print('ДА')
    else:
        print('НЕТ')


s = 'sc_lib@list.ru'
is_email(s)

import re


def check_email(email):
    x = re.match(r'^(?:[a-zA-Z0-9-_.]+?)(?:@)(?:[a-zA-Z0-9-]+?\.)(?:[a-zA-Z]+?)$', i)
    print('НЕТ' if x is None else 'ДА')


i = input()
check_email(i)


def chek_email(s):
    s = set(s) - t

    print('НЕТ' if s else 'ДА')  # проверить на пустое множество s


t = {'A', 'E', 'I', 'O', 'U', 'Y', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V',
     'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_', 'a', 'e', 'i', 'o', 'u', 'y', 'b', 'c',
     'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', '@', '.'}
chek_email('sc_lib@list.ru')

x = set(__import__('re').sub(r'[a-zA-Z\d_]', '', input()))  # Поиск и замена на основе регулярного выражения.
# re.sub(pattern, repl, string, count=0, flags=0)Возвращаемое значение: строка
# Функция sub() модуля re возвращает строку, полученную путем замены крайнего левого неперекрывающегося вхождения
# шаблона регулярного выражения pattern в строке string на строку замены repl. Если шаблон регулярного выражения не
# найден, строка возвращается без изменений.

print(('НЕТ', 'ДА')[{'@', '.'}.issubset(x) and len(x) == 2])


def check_email(email: str) -> None:
    print('ДА' if bool(__import__('re')
                       .match(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.[a-zA-Z0-9_]+$", email)) else 'НЕТ')


check_email(input())

import string


def f(arg):
    valid = string.ascii_letters + string.digits + '@' + '.' + '_'
    if '@' in arg and '.' in arg:
        flag = set(arg).issubset(set(valid))
    else:
        flag = False
    print('ДА' if flag else 'НЕТ')


f(input())

import string


def f(arg):
    valid = string.ascii_letters + string.digits + '@' + '.' + '_'
    if arg.count('@') == arg.count('.') == 1:
        flag = set(arg).issubset(set(valid))
    else:
        flag = False
    print('ДА' if flag else 'НЕТ')


f(input())


#######7.2 Оператор return
# Подвиг 4. Объявите функцию для проверки числа на четность (возвращается True, если переданное число четное и False,
# если число нечетное).После объявления функции в цикле необходимо считывать целое числовое значение (функцией input),
# пока не поступит число 1. Если прочитанное значение четное (проверяется с помощью заданной функции), то оно
# выводится на экран (в столбик, то есть, каждое значение с новой строки).
def f(n):
    return True if n % 2 == 0 else False


n = int(input())
while n != 1:
    if f(n):
        print(n)
    n = int(input())


def f(n):
    return not int(n) % 2


for i in iter(input, '1'):
    if f(i):
        print(i)


def f(n):
    return not int(n) % 2


print(*[i for i in iter(input, '1') if f(i)], sep='\n')


# Подвиг 5. Объявите функцию для проверки числа на нечетность (возвращается True, если переданное число нечетное и False
# , если число четное). После объявления функции прочитайте (с помощью функции input) список целых значений,
# записанных в одну строку через пробел. И, используя генератор списков и созданную функцию, сформируйте список из
# нечетных значений на основе введенного исходного списка. Результат отобразите на экране командой:
def f(x):
    return int(x) % 2


lst = [i for i in input().split() if f(i)]
print(*lst)


def f(x):
    return x % 2


print(*filter(f, map(int, input().split())))

f = lambda *arg: print(
    *filter(lambda arg: arg % 2, arg))  # просьба поясните пжл общую схему: f это функция, которая принимает
# *args (не сколько аргументов) и выполняет print по  условию,   так ? или есть нюансы ? да...именно так  ...  *args
# в данном случае это 1 объект -кортеж из нескольких аргументов ...который является итерируемым объектом ,поэтому для
# него можно использовать функцию filter, в которой прописано условие фильтрации - lambda x: x%2 ,то есть отобрать
# все элементы исходного кортежа ,для которых выполняется условие x%2 (которое означает что существует остаток от
# деления этого элемента на 2 не равный 0)
f(*map(int, input().split()))

(lambda x: print(*[i for i in list(map(int, input().split())) if x(i)]))(lambda x: x % 2 != 0)
# lambda аргумент лямбды: <тело лямбды>(передаваемое значение в аргумент лямбды)1) (lambda x: x % 2 != 0) - выбирается
# как аргумент для lambda x: print(*[i for i in list(map(int, input().split())) if x(i)]
# 2) Она попадает в lambda x: и используется в блоке if x(i)
# 3) Блок if x(i) проверяет i на чётность в генераторе списка [i for i in list(map(int, input().split())) if x(i)]
# 4) Проверка осуществляется за счёт того, что x это lambda x: x % 2 != 0, которая была передана ранее в виде аргумента
# . x(i) - вызов функции, равнозначный lambda x: x % 2 != 0(i)
# Я настоятельно не рекомендую прибегать к подобному синтаксису, если это не даёт выигрыша в производительности
# или расходе памяти.


# Подвиг 6. Вводится слово в переменную tp. Если это слово RECT, то следует объявить функцию с именем get_sq с двумя
# параметрами, вычисляющую площадь прямоугольника и возвращающую вычисленное значение. (На экран она ничего не должна
# выводить, только возвращать значение). Если же введенное слово не RECT (любое другое), то объявляется функция с тем
# же именем get_sq, с одним параметром для вычисления площади квадрата (формула: a*a). Вычисленное значение
# возвращается функцией. (Она также ничего не выводит на экран).Примечание: в программе должна быть задана только
# одна функция с именем get_sq в зависимости от введенного слова. Вызывать функцию не нужно, только объявлять.

tp = input().strip()

if tp == 'RECT':
    def get_sq(a, b):
        print(a, b)
        return a * b

else:
    def get_sq(a):
        return a * a

tp = input().strip()

if tp == 'RECT':
    get_sq = lambda a, b: a * b


else:
    get_sq = lambda a: a * a


def is_odd(n):
    return n & 1


print(*(e for e in map(int, input().split()) if is_odd(e)))


# n & 1 - это операция побитового "и", имеет тот же эффект что и n % 2. Четность числа можно определить по младшему
# разряду его битового представления. У четных чисел он равен нулю, а у нечентых - равен единице. Число 1 используется
# как битовая маска, выделяющая младший разряд битового представления числа n. Подробнее битовые операции разбираются
# в отдельном уроке 10.2.


# Подвиг 7. Объявите функцию, которая принимает строку (в качестве аргумента) и возвращает False, если длина строки
# меньше 6 символов. Иначе возвращается значение True.После объявления функции прочитайте (с помощью функции input)
# список названий городов, записанных в одну строку через пробел. Затем, используя генератор списка и созданную функцию,
# сформируйте список из названий городов длиной не менее шести символов на основе введенного исходного списка
def f(s):
    return len(s) > 5


lst = [i for i in input().split() if f(i)]
print(*lst)

print(*filter(f, input().split()))

print(*filter(lambda x: len(x) >= 6, input().split()))


# Подвиг 8. Объявите функцию, которая принимает строку (в качестве аргумента) и возвращает два значения в виде кортежа:
# переданная строка и ее длина.После объявления функции прочитайте (с помощью функции input) список названий городов,
# записанных в одну строку через пробел. Затем, используя генератор словарей и созданную функцию, сформируйте словарь
# d в формате:d = {<город 1>: <число символов>, ..., <город N>: <число символов>}

def f(s):
    return (s, len(s))


d = {f(i)[0]: f(i)[1] for i in input().split()}
d = dict(f(i) for i in input().split())
d = {k: v for k, v in map(f, input().split())}

a = sorted(d, key=lambda x: d[x])  # sorted(iterable, *, key=None, reverse=False)
a = sorted(d, key=d.get)
print(*a)

print(*sorted(input().split(), key=len))


# Подвиг 9. Вводится список целых чисел в одну строчку через пробел. Необходимо задать функцию, которая принимает два
# аргумента (максимальное и минимальное значения из списка) и возвращает их произведение. Вызовите эту функцию и
# отобразите на экране полученное числовое значение.
def f(x, y):
    return x * y


lst = list(map(int, input().split()))
lst = [int(i) for i in input().split()]
print(f(max(lst), min(lst)))

print((lambda x: x[0] * x[-1])(sorted(map(int, input().split()))))

import doctest  # Другие возможности тестирования:

doctest.testmode()


# Большой подвиг 1. Повторите быстрый алгоритм Евклида для нахождения наибольшего общего делителя двух натуральных
# чисел a и b. В программе необходимо объявить функцию get_nod, которая принимает два аргумента a и b (натуральные
# числа) и возвращает вычисленное значение НОД(a, b).

def get_nod(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b

    return a


print(get_nod(18, 24))

import math


def get_nod(a, b):
    return math.gcd(a, b)


# Подвиг 2. Объявите функцию с именем get_rect_value, которая принимает два аргумента (два числа) и еще один формальный
# параметр type с начальным значением 0. Если параметр type равен нулю, то функция должна возвращать периметр
# прямоугольника, а иначе - его площадь.

def get_rect_value(a, b, type=0):
    if not type:
        return 2 * (a + b)
    else:
        return a * b


def get_rect_value(a, b, type=0):
    return a * b if type else 2 * (a + b)


def get_rect_value(a, b, type=0):
    return [2 * (a + b), a * b][type]


# Подвиг 3. Объявите функцию с именем check_password, которая принимает аргумент - строку (пароль) и имеет один
# формальный параметр chars с начальным значением в виде строки "$%!?@#". Функция должна проверять: есть ли в пароле
# хотя бы один символ из chars и что длина пароля не менее 8 символов. Если проверка проходит, то функция возвращает
# True, иначе - False.

def check_password(s, chars="$%!?@#"):
    return True if len(s) > 7 and any(i for i in s if i in chars) else False


def check_password(s, chars="$%!?@#"):
    return len(s) > 7 and len(set(s) & set(chars)) != 0
    return True if set(s) & set(chars) and len(s) >= 8 else False
    return bool(len(s) > 7 and set(s) & set(chars))
    # (len(s) > 7) * len(set(s)&set(chars)) > 0


# Подвиг 4. Объявите функцию, которая принимает строку на кириллице и преобразовывает ее в латиницу, используя следующий
# словарь для замены русских букв на соответствующее латинское написание:
# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
# 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
# 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
# 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
# Функция должна возвращать преобразованную строку. Замены делать без учета регистра (исходную строку перевести в
# нижний регистр - малые буквы). У функции также определить формальный параметр sep с начальным значением в виде
# строки "-". Он будет определять символ для замены пробелов в строке.
# После объявления функции прочитайте (с помощью функции input) строку и дважды вызовите функцию (с выводом результата
# ее работы на экран):- первый раз только со строкой - второй раз со строкой и именованным аргументом sep
# со значением '+'.

def func(s, t, sep='-'):
    string = ''
    for i in s:
        if i == ' ':
            string += sep
        elif i.lower() not in t:
            string += i.lower()
        else:
            string += t[i.lower()]
    return string


s = input()
a = func(s, t, )
b = func(s, t, sep='+')
print(a)
print(b)


def func(s, sep='-'):
    return ''.join([t[i] if i in t else i for i in s]).replace(' ', sep)


s = input().lower()
print(func(s))
print(func(s, sep='+'))


def func(s, sep='-'):
    t.update({' ': sep})
    return ''.join([t.get(i, i) for i in s])  # dict.get(key[, default])
    return ''.join([t.get(i, i) for i in s.replace(' ', sep)])
    return ''.join([t[i] if i in t else sep if i == ' ' else i for i in st])


s = input().lower()
print(func(s))
print(func(s, sep='+'))


def f(s, sep='-'):
    return s.replace(' ', sep).translate(t)  # str.translate(table)
    # Метод str.translate() возвращает копию строки, в которой каждый
    # символ был сопоставлен и преобразован согласно карте перевода символов table.


def f(s, sep='-'):
    s = s.replace(' ', sep)  # Идем по словарю и меняем символы в строке, отдельно меняем пробел на sep:
    for k, v in t.items():
        s.replace(k, t.get(k, v))  # dict.get(key[, default])
    return s


# Подвиг 5. Объявите функцию, которая принимает строку и заключает ее в указанный тег. Тег определяется формальным
# параметров tag с начальным значением в виде строки "h1". Например, мы передаем строку "Hello Python" и заключаем
# в тег "h1". На выходе должны получить строку (без кавычек):"<h1>Hello Python</h1>"
# То есть, сначала открывается тег <h1>, а в конце строки - закрывается </h1>. И так для любых указанных тегов.
# После объявления функции прочитайте (с помощью функции input) строку и дважды вызовите функцию (с выводом
# результата ее работы на экран): первый раз только со строкой - второй раз со строкой и именованным аргументом
# tag со значением 'div'.

def f(s, tag='h1'):
    return f'<{tag}>{s}</{tag}>'


s = input()
print(f(s))
print(f(s, tag='div'))


# Подвиг 6. Функции из предыдущего подвига 5 добавьте еще один формальный параметр up с начальным булевым значением
# True. Если параметр up равен True, то тег (указанный в формальном параметре tag) следует записывать заглавными
# буквами, а иначе - малыми.После объявления функции прочитайте (с помощью функции input) строку и дважды вызовите
# функцию (с выводом результата ее работы на экран):- первый раз со строкой и именованным аргументом tag со
# значением 'div'- второй раз со строкой, именованным аргументом tag со значением 'div' и именованным аргументом up
# со значением False.

def f(s, tag='h1', up=True):
    return f'<{tag.upper()}>{s}</{tag.upper()}>' \
        if up else \
        f'<{tag}>{s}</{tag}>'


s = input()
print(f(s, tag='div'), f(s, tag='div', up=False), sep='\n')


def f(s, tag='h1', up=True):
    return '<{1}>{0}</{1}>'.format(s, tag.upper() if up else tag)  # str.format(*args, **kwargs)


# *args - позиционные аргументы
# **kwargs - ключевые аргументы

s = input()
print(f(s, tag='div'), f(s, tag='div', up=False), sep='\n')


######7.5 Функции с произвольным числом параметров ##########
# Подвиг 3. Объявите функцию с именем get_even, которая принимает произвольное количество чисел в качестве аргументов
# и возвращает список, составленный только из четных переданных значений.
def get_even(*args):
    return [i for i in args if not int(i) % 2]


m = map(int, input().split())
print(get_even(*m))

lst = list(map(int, input().split()))
print(get_even(*lst))


def get_even(*args):
    return list(filter(lambda x: x % 2 == 0, args))


get_even = lambda *args: [x for x in args if not x % 2]


# Подвиг 4. Объявите функцию с именем get_biggest_city, которой можно передавать произвольное количество названий
# городов через аргументы. Данная функция должна возвращать название города наибольшей длины. Если таких городов
# несколько, то первый найденный (из наибольших). Программу реализовать без использования сортировки.

def get_biggest_city(*args):
    max_i = 0
    print(len(args), args)
    for i in range(len(args) - 1):
        if len(args[i]) > len(args[i + 1]):
            max_i = args[i]
        else:
            max_i = args[i + 1]
    return max_i


lst = list(map(str, input().split()))
print(lst)
print(get_biggest_city(*lst))


def get_biggest_city(*args):
    max_i = ''
    for i in args:
        if len(i) > len(max_i):
            max_i = i
    return max_i


def get_biggest_city(*args):
    return max(args, key=len)

    d = {len(i): i for i in args}
    return d[max(d)]


# Подвиг 5. Объявите функцию с именем get_data_fig для вычисления периметра произвольного N-угольника. На вход этой
# функции передаются N длин сторон через аргументы. Дополнительно могут быть указаны именованные аргументы:
# type - булево значение True/False
# color - целое числовое значение
# closed - булево значение True/False
# width - целое значение
# Функция должна возвращать в виде кортежа периметр многоугольника и указанные значения именованных параметров
# в порядке их перечисления в тексте задания (если они были переданы). Если какой-либо параметр отсутствует, его
# возвращать не нужно (пропустить).

def get_data_fig(*args, **kwargs):
    s = sum(args)
    d = {'s': s, 'type': None, 'color': None, 'closed': None, 'width': None}
    for i in kwargs:
        d[i] = kwargs[i]
    lst = []
    for j in d.values():
        if j != None:
            lst.append(j)
    return tuple(lst)


print(get_data_fig(1, 2, 3, color=True, closed=True, width=True, type=True))


def get_data_fig(*args, **kwargs):
    lst = [kwargs[i] for i in ['type', 'color', 'closed', 'width']]
    return (sum(args), *lst)


def get_data_fig(*args, **kwargs):
    args = sum(args),
    if 'type' in kwargs:
        args += kwargs['type'],
    if 'color' in kwargs:
        args += kwargs['color'],
    if 'closed' in kwargs:
        args += kwargs['closed'],
    if 'width' in kwargs:
        args += kwargs['width'],
    return args


def get_data_fig(*args, **kwargs):
    d = {'type': True, 'color': True, 'closed': True, 'width': True}
    return (sum(args),) + tuple([d[k] for k in d if d[k] == kwargs[k]])


return (sum(args),) + tuple(kwargs[i] for i in ['type', 'color', 'closed', 'width'] if i in kwargs)


def get_data_fig(*args, **kwargs):
    s = (sum(args),)
    for i in ['type', 'color', 'closed', 'width']:
        if i in kwargs:
            s += (kwargs[i],)
    return s


def get_data_fig(*args, **kwargs):
    return ([sum(args)] + [kwargs[i] for i in ['type', 'color', 'closed', 'width'] if i in kwargs])


def get_data_fig(*args, **kwargs):
    return tuple([sum(args)] + [kwargs[i] for i in ['type', 'color', 'closed', 'width'] if i in kwargs])


def get_data_fig(*args, **kwargs):
    return (sum(args),) + tuple(kwargs[i] for i in ['type', 'color', 'closed', 'width'] if i in kwargs)


# Большой подвиг 6. (Для закрепления предыдущего материала). Вводится таблица целых чисел (см. пример ниже) размером
# N x N элементов (N определяется по входным данным). Эта таблица содержит нули, но кое-где - единицы. С помощью функции
# с именем verify, на вход которой передается двумерный список чисел, необходимо проверить, являются ли единицы
# изолированными друг от друга, то есть, вокруг каждой единицы должны быть нули.
# Рекомендуется следующий алгоритм. В функции verify производить перебор двумерного списка. Для каждого элемента
# (списка) со значением 1 вызывать еще одну вспомогательную функцию is_isolate для проверки изолированности единицы.
# То есть, функция is_isolate должна возвращать True, если единица изолирована и False - в противном случае.
# Как только встречается не изолированная единица, функция verify должна возвращать False. Если успешно доходим
# (по элементам списка) до конца, то возвращается значение True.
import sys

s = sys.stdin.readlines()

lst = [list(map(int, i.strip().split())) for i in s]


def is_isolate(*args):
    return sum(args) < 2
    # return sum(*args) < 2


def verify(l):
    for i in range(len(l) - 1):
        for j in range(len(l[i]) - 1):
            if l[j] == 1:
                if not is_isolate(l[i][j:j + 2], l[i + 1][j:j + 2]):
                    # if not is_isolate(l[i][j:j + 2]+ l[i + 1][j:j + 2]):
                    return False
    return True


print(verify(lst))


# Значимый подвиг 7. (Для закрепления предыдущего материала). Объявите функцию с именем str_min, которая сравнивает
# две переданные строки и возвращает минимальную из них (то есть, выполняется лексикографическое сравнение строк).
# Затем, используя функциональный подход к программированию (то есть, более сложные функции реализуются путем вызова
# более простых), реализовать еще две аналогичные функции:- с именем str_min3 для поиска минимальной строки из трех
# переданных строк;- с именем str_min4 для поиска минимальной строки из четырех переданных строк.
def str_min4(s4):
    def str_min3(s3):
        def str_min(*args):
            s = min(args, key=len)
            return s

        s = str_min('s222', 'a22222')
        print(s)

        s_min3 = min(s3, s, key=len)
        return s_min3

    s3 = str_min3('s33')
    print(s3)

    s_min4 = min(s4, s3, key=len)
    return s_min4


s4 = str_min4('s4')
print(s4)


##############
def str_min(*args):
    return min(*args, key=len)


def str_min3(*args):
    # print(':', args) #: ('s222', 's22222', 's33', 's333', 's333333')
    return min(args, key=len)


def str_min4(*args):
    return min(args, key=len)


s2 = 's222', 's22222'  # передаётся как кортеж ('s222', 's22222')
s3 = 's33', 's333', 's333333'
s4 = 's4', 's44', 's222', 's444444'

print('str_min:', str_min(s2))
print('str_min3:', str_min3(*s2, *s3))
print('str_min4:', str_min3(*s2, *s3, *s4))
print('str_min4:', str_min4('s4', str_min3('s33', str_min('s222', 's22222'))))  # без распаковки передача функции в


# функцию

def str_min(*args):
    return min(*args, key=len)


def str_min3(*args):
    return min(*args, str_min(*args), key=len)


def str_min4(*args):
    return min(*args, str_min3(*args), key=len)


s2 = 's222', 's22222', '000'  # передаётся как кортеж ('s222', 's22222')
s3 = 's33', 's333', 's333333', '11'
s4 = 's4', 's44', 's222', 's444444'
###ничего не работает!!!!!!!!
print('str_min:', str_min(s2))  # str_min: s222 почему не надо распоковывать???
print('str_min3:', str_min3(*s3))  # str_min3: s33
print('str_min4:', str_min3(*s4))  # str_min4: s4
# str_min: 0
# str_min3: 11
# str_min4: s4


###########7.6 Операторы упаковки и распаковки коллекций
# Подвиг 2. Вводится список из семи целых чисел в одну строчку через пробел. Необходимо первые четыре числа занести в
# переменную lst, а остальные три в отдельные переменные x, y, z. Сделать с использованием оператора упаковки

*lst, x, y, z = map(int, input().split())
print(*lst)

# Подвиг 3. Вводятся названия городов в одну строчку через пробел. На основе этой строки необходимо сформировать список
# из названий. А, затем, используя оператор распаковки *, преобразовать этот список в кортеж lst_c.
lst = input().split(),
lst_c = tuple(*lst)
# lst_c = *lst,
print(lst_c)

lst_c = *input().split(),
print(lst_c)

lst = input().split()
print((*lst,))

# Подвиг 4. Вводятся два целых значения a и b (a < b) в одну строчку через пробел. Необходимо сформировать список из
# целых чисел от a до b (включительно) с шагом изменения 1, используя функцию range, оператор [] и оператор
# распаковки *

l = list(map(int, input().split()))
lst = [*range(l[0], l[1] + 1)]
print(*lst)

a, b = map(int, input().split())
lst = [*range(a, b + 1)]
print(*lst)

l = list(map(int, input().split()))
l[-1] += 1
lst = [*range(*l)]
print(*lst)

print(*(lambda a, b: range(a, b + 1))(*map(int, input().split())))

# Подвиг 5. Вводится список вещественных чисел и список названий городов, каждый в отдельной строке. Необходимо
# сформировать единый список lst, в котором сначала идут числа, а затем, названия городов. Реализовать программу с
# помощью оператор распаковки *

l1 = list(map(float, input().split()))
l2 = list(map(str, input().split()))
l1, l2 = list(map(float, input().split())), input().split()
lst = *l1, *l2
print(*lst)

print(*open(0).read().split())  # 5.8 11.0 4.3 РЈС„Р° РћРјСЃРє РўРІРµСЂСЊ РЎР°РјР°СЂР°

import sys

s = sys.stdin.read().split()
print(*s)

import sys

s = sys.stdin.readlines()
l = [i.strip() for i in s]
print(*l)

import sys

s = sys.stdin.readlines()
lst = [i.strip() for i in s]
print(lst)
lst = [*(float(i) for i in lst[0].split()), *(str(i) for i in lst[0].split())]
print(lst)

lst = [*map(float, input().split()), *input().split()]
print(*lst)

print(*input().split() + input().split())

lst = list(map(float, input().split()))
lst.extend(input().split())  # list.extend() в Python, расширяет список другой последовательностью
# в конец последовательности sequence добавляются элементы iterable.
print(*lst)

*a, b = *list(map(float, input().split())), input()
*a, b = *map(float, input().split()), input()
print((*a, b))  # (5.8, 11.0, 4.3, 'sgedgherhg')
print(*(*a, b))  # 5.8, 11.0, 4.3, 'sgedgherhg' без кортежа

print(*map(float, input().split()), input())

# Подвиг 6. Имеется словарь, содержащий пункты меню:menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
# Дополнительно вводятся еще пункты меню в виде строк в формате:
# название_1=url_1
# название_N=url_N
# Необходимо эту введенную информацию преобразовать в словарь и добавить к словарю menu, используя оператор
# распаковки для словарей. На результирующий словарь должна вести переменная menu.

lst_in = list(map(str.strip, sys.stdin.readlines()))
print(lst_in)

d = {i.split('=')[0]: i.split('=')[1] for i in lst_in}
menu = {**menu, **d}
menu |= d  # объединение {}
print(*menu.keys())
print(*menu.values())

s = sys.stdin.readlines()
d = dict(
    k.strip().split('=') for k in s)  # {'Города': 'about-cities', 'Машины': 'read-of-cars', 'Самолеты': 'airplanes'}
menu = {**menu, **d}


###############################7.7 Рекурсивные функции
# Подвиг 2. Вводится целое положительное число N. Необходимо написать рекурсивную функцию с именем get_rec_N, которая
# отображает на экране последовательность целых чисел от 1 до N (включительно). Каждое число выводится с новой строки.

def get_rec_N(N):
    if N > 0:
        get_rec_N(N - 1)
        print(N)


get_rec_N(8)


def get_rec_N(N):
    if N > 1:
        get_rec_N(N - 1)
    print(N)


get_rec_N(8)


# Подвиг 3. Вводится список целых чисел в одну строчку через пробел. Необходимо вычислить сумму этих введенных
# значений, используя рекурсивную функцию (для перебора элементов списка) с именем get_rec_sum. Функция должна
# возвращать значение суммы.
def get_rec_sum(l):
    if len(l) == 1:
        return l[0]  # l[-1]
    else:
        return l[0] + get_rec_sum(l[1:])


l = [8, 11, -5, 4, 3]
l = list(map(int, input().split()))
l = [int(i) for i in input().split()]
print(get_rec_sum(l))


def get_rec_sum(lst):
    head, *tail = lst
    if tail:
        return head + get_rec_sum(tail)
    else:
        return head
    # return head + get_rec_sum(tail) if tail else head


def get_rec_sum(lst):
    head, *tail = lst
    if not tail:
        return head
    else:
        return head + get_rec_sum(tail)


# если рассматривать концептуальный алгоритм для этой задачи, без технической реализации, то получится следующее:
# 1. 'Отрываем' от списка первое число, до тех пор пока не останется пустой список.
# 2. Складываем 'оторванные' числа.Вот аналог, через цикл while
lst = [1, 2, 3, 4, 5, 6]
summ = 0
while lst:
    head, *lst = lst
    summ += head
print(summ)


def get_rec_sum(l):
    if len(l) == 0:  # Определяем "базовый случай": len(lst) == 0, при котором рекурсия заканчивается.
        # А далее суммируем lst[0] со всех шагов  рекурсии.
        return 0
    else:
        return l[0] + get_rec_sum(l[1:])


def get_rec_sum(l):
    return 0 if len(l) == 0 else l[0] + get_rec_sum(l[1:])


def get_rec_sum(l):
    if len(l) > 0:
        return l.pop() + get_rec_sum(l)
    return 0


def get_rec_sum(lst):
    return lst and lst[-1] + get_rec_sum(lst[:-1]) or 0


def get_rec_sum(lst):
    return bool(lst) and lst[0] + get_rec_sum(lst[1:])


def get_rec_sum(lst):
    return 0 if not lst else lst[0] + get_rec_sum(lst[1:])


# Подвиг 4. Вводится натуральное число N. Необходимо с помощью рекурсивной функции fib_rec(N, f=[]) (здесь N - общее
# количество чисел Фибоначчи; f - начальный список этих чисел) сформировать последовательность чисел Фибоначчи по
# правилу: первые два числа равны 1 и 1, а каждое следующе значение равно сумме двух предыдущих. Пример такой
# последовательности для первых 7 чисел: 1, 1, 2, 3, 5, 8, 13, ...Функция должна возвращать список сформированной
# последовательности длиной N.

def fib_rec(N, f=[]):
    if len(f) == N:
        return f
    elif f is None:
        return fib_rec(N, f=[1, 1])
    else:
        f.append(f[-1] + f[-2])
        return fib_rec(N, f)


N = 7
print(*range(1, N + 1))  # 1 2 3 4 5 6 7
print(*fib_rec(N))


def fib_rec(N, f=[1, 1]):
    for i in range(N - 2):
        f.append(f[-1] + f[-2])
        # f.append(sum(f[-2:]))
    return f


def fib_rec(N, f=[]):  # Вся прелесть записи входной переменной f=[] при определении функции в том, что для данного
    # параметра зарезервирован адрес памяти и он не меняется (если не переопределять переменную, а работать с ней
    # только методами списка). Т.е. если в программе в первый раз вычислить fib_rec(10) и записать полученный ряд в
    # f, то при следующем обращении fib_rec(4) адрес памяти списка f будет тем же и там уже хранится ранее
    # вычисленный ряд из 10 чисел. Заново вычислять ряд не нужно. Останется только выбрать нужное количество
    # элементов из ряда.
    if len(f) < N:
        f.append(1 if len(f) < 2 else f[-1] + f[-2])
        fib_rec(N)
    return f[:N]  # Заново вычислять ряд не нужно. Останется только выбрать нужное количество элементов из ряда.
    # + f[:N]   нужен    лишь    для    случая    N = 1, чтобы   на   выводе   не   оказались   два    числа 1 1


def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib_rec(N, f=[]):
    f = [fib(i) for i in range(N)]
    return f


def fib_rec(N, f=[1, 1]):
    return fib_rec(N, f + [f[-1] + f[-2]]) if len(f) < N else f[:N]


def fib_rec(N, f=[]):
    f.append(1) if len(f) < 2 else f.append(f[-1] + f[-2])
    return f if len(f) == N else fib_rec(N, f)


# Подвиг 5. Вводится целое неотрицательное число n. Необходимо с помощью рекурсивной функции fact_rec вычислить
# факториал числа n. Напомню, что факториал числа, равен: n! = 1 * 2 * 3 *...* n. Функция должна возвращать
# вычисленное значение.

def fact_rec(n):
    if n < 2:
        return 1
    return n * fact_rec(n - 1)


print(fact_rec(3))


def fact_rec(n):
    return 1 if n < 2 else n * fact_rec(n - 1)


def fact_rec(n):
    return 1 if not n else n * fact_rec(n - 1)


def fact_rec(n):
    return n and n * fact_rec(n - 1) or 1


# Подвиг 6. Имеется следующий многомерный список:
# d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
# С помощью рекурсивной функции get_line_list создать на его основе одномерный список из значений элементов
# списка d. Функция должна возвращать новый созданный одномерный список.


d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
def get_line_list(d, l=[]):
    for i in d:
        if type(i) is list:
       #if isinstance(i,list):
            get_line_list(i)
        else:
            l.append(i)
    return l
print(get_line_list(d))

def get_line_list(d, l=[]):
    [get_line_list(i) if isinstance(i,list) else l.append(i) for i in d]
    return l

def get_line_list(d, l=[]):
    for i in d:
        if isinstance(i, list):
            get_line_list(i)
        else:
            l.append(i)
    return l


#Подвиг 7. Лягушка прыгает вперед и может скакнуть либо на одно деление, либо сразу на два. Наша задача определить
# количество вариантов маршрутов, которыми лягушка может достичь риски под номером N (натуральное число N вводится
# с клавиатуры).

def get_path(N):
    if N == 1:
        return 1
    if N == 2:
        return 2
    else:
        return get_path(N - 1) + get_path(N - 2)


N = int(input())
print(get_path(N))

def get_path(n):
    if n <= 2:
        return n
    return get_path(n - 1) + get_path(n - 2)

def get_path(n):
    if n > 2:
        return get_path(n - 1) + get_path(n - 2)
    return n


#Великий подвиг 8. Вводится список из целых чисел в одну строчку через пробел. Необходимо выполнить его
# сортировку по возрастанию с помощью алгоритма сортировки слиянием. Функция должна возвращать новый
# отсортированный список.Вызовите результирующую функцию сортировки для введенного списка и отобразите результат
# на экран в виде последовательности чисел, записанных через пробел.

def f(n):
    return sorted(n)


n = list(map(int, input().split()))
print(*f(n))



#по Хирьянову
def merge(L, R): # алгоритм слияния
    C = [0] * (len(L) + len(R))
    i = k = n = 0
    while i < len(L) and k < len(R):
        if L[i] <= R[k]:
            C[n] = L[i];  i += 1;  n += 1
        else:
            C[n] = R[k];k += 1 ;n += 1
    while i < len(L):
        C[n] = L[i]; i += 1;n += 1
    while k < len(R):
        C[n] = R[k]
        k += 1
        n += 1
    return C


def merge_sort(l): #сортировка рекурсивной функцией
    if len(l) <= 1:
        return #None
    L = [l[i] for i in range(len(l) // 2)]
    R = [l[i] for i in range(len(l) // 2, len(l))]
    merge_sort(L) #отсортированные половинки
    merge_sort(R)
    C = merge(L, R) #слияние в единый массив
    for i in range(len(l)):
        l[i] = C[i] #заменяем старый список l на отсортированный список C
        #! но нельзя делать так l=С, т к просто меняется ссылка на объект при этом R,L,C списки сеъст сборщик
        # мусора и они уничтожаться и l не сможет ссылаться на C
    return C

l = list(map(int, input().split()))
#l = [8, 11, -6, 3, 0, 1]
print(*merge_sort(l))


##########################
def merge_two_lists(a, b):
    res = []
    while a and b:
        res += [a.pop(0) if a[0] < b[0] else b.pop(0)]
    return res + a + b

def merge_sort(l):
    if len(l) == 1:
        return l
    mid = len(l) // 2
    a, b = l[:mid], l[mid:]
    return merge_two_lists(merge_sort(a), merge_sort(b))

##############################
def merging(a, b):
    if not len(a) or not len(b):
        c = a + b
    elif a[0] <= b[0]:
        c = [a[0]] + merging(a[1:], b)
    else:
        c = [b[0]] + merging(a, b[1:])
    return c


def merge_sort(l):
    if len(l) <= 1:
        return l
    return merging(merge_sort(l[:len(l) // 2]), merge_sort(l[len(l) // 2:]))

###########
def merging(a, b):
    if a == [] or b == []:
        return a + b
    elif a[0] <= b[0]:
        return [a[0]] + merging(a[1:], b)
    else:
        return [b[0]] + merging(a, b[1:])

def merge_sort(l):
    if len(l) <= 1:
        return l
    return merging(merge_sort(l[:len(l) // 2]), merge_sort(l[len(l) // 2:]))

l = [8, 11, -6, 3, 0, 1]
print(*merge_sort(l))


#7.8 Анонимные (lambda) функции
#Подвиг 3. Объявите анонимную (лямбда) функцию с двумя параметрами для деления одного целого числа на другое.
# Если происходит деление на ноль, то функция должна возвращать значение None, иначе - результат деления.

get_div=lambda x,y:x/y if y else None
print(get_div(6,0))


#езультатом логического выражения будет значение подвыражения, которое проверялось последним в процессе ленивого
# вычисления.Причем подвыражение может быть любым: логическим или арифметическим или даже сложением строк и
# результат будет равен значению этого подвыражения, т.е. он не обязательно будет булевым значением!
# например (b or None), почему функция выбирает None, если b == 0, а не ноль?
# Если b == 0 значит в булевом эквиваленте это будет False. В этом случае, по правилам ленивого вычисления,
# оператор or должен проверить свой операнд справа (это None). None в булевом эквиваленте всегда даёт False,
# значит все выражение в круглых скобочках дает False: False or False = False.
# Дальше в игру вступает логический оператор and. Но, по правилам ленивого выполнения, он уже не будет проверять
# свой правый операнд, потому что независимо от значения последнего, все выражение все равно будет False, так как
# его левый операнд уже - False. Далее идет самое необычное, значением всего выражения будет не вычисленное булево
# значение (False), как это происходит в дргуих ЯП, а это будет значение последнего проверенного подвыражения!
# Этим подвыражением было None, значит оно и вернется в качестве результата. Точно так же, при ненулевом значении b,
# булево значение в круглых скобочках будет True, тогда оператор and вынужден будет проверит свой правый операнд.
# Тут уже даже не важно каким будет результат деления a / b и даст ли он False или True! Важно лишь то,
# что деление выполнялось последним и значит его значение и будет возвращено! Иная картина была в первом решении,
# там было действительно важно каким будет результат деления a / b, потому что в случае нулевого значения
# выполнилось бы or None.
get_div = lambda a, b: (b or None) and a / b

#Подвиг 4. Объявите анонимную (лямбда) функцию для вычисления модуля числа (то есть, отрицательные числа нужно
# делать положительными). Вызовите эту функцию для введенного числа x:

func = lambda y: abs(y)
x = float(input())
print(func(x))


func=lambda x:x if x>0 else (-x)
x = float(input())
print(func(x))

#Подвиг 5. Объявите анонимную (лямбда) функцию для определения вхождения в переданную ей строку фрагмента "ra".
# То есть, функция должна возвращать True, если такой фрагмент присутствует в строке и False - в противном случае.
func=lambda x:True if 'ra' in x else False
s = input()
print(func(s))

func=lambda x: 'ra' in x

print((lambda x:  'ra' in x)(input()))

func=lambda s,x='ra': x in s



#Подвиг 6. В программе задана функция filter_lst (см. программу ниже), которая отбирает элементы, переданного ей
# итерируемого объекта и возвращает сформированный кортеж значений.
# На вход программы поступает список целых чисел, записанных в одну строчку через пробел. Вызовите функцию
# filter_lst для формирования:
# - кортежа из всех значений входного списка (передается в параметр it);
# - кортежа только из отрицательных чисел;
# - кортежа только из неотрицательных чисел (то есть, включая и 0);
# - кортежа из чисел в диапазоне [3; 5]
# Каждый результат работы функции следует отображать с новой строки командой:
# print(*lst)
# где lst - список на возвращенный функцией filter_lst. Для отбора нужных значений формальному параметру key
# следует передавать соответствующие определения анонимной функции.


def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)

    return res


# l = list(map(int, input().split()))
l=[int(i) for i in input().split()]
l = [5, 4, -3, 4, 5, -24, -6, 9, 0]
lst = filter_lst(l, lambda x: x or x==0)
print(*lst)
lst = filter_lst(l, lambda x: x < 0)
print(*lst)
lst = filter_lst(l, lambda x: x >= 0)
print(*lst)
lst = filter_lst(l, lambda x: x > 2 and x < 6)
#lst = filter_lst(l, lambda x:3<=x<=5)
print(*lst)

#############################################
def filter_lst(it, key):
    print(*it)
    for i in key:
        print(*filter(i, it))


l = [5, 4, -3, 4, 5, -24, -6, 9, 0]
filter_lst(l, key=[lambda x: x < 0, lambda x: x >= 0, lambda x: 3 <= x <= 5])
#######################

filter_lst = lambda it, key=None: tuple(it if key is None else filter(key, it))
lst = [5, 4, -3, 4, 5, -24, -6, 9, 0]
for i in (None, lambda x: x < 0, lambda x: x >= 0, lambda x: 2 < x < 6):
    print(*filter_lst(lst, key=i))

#######################################
def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)

    return res

lst = [5, 4, -3, 4, 5, -24, -6, 9, 0]
key = [None, lambda a: a < 0, lambda a: a >= 0, lambda a: a >= 3 and a <= 5]
for i in key:
    (lambda x: print(*x))  (filter_lst(lst, i))  # (lst,key=i)
    #(lambda x:print(x))(None)



############################################
#7.9 Области видимости. Ключевые слова global и nonlocal ###############
#Подвиг 3. Имеется программа (см. листинг ниже), где читается глобальная переменная WIDTH (из входного потока) и
# функция с именем func1. Допишите в теле функции команду, которая бы позволяла изменять глобальную переменную WIDTH.

WIDTH = int(input())
def func1():
    global WIDTH
    WIDTH += 1
    return WIDTH

print(func1())

#Подвиг 4. Имеется программа (см. листинг ниже). Необходимо в теле функции func2 дописать команду, которая бы меняла
# значение уже существующей переменной msg, объявленной в функции func1.

def func1():
    msg = input()
    def func2():
        nonlocal msg
        msg = input()
        print(msg)
    func2()
    print(msg)
func1()

#Подвиг 5. Объявите функцию с именем create_global, которая имеет, следующую сигнатуру:
# def create_global(x): ...
# Эта функция должна создавать глобальную переменную с именем TOTAL и присваивать ей значение x.

def create_global(x):
    global TOTAL
    TOTAL = x
    return TOTAL

print(create_global(3))
print(TOTAL)
##################
def create_global(x):
    globals()['TOTAL'] = x

##################
###################    7.10 Замыкания в Python. Вложенные функции
def counter(start=0):
    def step():
        nonlocal start # для использования start из counter()
        #локальные переменные из другой связанной области видимости можно спокойно использовать, но только для
        # считывания информации, если же мы собираемся их менять, т.е. применять оператор присваивания, то нужно перед
        # этим указать nonlocal, иначе, будет создана новая переменная в текущей области видимости
        start += 1
        return start

    return step

c1 = counter(10)
c2 = counter()

[print(c1(), c2()) for _ in '...'] #строка  это коллекция. Цикл for перебирает элементы коллекций.
                           # В данном случае у нас три ".", т.е. 3 элемента, значение которых ".", т.е. три итерации.
# 11 1
# 12 2
# 13 3

##################
def strip_string(strip_chars=' '):
    def do_strip(string):
        return string.strip(strip_chars)

    return do_strip


strip1 = strip_string()
strip2 = strip_string(" !?,.;")

print(strip1(" hello python!..  "))
print(strip2(" hello python!..  "))
hello
python!..
hello
python



##################
#Подвиг 1. Используя замыкания функций, определите вложенную функцию, которая бы увеличивала значение переданного
# параметра на 5 и возвращала бы вычисленный результат.
def counter_add():
    def func(x):
        cnt = x + 5
        return cnt
    return func

k = int(input())
cnt = counter_add()
print(cnt(k))


def counter_add(x):
    def func():
        #nonlocal x
        cnt = x + 5
        return cnt
    return func

k = int(input())
cnt = counter_add(k)
print(cnt())
##################
#Подвиг 2. Используя замыкания функций, объявите внутреннюю функцию, которая увеличивает значение своего
# аргумента на некоторую величину n - параметр внешней функции
def counter_add(n):
    def func(k):

        return n +k

    return func
k = 5
cnt = counter_add(2)
print(cnt(k))

##################
#Подвиг 3. Используя замыкания функций, объявите внутреннюю функцию, которая заключает в тег h1 строку s (s - строка,
# параметр внутренней функции). Далее, на вход программы поступает строка и ее нужно поместить в тег h1 с помощью
# реализованного замыкания.
def out(tag='h1'):
    def in_func(s):
        #s1='<h1>'+s+'</h1>'
        return f'<{tag}>{s}</{tag}>'
    return in_func
s='Bala'
print(out()(s))

##################
#Подвиг 4. Используя замыкания функций, объявите внутреннюю функцию, которая заключает строку s (s - строка, параметр
# внутренней функции) в произвольный тег, содержащийся в переменной tag - параметре внешней функции.
# Далее, на вход программы поступают две строки: первая с тегом, вторая с некоторым содержимым. Вторую строку нужно
# поместить в тег из первой строки с помощью реализованного замыкания.
def out(tag):
    def in_func(s):
        return f'<{tag}>{s}</{tag}>'
    return in_func
s1 = 'div'
s2 = 'Балакирев'

print(out(s1)(s2)) #<div>Балакирев</div>
#или так
ch=out(s1)
print(ch(s2)) #<div>Балакирев</div>
##################
#Подвиг 5. Используя замыкания функций, объявите внутреннюю функцию, которая преобразует строку из списка целых чисел,
# записанных через пробел, либо в список, либо в кортеж. Тип коллекции определяется параметром tp внешней функции.
# Если tp = 'list', то используется список, иначе (при другом значении) - кортеж.Далее, на вход программы поступают
# две строки: первая - это значение для параметра tp; вторая - список целых чисел, записанных через пробел. С помощью
# реализованного замыкания преобразовать эти данные в соответствующую коллекцию
def out(tp):
    def in_func(s):
        if tp == 'list':
            #return list(map(int, s.split()))
            return [int(i) for i in s.split()]
        else:
            #return tuple(map(int, s.split()))
            return tuple(int(i) for i in s.split())
    return in_func

val = 'list'
s = input()
ch = out(tp=val)
lst = ch(s)  # [-5, 6, 8, 11, 0, 111, -456, 3]
print(lst)

##################
def parse(tp='list'):
    def inner(s):
        return (tuple, list)[tp == 'list'](map(int, s.split()))
    return inner

pr = parse(input())
print(pr(input()))






##################  7.11 Декораторы функций ######################
#универсальный шаблон для декораторов.

def decorator(func):  # Сюда передаём функцию которую нужно декорировать
    def wrapper(*args, **kwargs):  # Сюда передаём аргументы декорированной функции
        print(f'{func.__name__} started')  # декорирующие действия 1
        result = func(*args, **kwargs)  # *args -чтобы работать с разным кол-вом аргументов
        print(f'{func.__name__} finished')  # декорирующие действия 2
        return result  # возвращаем результат

    return wrapper  # передаём ссылку на вложенную функцию

@decorator  # сахар для вызова декоратора (навешиваем декоратор)
def summ(a, b):  # функция которую нужно декорировать в этот момент: summ = wrapper
    return a + b
print(summ(2, 3))

#Подвиг 1. Объявите функцию с именем get_sq, которая вычисляет площадь прямоугольника по двум параметрам: width
# и height - ширина и высота прямоугольника. И возвращает результат (сама ничего на экран не выводит).
# То есть, функция имеет сигнатуру:def get_sq(width, height): ...Определите декоратор func_show для этой функции,
# который отображает результат на экране в виде строки (без кавычек):"Площадь прямоугольника: <значение>"

width, height = [int(input()) for _ in '12']
# height=int(input())
def func_show(func):
    def wrapper(*args):
        print(f'Площадь прямоугольника: {func(*args)}')
    return wrapper

@func_show
def get_sq(width,height):
    return width * height

get_sq(width, height)

#get_sq=func_show(get_sq)
#get_sq(width,height)

#get_sq=func_show(get_sq)(width,height)
##################
#Подвиг 2. На вход программы поступает строка с названиями пунктов меню, записанные в одну строчку через
# пробел. Необходимо задать функцию с именем get_menu, которая преобразует эту строку в список из слов и
# возвращает этот список. Сигнатура функции, следующая:def get_menu(s): ...
# Определите декоратор для этой функции с именем show_menu, который отображает список на экран в формате:
# 1. Пункт_1
# 2. Пункт_1

s = input()
def show_menu(func):
    def wrapper(*args, **kwargs):
        j = 0
        for i in func(*args,**kwargs):
            print(f'{(j := j + 1)}.{i}')

    return wrapper

@show_menu
def get_menu(s):
    #lst = [i for i in s.split(' ')]
    #return lst
    return s.split()

get_menu(s)
####################
def show_menu(func):
    def wrapper(*args, **kwargs):
        j = 1
        for i in func(*args,**kwargs):
            print(f'{(j)}.{i}')
            j+=1
    return wrapper
#############
def show_menu(func):
    def wrapper(*args, **kwargs):
        j=0
        for i in func(*args):
            j=j+1
            print(f'{j}. {i}')
##################################
def show_menu(func):
    def wrapper(*args, **kwargs):
        for i,val in enumerate(func(*args),start=1):
            print(f'{i}. {val}')

##############################################################
#Подвиг 3. На вход программы поступает строка из целых чисел, записанных через пробел.
# Напишите функцию get_list, которая преобразовывает эту строку в список из целых чисел и
# возвращает его. Определите декоратор для этой функции, который сортирует список чисел по
# возрастанию. Результат сортировки должен возвращаться при вызове декоратора.
s = input()
def dec_sort(func):
    def wrapper(*args):
        return sorted(func(*args))

    return wrapper

@dec_sort
def get_list(s):
    return [int(i) for i in s.split()]
    #return list(map(int,s.split()))

lst = get_list(s)
print(*lst)
##############
def dec_sort(func):
    return lambda *args,**kwargs:func(*args,**kwargs)
################################
def sort_list(get_list):
    def sort_s(s=list):
        return sorted(get_list(s))

    return sort_s

@sort_list
def get_list(s):
    return map(int, s.split())

lst = get_list(input())
print(*lst)
################################
#Подвиг 4. Вводятся две строки из слов (слова записаны через пробел). Объявите функцию,
# которая преобразовывает эти две строки в два списка слов и возвращает эти списки.
# Определите декоратор для этой функции, который из двух списков формирует словарь, в
# котором ключами являются слова из первого списка, а значениями - соответствующие
# элементы из второго списка. Полученный словарь должен возвращаться при вызове декоратора
# Примените декоратор к первой функции и вызовите ее для введенных строк
s = 'house river tree car'
ss = 'дом река дерево машина'

def dec_dict(func):
    def wrapper(*args, **kwargs):
        print(*func(*args))  # ['house', 'river', 'tree', 'car'] ['дом', 'река', 'дерево', 'машина']
        return dict(zip(*func(*args)))
    return wrapper

@dec_dict
def get_lst(s, ss):
    lst1 = [i for i in s.split()]
    lst2 = [i for i in ss.split()]
    # print(*zip(lst1,lst2))
    return lst1, lst2

d = get_lst(s, ss)
# print(d) #{'house': 'дом', 'river': 'река', 'tree': 'дерево', 'car': 'машина'}
print(*sorted(d.items()))  # ('car', 'машина') ('house', 'дом') ('river', 'река') ('tree', 'дерево')
################################
@dec_dict
def get_lst(*args):
    return [i.split() for i in args]
################################
def dec_dict(func):
    return lambda *args:dict(zip(*func(*args)))

@dec_dict
def get_lst(*args):
    return list(map(str.split, args))
################################
def into_dict(func):
    def wrapper(*args, **kwargs):# объявляем функцию которая будет "оборачивать" func
        tp_of_lists = func(*args, **kwargs)# сохраняем кортеж состоящий из двух списков
        d={}#объявляем словарь
        for i in range(len(tp_of_lists[0])):#пробигаем по i по всем элементам одного из списков
            d[tp_of_lists[0][i]]=tp_of_lists[1][i]# кладём в i-й ключ словаря из списка 0 кладём i-e значение из списка 1
        return d# возвращаем словарь
    return wrapper# возвращаем ссылку на обёртку
#Есть два списка, нулевой список содержит ключи, а первый содержит значения. Он пробегает i по длине нулевого списка
# и добавляет в словарь по ключу i из нулевого списка значение i из первого списка

################################
def get_dict(func):
    def wrapper(*args, **kwargs):
        sp1, sp2 = func(*args, **kwargs)
        return {sp1[i]:sp2[i] for i in range(len(sp1))}
    return wrapper
################################
def dec_dict(func):
    def wrapper(*args, **kwargs):
        keys,val=func(*args)
        return {keys[i]:val[i] for i in range(len(keys))}
################################
# без zip с итератором
def dict_it(func):
    """    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/stepik.org/decorators.py    """
    def wrapper(*args):
        keys, val = func(*args)
        it_val = iter(val)  # получаем списки из ф-ции, значения преобразуем в итератор
        return {i: next(it_val) for i in keys}  # формируем список генератором, итерируя values
    return wrapper

@dict_it
def get_lists(*args):  # объявление функции
    return [i.split() for i in args]  # преобразование параметров в списки и возврат

# help(dict_it)
vol1 = 'house river tree car'  # ввод с клавиатуры первой строки
vol2 = 'дом река дерево машина'  # ввод с клавиатуры первой строки
# vol1 = 'house river tree car'       # тестовый ввод первой строки
# vol2 = 'дом река дерево машина'     # тестовый ввод второй строки
d = get_lists(vol1, vol2)  # запуск функции, получение d
print(*sorted(d.items()))  # вывод результата согласно заданию

################################
#Подвиг 5. Объявите функцию, которая принимает строку на кириллице и преобразовывает ее в латиницу, используя
# следующий словарь для замены русских букв на соответствующее латинское написание:
# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
# 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
# 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
# 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
# Функция должна возвращать преобразованную строку. Замены делать без учета регистра (исходную строку перевести в
# нижний регистр - малые буквы). Все небуквенные символы ": ;.,_" превращать в символ '-' (дефиса).
# Определите декоратор для этой функции, который несколько подряд идущих дефисов, превращает в один дефис.
# Полученная строка должна возвращаться при вызове декоратора. (Сам декоратор на экран ничего выводить не должен).
s = 'Pyth ;.,_on - это круто!'.lower()

def dec_defis(func):
    def wrapper(*args):
        #1 var
        res = func(*args)
        while res.count('--'): # while '--' in res:
            res = res.replace('--', '-')
        #2 var
        #return ''.join(func(*args).split('--')) #split разбиваем в список только где по два дефиса '--'
        #3 var
        #return '-'.join(filter(None, func(*args).split('-')))
        #Если фильтрующая функция func вернет None, то считается что требуется применить тождественное действие
        # (item for item in iterable if item), таким образом все элементы, оцениваемые как False будут отфильтрованы
        #return '-'.join(i for i in func(*args).split('-') if i)
        #if i - чтобы отсеять пустые эл в списке после того как
        #воспольз. pyth-----on---eto-kruto!'.split('-') получили ['pyth', '', '', '', '', 'on', '', '', 'eto', 'kruto!']
        return res
    return wrapper

@dec_defis
def kiril(s,**kwargs):
    r = ''.join(t[i] if i in t else i for i in s)
    # r = r.replace('_', '-').replace(':', '-').replace(';', '-').replace(' ', '-').replace('.', '-').replace(',', '-')
    s = ''.join('-' if i in ': ;.,_' else i for i in r)
    return s

res = kiril(s)
print(res)
################################
@dec_defis
def kiril(s,**kwargs):
    st=''
    for i in s:
        if i in t:
            st+=t[i]
        elif i in ": ;.,_":
            st+='-'
        else:
            st+=i
    return st
################################
def dec_defis(func):
    def wrapper(*args):
        res=func(*args).replace('-',' ').split() #['pyth', '_on', 'eto', 'kruto!']
        return '-'.join(res)
    return wrapper

@dec_defis
def kiril(s, **kwargs):
    lst = [t.get(i, i) if i not in [":", ";", '.', ',', ' '] else '-' for i in s]  # dict.get(key[, default])
    return ''.join(lst)
################################
#добавляем знаки препинания ': ;.,_' в словарь dict.fromkeys(': ;.,_', '-') распаковкой словарей
# методы строк maketrans и translate для шифрования/дешифрования
# регулярка для удаления лишних дефисов
# лямда функция в качестве вложенной функции декоратора.
import re

def hyphenator(func):
    return lambda *args, **kwards: re.sub(r'-+', '-', func(*args, **kwards))

@hyphenator
def transliterate(s):
    return s.lower().translate(str.maketrans({**t, **dict.fromkeys(': ;.,_', '-')}))

print(transliterate(s))
################################
import re
from re import sub

def unite_hyphen(func):
    return lambda *args: re.sub(r'[-]+', '-', func(*args))

@unite_hyphen
def translate(s: str):
    return ''.join(['-' if i in ': ;.,_' else t.get(i, i) for i in s])

print(translate(s))

################################
def decor(func):
    def wrapper(*args):
        return func(*args).replace("--", "") #заменять 2 дефиса на пустоту 2 дефиса на пустоту, но вот незадача
        # если подать вам на вход четное число, то вместо ожидаемого одного дефиса получаем пустоту, как я понял по условию это не является верным.
    return wrapper

@decor
def asd(s):
    return ''.join([t[i] if i in t else '-' if i in ': ;.,_' else i for i in s])

print(asd(s))
################################
@strip_excess
def invert_english(s, t):
    items = ": ;.,_"  # строка с доп сиволами из задания
    t = {**t, **dict.fromkeys(items, "-")}  # items для всех ключей : ;.,_ со знач '-' дополнена в словарь t
    return "".join([t[i] if i in t else i for i in s])  # возвращаем преобразованную строку

################################
'Pyth------on---это-круто!'.replace('-', '').split()
Out[3]: ['Pythonэтокруто!']

'Pyth------on---это-круто!'.replace('-', ' ').split(' ')
Out[4]: ['Pyth', '', '', '', '', '', 'on', '', '', 'это', 'круто!']

'Pyth------on---это-круто!'.replace('-', ' ').split()
Out[5]: ['Pyth', 'on', 'это', 'круто!']
#Если sep не указан или задан None, применяется другой алгоритм разбиения:
# Последовательности пробелов рассматриваются как один разделитель и если строка имеет начальные или конечные
# пробелы,то результат не будет содержать пустых строк в начале или конце.
################################
import re
s = 'Python ;.,_on - Это круто!'
def dec_defis(func):
    def wrapper(*args, **kwargs):
        return re.sub(r'-+', '-', func(*args, **kwargs))
    return wrapper

@dec_defis
def kiril(*args, **kwargs):
    print(args)  # ('python ;.,_on - это круто!',)
    print(*args)  # python ;.,_on - это круто!
    for i in args:
        print(f':', *i)  # : p y t h o n   ; . , _ o n   -   э т о   к р у т о ! - распаковка ч/з пробел
        #print(f':', i)  # : python ;.,_on - это круто!

    return re.sub(kwargs['smb'], kwargs['sep'], ''.join(t.get(i, i) for i in s))
    # kwargs['smb'] извлечение значения из словаря kwargs

f = kiril(s.lower(), smb='[: ;.,_]', sep='-')  # smb='[: ;.,_]', sep='-' всё передаём в kwargs
print(f)
################################
def replace_dashes(func):
    return lambda *args, sep='-': re.sub(f'{sep}+', sep, func(*args, sep=sep))
# для чего вы прописываете sep=sep в func(*args, sep=sep) если и без него работает, зачем он здесь вообще нужен?
# чтобы можно было вызвать функцию transliterate(string, sep='!') с другим разделителем
@replace_dashes
def transliterate(string, smb='[: ;.,_-]', sep='-'):
    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e',
         'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
         'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
         'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
         'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
    return re.sub(smb, sep, ''.join(t.get(s, s) for s in string.lower()))

print(transliterate(input()))
#################################
def dec_defis(func):
    def wrapper(*args, **kwargs):
        return re.sub(r'-+', '-', func(*args, **kwargs))
    return wrapper

@dec_defis
def kiril(**kwargs):
    return re.sub(kwargs['smb'], kwargs['sep'], ''.join(t.get(i, i) for i in kwargs['ss'].lower()))
    # kwargs['smb'] извлечение значения из словаря kwargs

s = 'Python ;.,_on - Это круто!'
f = kiril(ss=s, smb='[: ;.,_]', sep='-')  #ss=s, smb='[: ;.,_]', sep='-' всё передаём в kwargs
print(f)
#####################################
@dec_defis
def kiril(s):
    l=''
    for i in s.lower():
        if i in t:
            l+=t[i]
        elif i in ': ;.,_':
            l+='-'
        else:
            l+=i
    return l
################################
@dec_defis
def kiril(s):
    l=''
    for i in s.lower():
        if i in t:
            l+=t[i]
        elif i in ': ;.,_':
            l+='-'
        else:
            l+=i
    return l
################################ 7.12 Передача аргументов декораторам ##########
#Подвиг 1. Вводится строка целых чисел через пробел. Напишите функцию, которая преобразовывает эту строку в список
# чисел и возвращает их сумму.Определите декоратор для этой функции, который имеет один параметр start -
# начальное значение суммы.Примените декоратор со значением start=5 к функции и вызовите декорированную
# функцию для введенной строки s:
s = '5 6 3 6 -4 6 -1'
def dec_start(start):
    def decor(func):
        def wrapper(*args):
            return func(*args) + start
        return wrapper
    return decor

@dec_start(5)
def transformation(s):
    return sum([int(_) for _ in s.split()])
    #return sum(list(map(int,s.split())))

print(transformation(s))

################################
#Подвиг 2. Объявите функцию, которая возвращает переданную ей строку в нижнем регистре (с малыми буквами).
# Определите декоратор для этой функции, который имеет один параметр tag, определяющий строку с названием тега и
# начальным значением "h1". Этот декоратор должен заключать возвращенную функцией строку в тег tag и возвращать
# результат. Пример заключения строки "python" в тег h1: <h1>python</h1>
s = 'Декораторы - это классно!'
from functools import wraps

def dec_tag(tag):
    def decor(func):
        @wraps(func)
        def wrapper(*args):
            return f'<{tag}>{func(*args)}</{tag}>'
        return wrapper
    return decor

@dec_tag("div")
def transfor(s):
    return s.lower()

print(transfor(s))
################################################################
def dec_tag(tag):
    return lambda func: lambda *args: f'<{tag}>{func(*args)}</{tag}>'

@dec_tag("div")
def transfor(s):
    return s.lower()

print(transfor(s))
################################################################
dec = lambda tag='h1': lambda f: lambda a: f'<{tag}>{f(a)}</{tag}>'

@dec('div')
def su(s):
    return s.lower()
print(su(input()))
################################################################
#через класс - читабельнее
from functools import wraps

def set_tag(tag='h1'):  # декоратор через функции
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return f'<{tag}>{func(*args, **kwargs)}</{tag}>'
        return wrapper
    return inner

class SetTag:  # декоратор через класс
    def __init__(self, tag='h1'):
        self._tag = tag

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return f'<{self._tag}>{func(*args, **kwargs)}</{self._tag}>'
        return wrapper

@SetTag('div')
def to_lower(s):
    return s.lower()
print(to_lower(input()))
################################################################
#Подвиг 3. Объявите функцию, которая принимает строку на кириллице и преобразовывает ее в латиницу, используя следующий
# словарь для замены русских букв на соответствующее латинское написание:
# Функция должна возвращать преобразованную строку. Замены делать без учета регистра (исходную строку перевести в
# нижний регистр - малые буквы). Определите декоратор с параметром chars и начальным значением " !?", который данные
# символы преобразует в символ "-" и, кроме того, все подряд идущие дефисы (например, "--" или "---") приводит к
# одному дефису. Полученный результат должен возвращаться в виде строки.Примените декоратор с аргументом
# chars="?!:;,. " к функции и вызовите декорированную функцию для введенной строки s:
s = '?Декораторы - это круто!!'
def dec_tag(tag):
    def decor(func):
        def wrapper(*args):
            # print(tag, func(*args))
            s = ''.join(['-' if i in tag else i for i in func(*args)])
            while s.count('--'):
                s = s.replace('--', '-')
            return s
        return wrapper
    return decor

@dec_tag(' !?')
def translate(s):
    return ''.join([t[i] if i in t else i for i in s.lower()])
    #return ''.join([t.get(i, i) for i in s.lower()])

print(translate(s))
################################################################
import re
def code(s, t):
    return s.translate(str.maketrans(t)) # метод str.maketrans() создает и возвращает таблицу преобразования
                                        # символов, используемую методом строки str.translate().
def punctuator(chars='!?'):
    def hyphenator(func):
        def wrapper(*args, **kwards):
            return re.sub(r'-+', '-', code(func(*args, **kwards), dict.fromkeys(chars, '-')))
            #dict.fromkeys(chars,'-') тут второй аргумент функции  code. Это словарь, по которому символы
            # пунктуации будут заменены на символ '-'
        return wrapper
    return hyphenator

@punctuator(chars='?!:;,. ')
def transliterator(s):
    return code(s.lower(), t)

print(transliterator(s))
################################################################
t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
s = '??Декораторы - это круто!!'
import re
def punctuator(chars='!?'):
    def hyphenator(func):
        def wrapper(*args):
            #print(args)  # ('?декораторы - это круто!!',)
            t = dict.fromkeys(chars, '-')  # создаём словарь со спец символами с ключами по умолчанию
            # {'?': '-', '!': '-', ':': '-', ';': '-', ',': '-', '.': '-', ' ': '-'}
            #t1 = {**t, **tt}  # Объединение или слияние двух словарей в один новый словарь чтобы не изменять словарь t
            return re.sub(r'-+', '-', func(t, *args))
        return wrapper
    return hyphenator

@punctuator(chars='?!:;,. ')
def transliterator(w, s):  # w ссылка на словарь t1 кот был создан в декораторе при слиянии 2-х словарей
    return s.lower().translate(str.maketrans(w))  # str.translate(str.maketrans(s,t))# метод str.maketrans() создает
    # и возвращает таблицу преобразования символов, используемую методом строки str.translate().

print(transliterator(s))
################################################################
s = '?Декораторы - это круто!!'
def dec_tag(tag):
    def decor(func):
        def wrapper(*args):
            s=''
            for i in func(*args):
                s+='-' if i in tag else i
                s=s.replace('--','-')
            return s
        return wrapper
    return decor
#@dec_tag(' !?') # var 2
def translate(s):
    return ''.join(t.get(i,i)for i in s.lower()) #Значение по умолчанию для отсутствующих ключей в словаре.

tag=dec_tag(' !?')(translate)(s)
print(tag)
#print(translate(s)) # var 2
################################################################
#Подвиг 4. Объявите функцию с именем get_list и следующим описанием в теле функции
# '''Функция для формирования списка целых значений'''
# Сама функция должна формировать и возвращать список целых чисел, который поступает на ее вход в виде строки из
# целых чисел, записанных через пробел.# Определите декоратор, который выполняет суммирование значений из списка
# этой функции и возвращает результат.Внутри декоратора декорируйте переданную функцию get_list с помощью команды
# @wraps (не забудьте сделать импорт: from functools import wraps). Такое декорирование необходимо, чтобы исходная
# функция get_list сохраняла свои локальные свойства: __name__ и __doc__.

from functools import wraps
s = '1 2 3 4 5'
def dec_sum(func):
    @wraps(func)  # необходимо, чтобы исходная функция get_list сохраняла свои локальные свойства: __name__ и __doc__.
    def wrapper(*args):
        return sum(func(*args))
    return wrapper

@dec_sum
def get_list(s):
    """    Функция для формирования списка целых значений """
    return [int(i) for i in s.split()]

help(get_list)
print(get_list(s))
print(get_list.__name__)
print(get_list.__doc__)
################################################################

################################################################

################################################################

################################################################

################################



























