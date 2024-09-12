from PIL import Image, ImageFilter

def apply_blur(image_path, output_path):
    image = Image.open(image_path)
    blurred_image = image.filter(ImageFilter.BLUR)
    blurred_image.save(output_path)

def apply_contour(image_path, output_path):
    image = Image.open(image_path)
    contoured_image = image.filter(ImageFilter.CONTOUR)
    contoured_image.save(output_path)
