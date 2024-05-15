from PIL import Image
import os

# Desired dimensions for the resized images
width = 300
height = 200

# List of image files for the C++ projects
cpp_images = [
    "Budget traker.jpeg",
    "Phone Agenda.jpeg"
]

# Path to the directory where the images are located
images_directory = 'C:\\Users\\mihai\\html-css-js portofolio\\html-css-js-portofolio\\assets\\'

# Iterate through each image and resize it
for image in cpp_images:
    image_path = os.path.join(images_directory, image)
    if os.path.exists(image_path):
        img = Image.open(image_path)
        # Preserve aspect ratio and pad with white background
        img.thumbnail((width, height))
        padded_img = Image.new("RGB", (width, height), "white")
        x_offset = (width - img.width) // 2
        y_offset = (height - img.height) // 2
        padded_img.paste(img, (x_offset, y_offset))
        padded_img.save(image_path)
        print(f"Resized {image} to {width}x{height}")
    else:
        print(f"Image {image} was not found in the specified directory.")

# Check if the file exists
for image in cpp_images:
    file_path = os.path.join(images_directory, image)
    if os.path.exists(file_path):
        print(f"File {image} exists.")
    else:
        print(f"File {image} does not exist or the path is incorrect.")
