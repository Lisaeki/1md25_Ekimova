from PIL import Image, ImageFilter, ImageDraw, ImageOps

def n1():
    image = Image.open("4_8.png")
    image.show()
    print(f"Размер: {image.size}")
    print(f"Формат: {image.format}")
    print(f"Цветовая модель: {image.mode}")
n1()

def n2():
    image = Image.open("4_8.png")
    red = image.reduce(3)
    s = ImageOps.mirror(red)
    f = ImageOps.flip(s)
    f.show()
    f.save("4_99.png")
n2()

def n3():
    images = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
    for img in images:
        image = Image.open(img)
        imgef = image.filter(ImageFilter.SHARPEN)
        imgef.save("filtr.png" + str(img))
n3()

def n4():
    images = "photo.jpg"
    def watermark_text(inp, out, text, pos):
        photo = Image.open(inp)
        drawing = ImageDraw.Draw(photo)
        photo.show()
        photo.save(out)

    if __name__ == '__main__':
        img = 'photka.jpg'
        watermark_text(img, "photka_watermarked.jpg", text = 'Text', pos=(0,0))
n4()