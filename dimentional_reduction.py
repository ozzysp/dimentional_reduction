from PIL import Image

def convert_to_grayscale(image):
    width, height = image.size
    grayscale_image = Image.new("L", (width, height))

    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            gray_value = int(0.2989 * r + 0.5870 * g + 0.1140 * b)
            grayscale_image.putpixel((x, y), gray_value)

    return grayscale_image

def binarize(image, threshold=128):
    width, height = image.size
    binary_image = Image.new("1", (width, height))

    for x in range(width):
        for y in range(height):
            gray_value = image.getpixel((x, y))
            if gray_value < threshold:
                binary_image.putpixel((x, y), 0)
            else:
                binary_image.putpixel((x, y), 255)

    return binary_image


input_path = input("Type path of picture: ")


try:
    img = Image.open(input_path)
except Exception as e:
    print("Error opening image:", e)
    exit()

gray_img = convert_to_grayscale(img)

threshold_value = 128
bw_img = binarize(gray_img, threshold_value)

output_folder = input("Type path to save B&W image: ")

gray_output_path = input("Type name to save gray image: ")
gray_img.save(output_folder + gray_output_path)

bw_output_path = input("Type name for binarized image (example: binary.png): ")
bw_img.save(output_folder + bw_output_path)

print(f"The images was saved in {output_folder}{gray_output_path} and {output_folder}{bw_output_path}")
