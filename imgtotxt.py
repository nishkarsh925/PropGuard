import os
from PIL import Image
import pytesseract

# 🔧 Windows users: Set this if tesseract isn't in PATH
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 📁 Input/Output directories
input_folder = "images"
output_folder = "output"
os.makedirs(output_folder, exist_ok=True)

# ⚙️ Tesseract OCR config
config = r"--oem 3 --psm 6"
lang = "eng"  # Or 'hin+eng' for Hindi+English

# 📤 Process all images in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".pdf")):
        filepath = os.path.join(input_folder, filename)
        image = Image.open(filepath)

        print(f" OCR processing: {filename}")
        text = pytesseract.image_to_string(image, config=config, lang=lang)

        # Save output
        output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.txt")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)

        print(f" Saved: {output_path}")
