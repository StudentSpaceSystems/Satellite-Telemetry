from PIL import Image
img = Image.open('image5.jpg').convert('L')
img.save('greyscale5.jpg')
