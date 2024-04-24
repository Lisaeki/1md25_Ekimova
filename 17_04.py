from PIL import Image, ImageFilter, ImageDraw, ImageOps, ImageFont

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
    images = "photo2.jpg"
    def watermark_text(input_image_path, output_image_path, text, pos):
        photo = Image.open(input_image_path)
        drawing = ImageDraw.Draw(photo)
        black = (3, 8, 12)
        drawing.text(pos, text, fill=black)
        photo.show()
        photo.save(output_image_path)

    if __name__ == '__main__':
        img = 'photo2.jpg'
        watermark_text(img, "photo2_watermarked.jpg", text = 'Squirrel', pos=(10,5))
n4()