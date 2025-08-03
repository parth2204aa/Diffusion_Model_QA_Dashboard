# ------------------- backend/model_runner.py -------------------
from diffusers import StableDiffusionPipeline
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipe = pipe.to(device)

def generate_image(prompt):
    image = pipe(prompt).images[0]
    return image
