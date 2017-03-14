
from PIL import Image
from numpy import array

img = Image.open("d.jpg")
data = array(img)


print(data)
