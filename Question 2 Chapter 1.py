# python -m venv myenv
# myenv\Scripts\activate
# pip install pillow

import time
from PIL import Image

# Step 1: Generate the number n
current_time = int(time.time())
generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10

print(f"Generated Number: {generated_number}")

# Step 2: Open the image
image_path = r"C:\Users\shuva\OneDrive\Documents\chapter1.jpg"  # Use your extracted path
img = Image.open(image_path)
pixels = img.load()  # Load the pixel data

# Prepare to sum all red values
red_sum = 0

# Step 3: Modify the pixel values
width, height = img.size
for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]  # Get the pixel at (x, y)
        # Add the generated number to each of the RGB values
        r = (r + generated_number) % 256
        g = (g + generated_number) % 256
        b = (b + generated_number) % 256
        # Update the pixel with new values
        pixels[x, y] = (r, g, b)
        # Add the red value to the sum
        red_sum += r

# Step 4: Save the modified image
output_image_path = 'chapter1out.png'
img.save(output_image_path)
print(f"Image saved as {output_image_path}")

# Step 5: Print the sum of the red values
print(f"Sum of all red pixel values: {red_sum}")
