# ZAMUDIO.png

This Python script generates PNG images with custom text, adjusting font size and line breaks dynamically to fit the image dimensions. The script allows users to specify a phrase, and it automatically adjusts the text size and alignment for aesthetic appearance.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Customization](#customization)
- [License](#license)

## Installation

### Requirements
- Python 3.x
- `PIL` (Python Imaging Library) or `Pillow`
- Custom font file (e.g., `GENEVA.ttf`)

### Steps

1. Install the necessary Python libraries:

   ```bash
   pip install Pillow
   ```

2. Ensure you have a font file available (in this case, `GENEVA.ttf`), and place it in the correct directory. Update the `FONT_PATH` in the script to match your system's path.

3. Download or clone the script to your local environment.

## Usage

1. **Set the destination folder** for saving generated images in the `WHERE_TO_SAVE` variable (e.g., `"C:/Users/Sebas/Documents/GENERADOR_PNG"`).

2. **Run the script** and input the desired text when prompted. The script will generate an image based on the input text.

   ```bash
   python script.py
   ```

   You will be prompted to enter a phrase or text.

3. **The generated PNG** will be saved in the specified directory.

## Examples

- If you input: `"Hello World"`, the script will generate a centered image with the text adjusted to fit the 500x500 pixel canvas.
  ![Hello_world!](https://github.com/user-attachments/assets/bed92a60-696d-48e3-84fc-b3e8a2d2baaf)


- For a single letter, the font size will be maximized to fill the image, whereas longer text will automatically adjust the font size and wrap lines as needed.
  ![z](https://github.com/user-attachments/assets/de6c4e10-81c1-4f7c-91bb-380260ee03f6)


## Customization

- **Font Path**: You can change the `FONT_PATH` variable to any custom TTF font file path of your choice.
  
- **Canvas Size**: Modify `WIDTH` and `HEIGHT` to change the dimensions of the generated image.

- **Font Size Adjustment**: The script decreases the font size dynamically when the text spans multiple lines to ensure it fits within the image.

## License

This project is licensed under the GPLv3 License.
