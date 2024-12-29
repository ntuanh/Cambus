from PIL import Image, ImageDraw

# Load the image
image_path = 'busdrawing.png'
image = Image.open(image_path)

# Create a draw object
draw = ImageDraw.Draw(image)

# Define the position for the bus marker (example coordinates)
bus_position = (100, 100)  # Placeholder for actual pixel coordinates

# Draw a red circle to mark the bus position
draw.ellipse((bus_position[0] - 5, bus_position[1] - 5, bus_position[0] + 5, bus_position[1] + 5), fill='red')

# Save the modified image
image.save('busdrawing_marked.png')
print("Bus position marked on the image.")
