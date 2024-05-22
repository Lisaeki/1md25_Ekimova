
def num1():
    s = int(input("Введите число: "))
    def n1(a):
        if a % 3 == 0:
            return "Число делится на 3!"
        else:
            return "Число не делится на 3."
    print(n1(s))
num1()

def num2():
    k = input("Введите число: ")
    def n2(b):
        try:
            k == int(k)
            if int(k) == 0:
                return "ZeroDivisionError"
            else:
                b = 100 / int(k)
                return b
        except:
            return "ValueError"
    print(n2(k))
num2()

def num3():
    import datetime as DT
    l = input("Введите дату (dd/mm/yyyy): ")
    v = DT.datetime.strptime(l,'%d/%m/%Y').date()
    n = str(v)
    day = n[-2:]
    month = n[-5:-3]
    year = n[2:4]
    if int(day) * int(month) == int(year):
        print("True")
    else:
        print("False")
num3()

def num4():
    u = 0
    n = 0
    b = 0
    m = input("Введите число: ")
    if int(len(m)) % 2 != 0:
        return False
    else:
        f = int(len(m)) // 2
        k = m[:f]
        s = m[f:]
        while u < f:
            n = n + int(m[u])
            u = u + 1
        i = f
        while i < (2*f):
            b = b + int(m[i])
            i = i + 1
    if n == b:
        print("Счастливый билет")
    else:
        print("Несчастливый билет")
num4()

