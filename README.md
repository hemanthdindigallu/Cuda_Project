# Gaussian Filtering


## Project Description

This Python script performs Gaussian filtering on a grayscale image using OpenCV and NumPy libraries. Gaussian filtering is a common image processing technique used to blur images and reduce noise. The script reads an input image in TIFF format, applies a Gaussian filter to it, and saves the processed image in the same format.

## How to Run the Code

1. Make sure you have Python installed.

2. Set Up a Virtual Environment in VS Code:

* Open VS Code.
* Open the terminal (`Ctrl+``).
* Navigate to your project directory:

cd path\to\your\project
* Create a virtual environment:

python -m venv venv
* Activate the virtual environment:
Windows:
.\venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

3.  Install Required Python Packages:

In the terminal with the virtual environment activated, install the necessary packages:

pip install numpy opencv-python-headless

4. Configure VS Code Python Interpreter:

Open the Command Palette (Ctrl+Shift+P or Cmd+Shift+P).
Type Python: Select Interpreter and select the interpreter that matches your virtual environment. It should show up as something like Python 3.x.x (venv).

5. Run the Script:

In the terminal, ensure your virtual environment is activated.
Run the script:

python main.py

Following these steps should help you successfully run the image processing code using only NumPy and OpenCV in VS Code. If you encounter any issues, please let me know!