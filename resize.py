from PIL import Image
import os

def resize_images(input_folder, output_folder, sizes):
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path_base, extension = os.path.splitext(filename)
        
        # Open the image
        with Image.open(input_path) as img:
            # Resize the image without specifying the resampling filter
            resized_img = img.resize((size, size))
            
            # Save the resized image
            output_path = os.path.join(output_folder, f"{output_path_base}{extension}")
            resized_img.save(output_path)

# Set your input and output folders
input_folder = "images"
output_folder = "resized_images_64"

# Set the desired sizes for resizing
size = 64

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Resize images
resize_images(input_folder, output_folder, size)

print("Images resized successfully for size 64x64.")

output_folder = "resized_images_256"

# Set the desired sizes for resizing
size = 256

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Resize images
resize_images(input_folder, output_folder, size)

print("Images resized successfully for size 256x256.")
