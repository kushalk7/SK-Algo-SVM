from PIL import Image
#
# collage = Image.new("RGBA", (25, 25), 255)
#
# # open the pic and give it an alpha channel so it's transparent
# im1 = Image.open("cross.png").convert('RGBA')
#
# # rotate it and expand it's canvas so the corners don't get cut off:
# im2 = im1.rotate(32, expand = 1)
#
# # note the second appearance of im2, that's necessary to paste without a bg
# collage.paste(im2, (30, 30), im2 )
# # collage.save("new.jpg")
im = Image.open("cross.png").convert('RGBA')
rot = im.rotate( 45, expand=1 ).resize((25,25))
f = Image.new( 'RGBA', rot.size, (255,)*4 )
im2 = Image.composite( rot, f, rot )
im2.show()
# collage.show()