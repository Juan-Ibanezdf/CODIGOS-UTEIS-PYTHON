# Image Editing
# necessario fazer a intalação do wanda.
# pip install Wand
from wand.image import Image
# Crop
with Image(filename='test.jpg') as img:
    img.crop(width=100, height=100)
    img.save(filename='cropped.jpg')
# Resize
with Image(filename='test.jpg') as img:
    img.resize(width=100, height=100)
    img.save(filename='resized.jpg')
# Compress
with Image(filename='test.jpg') as img:
    img.compression_quality = 99
    img.save(filename='compressed.jpg')
# Merge
with Image(filename='test.jpg') as img:
    with Image(filename='test2.jpg') as img2:
        img.composite(img2, 0, 0)
        img.save(filename='merged.jpg')
# Rotate
with Image(filename='test.jpg') as img:
    img.rotate(90)
    img.save(filename='rotated.jpg')
# Flip
with Image(filename='test.jpg') as img:
    img.flip()
    img.save(filename='flipped.jpg')
# Enhance
with Image(filename='test.jpg') as img:
    img.enhance_contrast()
    img.save(filename='contrasted.jpg')
# Blur
with Image(filename='test.jpg') as img:
    img.blur()
    img.save(filename='blurred.jpg')
# Sharpen
with Image(filename='test.jpg') as img:
    img.sharpen()
    img.save(filename='sharpened.jpg')
# Colorize
with Image(filename='test.jpg') as img:
    img.colorize(0, 0, 0, 0)
    img.save(filename='colorized.jpg')
# Drop Shadow
with Image(filename='test.jpg') as img:
    img.shadow(color='black', offset=10, opacity=50, blur=5)
    img.save(filename='shadowed.jpg')
# Border
with Image(filename='test.jpg') as img:
    img.border(10, 'black')
    img.save(filename='bordered.jpg')