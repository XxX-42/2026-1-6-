
from PIL import Image
import os

try:
    img = Image.open('image.png')
    img = img.convert('RGB')
    img.save('logo.jpg', 'JPEG')
    print("Image converted to logo.jpg")
except Exception as e:
    print(f"Error: {e}")
