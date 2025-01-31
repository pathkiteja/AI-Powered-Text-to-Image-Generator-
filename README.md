

Welcome to the **AI-Powered-Text-to-Image-Generator-** This project leverages the power of the Stable Diffusion model to generate stunning images from text prompts. Whether you're an artist, developer, or enthusiast, this tool allows you to create high-quality images effortlessly.



## 🚀 Features

- **Pre-trained Stable Diffusion Model**: Utilizes the `runwayml/stable-diffusion-v1-5` model for high-quality image generation.
- **Optimized for Speed & Memory**: Uses half-precision (`fp16`) and the Euler discrete scheduler for faster and more efficient processing.
- **NSFW Filter Disabled**: Allows unrestricted image generation by disabling the safety checker.
- **GPU Support**: Automatically utilizes CUDA if available for enhanced performance.
- **Easy-to-Use Interface**: Simple command-line prompts make image generation straightforward.

## 🛠️ Prerequisites

Before you begin, ensure you have met the following requirements:

- **Operating System**: Windows, macOS, or Linux
- **Python**: Version 3.8 or higher
- **CUDA**: If using a GPU, ensure CUDA is installed and properly configured

## 📦 Installation

pip install torch diffusers transformers pillow

Follow these steps to set up the project on your local machine.

## Create a Virtual Environment
python -m venv venv---
venv\Scripts\activate

**📝 Usage**
Follow these steps to generate images from text prompts.
**Run the Script**
python generate_image.py
**Enter Your Text Prompt**
📝 Enter your text prompt: A serene landscape with mountains and a river at sunset
**Wait for the Image to Generate**
🔄 Loading model... This may take a few minutes.
✅ Model loaded successfully!
🎨 Generating image... Please wait.
✅ Image saved as 'generated_image.png' 🎉

**Project Structure**
stable-diffusion-image-generator/
├── generate_image.py
├── generated_image.png
├── README.md
├── requirements.txt

**requirements.txt**
torch
diffusers
transformers
pillow

--> pip install -r requirements.txt
**🤝 Contributing**
Contributions are welcome! Please follow these steps:

**Fork the repository**
**Create a new branch (git checkout -b feature/YourFeature)**
**Commit your changes (git commit -m 'Add some feature')**
**Push to the branch (git push origin feature/YourFeature)**
**Open a Pull Request**

**check my youtube video**
