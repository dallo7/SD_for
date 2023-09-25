import requests
import io
from PIL import Image

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1-base"
headers = {"Authorization": "Bearer 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"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content


def save_image(image_bytes, filename):
    with open(filename, "wb") as f:
        f.write(image_bytes)


def generate_image(prompt):
    image_bytes = query({"inputs": prompt})
    image = Image.open(io.BytesIO(image_bytes))
    return image


def save_generated_image(image, filename):
    image.save(filename, quality=90)


# Example usage
# prompt = "Astronaut riding a horse"
# image = generate_image(prompt)
# save_generated_image(image, "template/static/images/image.jpg")
