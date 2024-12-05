'''
conda install conda-forge::pillow
'''

from PIL import Image, ImageFilter, ImageDraw, ImageFont

image1 = Image.open('test.png')
image2 = Image.open('output.png')
image3 = Image.open('num_8-8bit.jpg')
#image1.show()

# convert in black and white
#gray = image1.convert('L')
#gray.show()
#gray.save('gray.png')

# reduce size
#miniature = image1.resize((10, 10))
#miniature.show()

# filtering image
#filtre = image1.filter(ImageFilter.GaussianBlur)
#filtre.show()

# drawing on image
#draw = ImageDraw.Draw(image1)
#police = ImageFont.truetype('MadimiOne-Regular.ttf', 32)
#draw.text((32, 150), 'TEST', fill='white', font=police)
#image1.show()

# concate images
width = image1.width + image2.width + image3.width
height = max(image1.height, image2.height, image3.height)
img = Image.new('RGB', (width, height), (255, 255, 255))
img.paste(image1, (0,0))
img.paste(image2, (image1.width, 0))
img.paste(image3, (image1.width + image2.width, 0))
img.show()

