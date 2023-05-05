from PIL import Image, ImageFilter

def n1():
        Filename = "art.jpg"
        with Image.open('art.jpg') as img:
            img.load()
        img.show()
        width, height = img.size

        format = img.format
        mode = img.mode
        print("Width:", width)
        print("Height:", height)
        print("Format:", format)
        print("Color Model:", mode)

n1()


def n2():
    img = Image.open('art.jpg')
    img.show()
    new = img.resize((img.width // 3, img.height // 3))
    new.save('new.png')
    con = img.rotate(120)
    con.save('new1.png')
    con = img.transpose(Image.Flip_left_right)
    con.save('new2.png')


n2()

def n3():
    name = ["1.jpg", "2.jpg", "3.jpg"]
    for file in name:
        with Image.open(file) as img:
            img.load()
            new1 = img.filter(ImageFilter.EMBOSS)
            new1.show()
            new1.save('new' + file)


n3()


def n4():
    image1 = Image.open("simv.png")
    new1 = image1.resize((image1.width // 4, image1.height // 4))
    img = Image.open("1.jpg")
    img.paste(new1)
    img.save("simv2.jpg")


n4()
