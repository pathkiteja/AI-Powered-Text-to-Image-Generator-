import torch
from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler
from PIL import Image

# ✅ Step 1: Load the Pre-trained Stable Diffusion Model
print("🔄 Loading model... This may take a few minutes.")

# Use "fp16" (half-precision) for lower memory usage
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16
)

# ✅ Fix NSFW Black Image Issue (Corrected)
pipe.safety_checker = lambda images, clip_input, **kwargs: (images, [False] * len(images))

# ✅ Step 2: Optimize for Speed & Memory
device = "cuda" if torch.cuda.is_available() else "cpu"  # Use GPU if available
pipe.to(device)  # Move model to GPU or keep on CPU

# Use a Faster Scheduler (Euler)
pipe.scheduler = EulerDiscreteScheduler.from_config(pipe.scheduler.config)

print("✅ Model loaded successfully!")

# ✅ Step 3: Get User Input for Text Prompt
prompt = input("📝 Enter your text prompt: ")

# ✅ Step 4: Generate Image
print("🎨 Generating image... Please wait.")
image = pipe(prompt).images[0]  # Generate image from text

# ✅ Step 5: Show & Save the Image
image.show()  # Open the image in the default viewer
image.save("generated_image.png")  # Save the image

print("✅ Image saved as 'generated_image.png' 🎉")
