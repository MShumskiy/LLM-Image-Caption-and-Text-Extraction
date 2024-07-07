import gradio as gr
import numpy as np
from PIL import Image
import os
from tools.ImgCapModel import describe,caption_image

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Ensure that accelerate is imported to enable its features
from accelerate import Accelerator

# Initialize the accelerator
accelerator = Accelerator()

def main(input_image: np.ndarray):
    # Convert numpy array to PIL Image and save it
    raw_image = Image.fromarray(input_image).convert('RGB')
    # Ensure the directory exists
    save_directory = 'g:\\projects\\ai_based\\ai_tools\\Building Generative AI-Powered Applications with Python\\image_captioning\\images/'
    os.makedirs(save_directory, exist_ok=True)
    
    # Define the base filename
    base_filename = "input_image"
    file_extension = ".jpg"
    image_path = os.path.join(save_directory, base_filename + file_extension)
    
    # Check if the file already exists and add a suffix if it does
    counter = 1
    while os.path.exists(image_path):
        image_path = os.path.join(save_directory, f"{base_filename}_{counter}{file_extension}")
        counter += 1
    
    # Save the image
    raw_image.save(image_path)

    tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen-VL", trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-VL", trust_remote_code=True)
    result = caption_image(image_path,tokenizer,model)
    caption = result[0].split(': ')[-1]
    text = result[1].split(': ')[-1]
    return {"caption": caption, "text": text}

iface = gr.Interface(
    fn=main, 
    inputs=gr.Image(), 
    outputs="json",
    title="Image Description Generator",
    description="This is a simple web app for extracting caption and text from image."
)

iface.launch()

