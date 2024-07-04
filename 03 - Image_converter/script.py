# Step 1
from PIL import Image
import os

# Step 2
input_dir = "input_images/"
output_dir = "output_images/"

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get all files in the input directory
files = os.listdir(input_dir)

# Iterate through each file in the input directory
for file in files:
    # Check if the file is an image
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".webp"):
        # Open the image
        image_path = os.path.join(input_dir, file)
        image = Image.open(image_path)

        # Convert the image format (e.g., from JPEG to PNG)
        new_file = os.path.splitext(file)[0] + ".png"
        output_path = os.path.join(output_dir, new_file)
        image.save(output_path, format="PNG")

        print(f"Converted {file} to PNG")

print("Conversion complete!")