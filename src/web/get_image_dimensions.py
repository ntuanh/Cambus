from PIL import Image

# Load the image
image_path = 'busdrawing.png'
image = Image.open(image_path)

# Get dimensions
width, height = image.size
print(f"Image dimensions: {width}x{height}")
