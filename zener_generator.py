
import numpy as np

from PIL import Image, ImageDraw
# from math import sin
from numpy import arange, sin, pi
from random import randint, uniform
import sys
import os


# Draw Star
# im = Image.new('L', (25, 25), 255)
# draw = ImageDraw.Draw(im)
# width = 2
# draw.line((0,9, 9,9), fill=0, width=width)
# draw.line((9,9, 12,0), fill=0, width=width)
# draw.line((12,0, 15,9), fill=0, width=width)
# draw.line((15,9, 25,9), fill=0, width=width)
# draw.line((25,9, 16,15), fill=0, width=width)
# draw.line((16,15, 19,24), fill=0, width=width)
# draw.line((19,24, 12,19), fill=0, width=width)
# draw.line((12,19, 4,24), fill=0, width=width)
# draw.line((4,24, 7,15), fill=0, width=width)
# draw.line((7,15, 0,9), fill=0, width=width)
# im.show()
# im.save("star.png")

#Draw Square
# im = Image.new('L', (25, 25), 255)
# draw = ImageDraw.Draw(im)
# width = 2
# draw.line((1,1, 1,22), fill=0, width=width)
# draw.line((1,22, 22,22), fill=0, width=width)
# draw.line((22,1, 22,23), fill=0, width=width)
# draw.line((1,1, 22,1), fill=0, width=width)
# im.show()
# im.save("square.png")

#Draw Circle
# im = Image.new('L', (25, 25), 255)
# draw = ImageDraw.Draw(im)
# width = 2
# draw.ellipse((1,1,23,23),outline=0)
# im.show()
# im.save("circle.png")

#Draw Cross
# im = Image.new('L', (25, 25), 255)
# draw = ImageDraw.Draw(im)
# width = 2
# draw.line((12,1, 12,23), fill=0, width=width)
# draw.line((23,12, 1,12), fill=0, width=width)
# im.show()
# im.save("cross.png")

#Draw Wavy
# im = Image.new('L', (25, 25), 255)
# draw = ImageDraw.Draw(im)
# width = 2
# t = arange(0.0, 1.0, 0.001)
# x = arange(0,25,0.025)
# for i,j in zip(x,t):#arange(0.0, 1.0, 0.01):
#     draw.point((i,sin(2*pi*j)+12),0)
# im.show()
# im.save("wavy.png")

#
# im = Image.open("cross.png")
# im.resize((25,25),0).convert(mode='L').save("cross1.png")
#
# im = Image.open("square.png")
# im.resize((25,25),0).convert(mode='L').save("square1.png")
#
# im = Image.open("star.png")
# im.resize((25,25),0).convert(mode='L').save("star1.png")
#
# im = Image.open("wavy.png")
# im.resize((25,25),0).convert(mode='L').save("wavy1.png")
#
# im = Image.open("circle.png")
# im.resize((25,25),0).convert(mode='L').save("circle1.png")

'''
Variations in position of the symbol, variations in the orientation of the symbol, variations in the size of the symbol, variations in the thickness of the strokes in the symbol, variations in the size and number of stray marks such as ellipsoids drawn in the image.
'''


def position():
    x = randint(1,12)
    y = randint(1,12)
    return (x,y)

def scaleSize(image):
    s = uniform(0.5,1)
    scaledim = image.resize((int(25*s),int(25*s)),0)
    im = Image.new('L', (25, 25), 255)
    im.paste(scaledim,(1,1))#position())
    return im


def strayMarks(image):
    r = randint(0,2)
    draw = ImageDraw.Draw(image)
    for i in range(r):
        x1 = randint(1,22)
        y1 = randint(1,22)
        x2 = x1+randint(1,2)
        y2 = y1+randint(1,2)
        draw.ellipse((x1,y1,x2,y2),outline=0)

    return image

def orientation(image):
    return image.rotate(randint(0,180))

def rotate(image):
    im = image.convert('RGBA')
    rot = im.rotate(randint(0,180), expand=1).resize((25, 25))
    f = Image.new('RGBA', rot.size, (255,) * 4)
    im2 = Image.composite(rot, f, rot)
    return im2.convert("L")

n = 100 #sys.argv[2]
base = ['square.png', 'star.png', 'circle.png', 'cross.png', 'wavy1.png']
sym = ['Q', 'S', 'O', 'P', 'W']
symbol = {'Q': 0, 'S': 0, 'O': 0, 'P': 0, 'W': 0}

os.mkdir(str(sys.arg[1]))

for i in range(n):
    r = randint(0,4)
    im = Image.open(base[r])
    im = strayMarks(rotate(scaleSize(im)))
    # im.show()
    s = sym[r]
    im.save('./folder_name/'+s+str(symbol[s])+'.png')
    symbol[s] = symbol[s]+1
