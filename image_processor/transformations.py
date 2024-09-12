from PIL import Image

def rotate_image(image_path, output_path, degrees):
    image = Image.open(image_path)
    rotated_image = image.rotate(degrees)
    rotated_image.save(output_path)

def resize_image(image_path, output_path, size):
    image = Image.open(image_path)
    resized_image = image.resize(size)
    resized_image.save(output_path)
