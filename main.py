import cv2
import numpy as np

def load(input):
    return 

def apply_gaussian_filter(image):
    return

def save(output, result):
    return

def main():
    input = "example_image.tiff"
    output = "example_gaussian.tiff"
    
    image  = load(input)
    if image is None:
        return
    
    result = apply_gaussian_filter(image)
    
    save(output, result)
    
    print(f"Processed image saved to : {output}")
    
if __name__ == "__main__":
    main()