#8 основных типов данных
# 1) int - целый числовой тип данных:
#    a) float - числа с плавающей точкой
#    b) complex - числа с буквенным выражением(12345123n)
# 2) str - строковый тип данных - "Строка"
# 3) bool - булевый тип данных/логический (True/False)
# 4) list - список []
# 5) tuple - кортеж/неизменяемый список ()
# 6) set - множество {}
# 7) dict - словарь {}
# 8) None Type - тип данных для обозначения отсутсвия значения(None)


# Изменяемые (mutable):
# list
# dict
# set


#print("Hello World") #print()  функция для вывода информации в терминал
# name = input("Введите ваше имя: ")
# print("Привет," + name)

# print(" Привет\n как дела")


# str1 = 'Hello'
# str2 = 'world'
# print(str1+str2)

# frog = 'Quak'
# print(frog * 3) #QuakQuakQuak


""" Функции и методы строк """

greeting = "Добрый вечер"
#print(len(greeting))
#len(x) - возвращает количество элементов

print(dir(greeting))
#dir (x) - возврвщает список методов переданного объекта


# Метод - функция, принадлежащая определенному типу данных, и может быть вызвана только через объект

my_str = 'Hello#world'

print(my_str.lower())
print(my_str.upper())
print(my_str.replace('#', ' '))
print(my_str.split('#')) #делит строку по разделителю и возвращает список

my_str2 = '   hello world   ' 

my_str2.title() #Hello World
my_str2.capitalize() #Hello world
my_str2.count("l") #3
print(my_str2.strip()) #удаляет лишние проблемы
my_str2.lstrip()
my_str2.rstrip()

print(my_str2.strip('!'))


my_str3 = 'My New String'


my_str3. isalpha() #True
my_str3.isdigit() #False
my_str3.isalnum() #False
my_str3.startswith('M') #True
my_str3.endswith('M') #False



# in

my_str4 = 'Hello world'

print('Hello' in my_str4)

# 'Hello' in my_str4 # True

name = input('Имя:')
party = input('Вечеринка: ')

invite1 = 'Дорогой %s, приглашаем тебя на %s' % (name, party)
print(invite1)
invite2 = 'Дорогой {a1}, приглашаем тебя на {b2}'.format (a1 = name, b2 = party)
print(invite2)


invite3 = f'Дорогой{name}, приглашаем тебя на {party}'
print(invite3)


string = 'Python'

start = 2
stop = 5
step = 2
print(string[4])
print(string[start:stop:step])

