from PIL import Image
import os

# Dimensiuni dorite pentru imaginile redimensionate
width = 300
height = 200

# Lista de imagini pentru proiecte
project_images = [
    "Budget traker.jpeg",
    "Phone Agenda.jpeg"
]

# Calea către directorul în care se află imaginile
images_directory = 'C:\\Users\\mihai\\html-css-js portofolio\\html-css-js-portofolio\\assets\\'

# Redimensionează fiecare imagine
for image in project_images:
    image_path = os.path.join(images_directory, image)
    if os.path.exists(image_path):
        img = Image.open(image_path)
        
        # Redimensionează imaginea la dimensiunile exacte
        resized_img = img.resize((width, height), Image.ANTIALIAS)
        
        # Salvează imaginea redimensionată
        resized_img.save(image_path)
        print(f"Redimensionat {image} la {width}x{height}")
    else:
        print(f"Imaginea {image} nu a fost găsită în directorul specificat.")

# Verifică dacă fișierele există
for image in project_images:
    file_path = os.path.join(images_directory, image)
    if os.path.exists(file_path):
        print(f"Fișierul {image} există.")
    else:
        print(f"Fișierul {image} nu există sau calea este incorectă.")
