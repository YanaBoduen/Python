def Delenie(a, b):
    if b==0:
        print("Не возможно поделить на ноль!")
    else:
        return (a/b)

def Info(name, surname, year, town, mail):
    print(name, surname, "родилась в ", year, 'году. Живет в городе', town, 'и имеет электронную почту:', mail)

def my_func(a, b, c):
    alis = [a, b, c]
    k = max(alis)
    alis.remove(k)
    return k + max(alis)

def Stepen1(x, y):
    return(x**y)
    
def Stepen2(x, y):
    k = 1
    for i in range(y):
        k = k*x
    return k

def SumStrok(spis):
    a = list(spis.split())
    if '#' in a:
        a = a[:a.index('#')]
    a = map(int, a)
    return sum(a)
    
def Zaglav(text):
    return text.capitalize()
    

a, b = map(int, input("Введите два числа для деления через пробел: ").split())
print("Результат: ", Delenie(a, b))
ll = input()

Info("Яна", "Петрова", "2000", 'Москва', 'gg.mail')
ll = input()

a, b, c = map(int, input("Введите три числа через пробел: ").split())
ll = input()

x, y = map(int, input("Введите число и степень, в которую его надо возвести черз пробел: ").split())
print("Результат:", Stepen1(x, y), Stepen2(x, y))
ll = input()

while True:
    spis = input('Введите числа через пробел. Для завершения введите "#" ')
    print(SumStrok(spis))
    if '#' in spis:
        break
ll = input()

text = list(input('Введите строку: ').split())
for i in range(len(text)):
    text[i] = Zaglav(text[i])
print(' '.join(text))
