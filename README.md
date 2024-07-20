
# Image Compression to WebP

This Python script compresses images in a specified input folder and saves them in WebP format in an output folder. The script uses the Pillow library (PIL) to handle image processing.

## Requirements

- Python 3.x
- Pillow library

You can install the Pillow library using pip:

```bash
pip install pillow
```

## Usage

1. **Import the Script**: Make sure the script is saved in a file, e.g., `main.py`.

2. **Call the Function**: Use the function `compress_images_to_webp` to compress images.

### Function Signature

```python
def compress_images_to_webp(input_folder, output_folder, quality=80):
```

- `input_folder`: Path to the folder containing images you want to compress.
- `output_folder`: Path to the folder where the compressed WebP images will be saved.
- `quality` (optional): Compression quality for the WebP images (default is 80).

### Example

```python
import compress_images

input_folder = 'path/to/input/folder'
output_folder = 'path/to/output/folder'
compress_images_to_webp(input_folder, output_folder, quality=85)
```

## Supported Image Formats

The script supports the following image formats for compression:
- PNG
- JPG
- JPEG
- BMP
- TIFF

## Notes

- The script creates the output folder if it does not already exist.
- The WebP images are saved with the same name as the original image but with a `.webp` extension.
- The `quality` parameter controls the compression quality; lower values result in higher compression and lower quality.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

Elkin Garcia