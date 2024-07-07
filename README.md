# LLM-Image-Caption-and-Text-Extraction

# Image Description Generator

This repository contains a simple web application that generates captions and descriptive text from images using a pre-trained model. The application is built with Python and leverages the Gradio library for creating the user interface.

## Features

- Upload an image to generate a caption and descriptive text.
- Utilizes a pre-trained model for image captioning.
- Simple and user-friendly web interface.

## Requirements

- Python 3.7+
- Gradio
- NumPy
- Pillow
- Transformers
- PyTorch
- Accelerate

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/image-description-generator.git
    cd image-description-generator
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Ensure you have the `Qwen/Qwen-VL` model available. You can modify the code to point to a different model if needed.

2. Run the application:
    ```bash
    python app.py
    ```

3. Open your web browser and navigate to the provided Gradio link (usually `http://127.0.0.1:7860`).

4. Upload an image to generate the caption and descriptive text.

## Code Explanation

The main components of the application are:

- **Image Saving**: Converts the input image from a NumPy array to a PIL Image and saves it locally, ensuring no filename conflicts.
- **Image Captioning**: Uses a pre-trained model to generate a caption and descriptive text for the saved image.
- **Gradio Interface**: Provides a user-friendly interface for uploading images and displaying results.

