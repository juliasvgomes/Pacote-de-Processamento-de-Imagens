from PIL import Image

def convert_to_grayscale(image_path, output_path):
    image = Image.open(image_path)
    grayscale_image = image.convert("L")
    grayscale_image.save(output_path)

def image_info(image_path):
    image = Image.open(image_path)
    return image.format, image.size, image.mode
