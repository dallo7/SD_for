import torch
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16)


prompt = "a photograph of an astronaut riding a horse"
image = pipe(prompt).images[0]

# Now to display an image you can either save it such as:
image.save(f"/static/tes1.png")
