N = input("Введите слово: ")

for i in N:
    if i == "ф":
        print("Ого! Это редкое слово!")
        break
    else:
        print("Эх, это не очень редкое слово...")
        break