from pathlib import Path
from PIL import Image

# ----------------------------
# CONFIGURATION
# ----------------------------
folder_path = Path("images")  # folder containing your images
prefix = "image"              # the base name prefix
start_number = 1              # starting index
use_words = True              # if True: image-one, image-two; else: image-1

# ----------------------------
# helper to convert number to words
# ----------------------------
def number_to_words(n):
    words = ["zero","one","two","three","four","five","six","seven","eight","nine","ten",
             "eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    tens = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    
    if n < 20:
        return words[n]
    elif n < 100:
        t = n // 10
        r = n % 10
        return tens[t] + (f"-{words[r]}" if r else "")
    else:
        return str(n)  # fallback for >99

# ----------------------------
# PROCESS IMAGES
# ----------------------------
supported_formats = [".png", ".jpg", ".jpeg", ".bmp", ".tiff"]

# find all image files
image_files = sorted([f for f in folder_path.glob("*") if f.suffix.lower() in supported_formats])

for idx, img_path in enumerate(image_files, start=start_number):
    try:
        # load image
        img = Image.open(img_path).convert("RGBA")  # keep transparency if any
        # determine new name
        number_str = number_to_words(idx) if use_words else str(idx)
        new_name = f"{prefix}-{number_str}.webp"
        new_path = folder_path / new_name
        # save as webp
        img.save(new_path, "WEBP", quality=95)
        print(f"Converted {img_path.name} → {new_name}")
        # optionally, delete the original
        # img_path.unlink()
    except Exception as e:
        print(f"Failed {img_path.name}: {e}")