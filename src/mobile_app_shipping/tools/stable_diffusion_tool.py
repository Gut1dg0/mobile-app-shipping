import base64
import requests
from crewai.tools import tool
from pathlib import Path
import os

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

@tool
def stable_diffusion_generate(prompt: str) -> str:
    """
    Generate an app mockup image using Stable Diffusion via Hugging Face Inference API.
    Saves the result as 'app_mockup.png' and returns the file path.
    """
    if not HUGGINGFACE_API_KEY:
        return "❌ Missing Hugging Face API key (HUGGINGFACE_API_KEY)."

    print(f"🎨 Generating mockup image from prompt: {prompt[:100]}...")

    model_id = "stabilityai/stable-diffusion-xl-base-1.0"
    api_url = f"https://api-inference.huggingface.co/models/{model_id}"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    payload = {"inputs": prompt}

    response = requests.post(api_url, headers=headers, json=payload)
    if response.status_code != 200:
        return f"❌ Error {response.status_code}: {response.text}"

    image_bytes = response.content
    image_path = Path(__file__).resolve().parents[2] / "static" / "app_mockup.png"
    os.makedirs(image_path.parent, exist_ok=True)
    with open(image_path, "wb") as f:
        f.write(image_bytes)

    print(f"✅ Image saved at {image_path}")
    return str(image_path)
