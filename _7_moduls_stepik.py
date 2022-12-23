######### moduls ##########
from math import ceil
n=float(input())
print(ceil(n))

n=5.6
print(__import__('math').ceil(n)) #импорт библиотеки, вызываемый магическим (!) методом __import__

from math import floor as fl
n=8.11
print(fl(n))
#Подвиг 4. В программе имеется функция factorial (см. листинг). В начале программы (до определения функции)
# необходимо из модуля math импортировать функцию с тем же именем factorial, используя команду from, но так,
# чтобы они не "затирали" друг друга.Уже объявленную функцию не менять. Выполнять функции не нужно, только прописать
# импорт.
from math import factorial as fct
n=5
def factorial(n):
    p=1
    for i in range(1,n+1):
        p*=i
        print(p)
factorial(n)

print(fct(n))

from random import seed,randint
seed(1) #seed - сохраняет числа из random.randint постоянными, т.е если запустить цикл и выбирать цифры рандомно
# из промежутка, то перед каждым новым запуском программы цифры не изменятся.
print(randint(10, 50)) #Если запускать randint(10, 50) без seed, будут выходить разные числа, если использовать
# seed(1), то одинаковые.В seed тоже можно менять параметр, тогда будет другое "одинаковое" число
#при каждом запуске программы будете получать одни и те же псевдослучайные числа

from math import floor as fl, ceil as cl, pi
from random import seed,random as ss,rnd
ss(10)
print(round(rnd(), 2))


file=open('conspect.docx')
print(file.read())

try:
    f = open("abc.txt")
    r = f.read(1)
    f.close()
except FileNotFoundError:
    print("File Not Found")

with open("my_file.txt") as file:
    ...

try:
    with open("out.txt", "w") as file:
        file.write("Hello")
        file.write("Hello") #HelloHello
except:
    print("Ошибка при работе с файлом")


