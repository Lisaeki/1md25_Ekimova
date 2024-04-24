from PIL import Image
def n1():
    image = Image.open("otk2.jpg")
    image.show()
    crop = image.crop((120, 115, 800, 800))
    crop.show()
    crop.save("otk2isp.jpg")
n1()

def n2():
    dictionary = {"Новый год":"", "новый год":"", "8 марта":"", "23 февраля":""}
    text = input("Введите название праздника: ")
n2()
