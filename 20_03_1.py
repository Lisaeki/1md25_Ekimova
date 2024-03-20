
def num1():
    s = int(input("Введите число: "))
    def n1(a):
        if a % 5 == 0:
            return "Число делится на 5!"
        else:
            return "Число не делится на 5."
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
                b = int(k) / 300
                return b
        except:
            return "ValueError"
    print(n2(k))
num2()

def num3():
    import datetime as DT
    l = input("Введите дату (dd/mm/yyyy): ")
    v = DT.datetime.strptime(l,'%d/%m/%Y').date()
    def n3(c):
        n = 
        print(n)
    print(n3(l))
num3()

# def num4():