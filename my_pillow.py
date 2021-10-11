import sys
from PIL import Image, ImageDraw, ImageFont

# Image.open('camaro.jpg').show()  #original image
with Image.open("camaro.jpg").convert("RGBA") as im:
    original = im
    txt = Image.new("RGBA", im.size, (255, 255, 255, 50))
    if im.size[1] > 500:
        font_size = 80
    else:
        font_size = 50
    fnt = ImageFont.truetype("fonts/FreeMono.ttf", font_size)
    d = ImageDraw.Draw(txt)

    draw = ImageDraw.Draw(im)
    for n in range(0, 5000, 200):
        draw.line((-200, im.size[1]-n, n-200, im.size[1]), fill='gray')
        draw.line(((n, -200), (-200, n)), joint='curve', fill='gray')

    d.text((10, 10), "Abdulvaliy", font=fnt, fill=(255, 255, 255, 128))
    d.text((im.size[0]-500, im.size[1]-100), "Abdulvaliy", font=fnt, fill=(255, 255, 255, 128))
    d.text((im.size[0]/2-150, im.size[1]/2-80), "Abdulvaliy", font=fnt, fill=(255, 255, 255, 128))

    out = Image.alpha_composite(im, txt)
    print(im.size)
    out.show()










# with Image.open("download.png").convert("RGBA") as base:
#
#     # make a blank image for the text, initialized to transparent text color
#     txt = Image.new("RGBA", base.size, (255,255,255,100))
#
#     # get a font
#     fnt = ImageFont.truetype("fonts/FreeMono.ttf", 40)
#     # get a drawing context
#     d = ImageDraw.Draw(txt)
#
#     # draw text, half opacity
#     d.text((-10,-10), "Hello", font=fnt, fill=(255,255,255,128))
#     # draw text, full opacity
#     d.text((10,60), "World", font=fnt, fill=(0,0,0,100))
#
#     out = Image.alpha_composite(base, txt)
#
#     out.show()


#####################################################
# # create an image
# out = Image.open('download.png')
#
# # get a font
# fnt = ImageFont.truetype("fonts/FreeMono.ttf", 25)  # Pillow/Tests/
# # get a drawing context
# d = ImageDraw.Draw(out)
#
# # draw multiline text
# d.multiline_text((80, 55), "Hello\nAbdulvaliy", font=fnt, fill=(0, 0, 0))
#
# out.show()
