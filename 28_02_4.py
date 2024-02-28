import random
w = 0
l = 0
while l < 3:
    a = random.randint(0, 20)
    b = random.randint(0, 20)
    k = int(input(f"{a} + {b}: "))
    if k == (a + b):
        w += 1
        complete = True
        print("Правильно!")
    elif k != (a + b):
        l += 1
        print("Ответ неверный")
        complete = False
print(f"Игра окончена. Правильных ответов: {w}")