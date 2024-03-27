def num1():
    import random
    k = []
    for i in range(5):
        k.append(random.randint(0, 10))
    n = int(input("Введите число: "))
    if n in k:
        print(k, n, "Поздравляю, Вы угадали число!")
    else:
        print(k, n, "Нет такого числа!")
num1()

def num2():
    import random
    s = []
    for x in range(10):
        s.append(random.randint(0, 20))
    s.sort()
    i = 0
    c = 0
    for i in s:
        if i == (i+1):
            c += 1
            i += 1
    print(c, s)
num2()

def num3():
    a = ("понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье")
    l = int(input("Сколько выходных на неделе вы хотите?"))
    s = a[-l:]
    n = 7 - l
    k = a[:n]
    print("Ващи выходные дни:", s)
    print("Ваши рабочие дни:" ,k)
num3()

def num4():
    import random
    a = ["Екимова", "Зотова", "Идрисова", "Бречалова", "Токарева", "Поспелова", "Гусева", "Анисимов", "Ахмадов", "Свириденко"]
    b = ["Иванов", "Петров", "Васильев", "Дмитриев", "Шишкин", "Филиппов", "Крылов", "Носов", "Щербаков", "Прохоров"]
    j = []
    h = []
    for i in range(5):
        for i in a:
            s = int(random.randint(0, 10))
            j.append(a[s])
    for o in range(5):
        for o in b:
            c = int(random.randint(0, 10))
            h.append(b[c])
    print(j)
num4()