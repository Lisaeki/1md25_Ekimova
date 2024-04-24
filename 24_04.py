from PIL import Image
def n1():
    image = Image.open("otk2.jpg")
    image.show()
    crop = image.crop((120, 115, 800, 800))
    crop.show()
    crop.save("otk2isp.jpg")
n1()

def n2():
    dictionary = {"Новый год":"2024.jpg", "новый год":"2024.jpg", "8 марта":"8m.jpg", "23 февраля":"23f.jpg"}
    text = input("Введите название праздника: ")
    s = dictionary[str(text)]
    m = Image.open(s)
    m.show()
n2()

def n3():

n3()