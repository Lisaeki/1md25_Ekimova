k = ""
s = ""
while True:
    k = input("Введите слово: ")
    if k != "stop":
        complete = True
        s = s + " " + k
    elif k == "stop":
        complete = False
        break
print(s)
