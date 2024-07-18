import cv2
import numpy as np

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

def main():
    input = "example_image.tiff"
    output = "example_gaussian.tiff"
    
    image  = load(input)
    if image is None:
        return
    
    result = gaussian_filter(image)
    
    save(output, result)
    
    print(f"Processed image saved to : {output}")
    
if __name__ == "__main__":
    main()