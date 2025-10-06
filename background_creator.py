import random
from PIL import Image

# Settings
input_image_path = 'public/img/aliice_head.png'
canvas_size = (3000, 3000)  # Width, Height
num_images = 20  # Number of images to place
output_image_path = 'collage_output.png'

# Load the input image
img = Image.open(input_image_path).convert('RGBA')
img_w, img_h = img.size

# Create a blank canvas
canvas = Image.new('RGBA', canvas_size, (255, 255, 255, 255))

for _ in range(num_images):
    # Random position
    x = random.randint(0, canvas_size[0] - img_w)
    y = random.randint(0, canvas_size[1] - img_h)
    # Random rotation
    angle = random.uniform(-30, 30)
    rotated = img.rotate(angle, expand=True)
    # Paste onto canvas
    canvas.paste(rotated, (x, y), rotated)

# Save the result
canvas.save(output_image_path)
print(f"Collage saved to {output_image_path}")