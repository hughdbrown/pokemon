#!/usr/bin/env python3

import os

from PIL import Image, ImageOps

def open_image(file_path):
    """Opens an image file as a JPG/JPEG."""
    if file_path.lower().endswith(('.jpg', '.jpeg')):
        return Image.open(file_path)
    else:
        print("Error: File must be a JPG or JPEG.")
        return None

def save_image(image, file_path):
    """Saves the image as a PNG file."""
    if not file_path.lower().endswith('.png'):
        file_path += '.png'
    image.save(file_path, 'PNG')
    print(f"Image saved as {file_path}")

def scale_image(image, x, y):
    """Scales the image to fit within a box of x by y dimensions."""
    return ImageOps.fit(image, (x, y))

def rotate_image(image, angle):
    """Rotates the image by the specified angle."""
    return image.rotate(angle, expand=True)

from PIL import Image, ImageOps, ImageDraw

def create_grid(image, rows, cols, box_size):
    """Creates a grid of the image with specified rows, columns, and box size, including black lines around each box."""
    grid_width = cols * box_size[0]
    grid_height = rows * box_size[1]
    grid_image = Image.new('RGB', (grid_width, grid_height), (255, 255, 255))
    draw = ImageDraw.Draw(grid_image)

    for row in range(rows):
        for col in range(cols):
            box_x = col * box_size[0]
            box_y = row * box_size[1]
            box_image = image.copy()
            box_image.thumbnail(box_size)

            # Calculate position to center the image in the box
            x_center = box_x + (box_size[0] - box_image.width) // 2
            y_center = box_y + (box_size[1] - box_image.height) // 2

            grid_image.paste(box_image, (x_center, y_center))

            # Draw black rectangle (box outline)
            draw.rectangle(
                [box_x, box_y, box_x + box_size[0] - 1, box_y + box_size[1] - 1],
                outline="black"
            )

    return grid_image

def main():
    while True:
        print("\nAvailable options:")
        print("1. Open image file (JPG/JPEG)")
        print("2. Save image as PNG")
        print("3. Scale image")
        print("4. Rotate image")
        print("5. Create grid with image")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            file_path = input("Enter the path of the JPG/JPEG file: ")
            image = open_image(file_path)
            if image:
                print("Image opened successfully.")
        elif choice == '2':
            if 'image' in locals():
                file_path = input("Enter the path to save the PNG file: ")
                save_image(image, file_path)
            else:
                print("No image loaded.")
        elif choice == '3':
            if 'image' in locals():
                x = int(input("Enter the width of the box: "))
                y = int(input("Enter the height of the box: "))
                image = scale_image(image, x, y)
                print("Image scaled successfully.")
            else:
                print("No image loaded.")
        elif choice == '4':
            if 'image' in locals():
                angle = float(input("Enter the angle to rotate the image: "))
                image = rotate_image(image, angle)
                print("Image rotated successfully.")
            else:
                print("No image loaded.")
        elif choice == '5':
            if 'image' in locals():
                rows = int(input("Enter the number of rows in the grid: "))
                cols = int(input("Enter the number of columns in the grid: "))
                box_width = int(input("Enter the width of each box: "))
                box_height = int(input("Enter the height of each box: "))
                box_size = (box_width, box_height)
                grid_image = create_grid(image, rows, cols, box_size)
                image = grid_image
                print("Grid created successfully.")
            else:
                print("No image loaded.")
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

