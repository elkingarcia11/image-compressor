import os
from PIL import Image

def compress_images_to_webp(input_folder, output_folder, quality=80):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        # Construct the full input and output file paths
        input_image_path = os.path.join(input_folder, filename)
        output_image_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.webp')
        
        # Check if the file is an image (you can add more extensions if needed)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            # Open the input image
            image = Image.open(input_image_path)
            
            # Convert and save the image in WebP format
            image.save(output_image_path, 'webp', quality=quality)
            
            print(f"Compressed {filename} and saved to {output_image_path}")