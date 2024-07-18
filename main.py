import cv2
import numpy as np
import os

def load(input):
    try:
        image = cv2.imread(input, cv2.IMREAD_GRAYSCALE)
        if image is None:
            raise IOError(f"Cannot open image {input}")
        return image
    except Exception as e:
        print(e)
        return None

def gaussian_filter(image):
    kernel = np.array([
        [1, 4, 7, 4, 1],
        [4, 16, 26, 16, 4],
        [7, 26, 41, 26, 7],
        [4, 16, 26, 16, 4],
        [1, 4, 7, 4, 1]
    ], dtype=np.float32)
    kernel /= 273.0

    result = cv2.filter2D(image, -1, kernel)

    return result

def save(output, result):
    try:
        cv2.imwrite(output,result)
    except Exception as e:
        print(f"Failed to save Image {output}: {e}")

def process_images_in_folder(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.tiff', '.tif')):
            input = os.path.join(input_folder, filename)
            output = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_gaussian.tiff")

            image = load(input)
            if image is None:
                continue

            result = gaussian_filter(image)

            save(output, result)

            print(f"Processed image saved to: {output}")

def main():
    input_folder = "input_images"
    output_folder = "output_images"

    process_images_in_folder(input_folder, output_folder)
    
if __name__ == "__main__":
    main()