import os
from PIL import Image

# Folder containing images
folder_path = "people"

# Supported image formats
valid_extensions = (".jpg", ".jpeg", ".png")

# Number words for naming
number_words = [
    "one", "two", "three", "four", "five",
    "six", "seven", "eight", "nine", "ten",
    "eleven", "twelve", "thirteen", "fourteen", "fifteen",
    "sixteen", "seventeen", "eighteen", "nineteen", "twenty"
]

# Get all image files
images = [
    f for f in os.listdir(folder_path)
    if f.lower().endswith(valid_extensions)
]

images.sort()  # keep order consistent

for index, filename in enumerate(images):
    if index >= len(number_words):
        print("Not enough number words defined.")
        break

    old_path = os.path.join(folder_path, filename)
    new_name = f"user-{number_words[index]}.webp"
    new_path = os.path.join(folder_path, new_name)

    try:
        with Image.open(old_path) as img:
            img.convert("RGB").save(new_path, "WEBP", quality=85)

        print(f"Converted: {filename} → {new_name}")

    except Exception as e:
        print(f"Error processing {filename}: {e}")

print("Done.")