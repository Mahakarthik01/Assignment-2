import time
from PIL import Image

current_time = int(time.time())
generated_number = (current_time % 100) + 50
if generated_number % 2 == 0:
    generated_number += 10

print(f"Generated number: {generated_number}")

image = Image.open('chapter1.jpg')  

pixels = image.load()
width, height = image.size

for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]
        pixels[x, y] = (min(r + generated_number, 255), 
                        min(g + generated_number, 255), 
                        min(b + generated_number, 255))

image.save('chapter1out.jpg')
print("Image saved as 'chapter1out.jpg'")

red_sum = 0
for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]
        red_sum += r

print(f"Sum of red pixel values: {red_sum}")