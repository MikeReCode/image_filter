"""
*** Coursera Python 3 Programming Specialization - Color filter project  ***
"""

import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# read image and convert to RGB
# put any image in the same folder and incert the corect name and format
image = Image.open("images.png")
image = image.convert('RGB')
largo, alto = image.size
# build a list of 9 images which have different brightnesses
enhancer = ImageDraw.Draw(image)
images = []


# font = ImageFont.truetype("readonly/fanwood-webfont.ttf", 70)
def color_change(img, mr=1.0, mg=1.0, mb=1.0):
    ancho, alto = img.size
    img = img.copy()
    for px in range(ancho):
        for py in range(alto):
            r, g, b = img.getpixel((px, py))
            nr = int(r * mr)
            ng = int(g * mg)
            nb = int(b * mb)
            img.putpixel((px, py), (nr, ng, nb))
    return img


chan = 0
inc_r = 0.1
inc_g = 0.1
inc_b = 0.1
for i in range(1, 10):
    if inc_r <= 0.9:
        new = color_change(image, mr=inc_r)
        ImageDraw.Draw(new).line([(0, alto), (largo, alto)], fill="black", width=50)
        ImageDraw.Draw(new).text((0, alto - 20), "channel {} intensity {}".format(chan, inc_r), fill=(255, 255, 255))

        if chan == 2:
            chan = 0
        inc_r += 0.4
    elif inc_g <= 0.9:
        new = color_change(image, mg=inc_g)
        ImageDraw.Draw(new).line([(0, alto), (largo, alto)], fill="black", width=50)
        ImageDraw.Draw(new).text((0, alto - 20), "channel {} intensity {}".format(chan, inc_g), fill=(255, 255, 255))
        if chan == 2:
            chan = 0
        inc_g += 0.4
    else:
        new = color_change(image, mb=inc_b)
        ImageDraw.Draw(new).line([(0, alto), (largo, alto)], fill="black", width=50)
        ImageDraw.Draw(new).text((0, alto - 20), "channel {} intensity {}".format(chan, inc_b), fill=(255, 255, 255))
        if chan == 2:
            chan = 0
        inc_b += 0.4

    images.append(new)

# create a contact sheet from different brightnesses
first_image = images[0]
contact_sheet = PIL.Image.new(first_image.mode, (first_image.width * 3, first_image.height * 3))
x = 0
y = 0

for img in images:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y))
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x + first_image.width == contact_sheet.width:
        x = 0
        y = y + first_image.height
    else:
        x = x + first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width / 2), int(contact_sheet.height / 2)))

# To save the image , uncomment the next line and modify the output image name if you wish
# contact_sheet.save("output.png")
contact_sheet.show()
