import os
import requests
from pathlib import Path
from crewai.tools import tool

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
MODEL_ID = "stabilityai/stable-diffusion-xl-base-1.0"

@tool
def stable_diffusion_gallery(prompt: str) -> str:
    """
    Generates a gallery of mockup images (Home, Profile, Settings, Login)
    for the given app concept using Hugging Face's Stable Diffusion API.
    Saves them in the 'static' folder and returns a JSON-like string list of image paths.
    """
    if not HUGGINGFACE_API_KEY:
        return "❌ Missing HUGGINGFACE_API_KEY environment variable."

    static_dir = Path(__file__).resolve().parents[1] / "static"
    os.makedirs(static_dir, exist_ok=True)

    screens = ["Home", "Profile", "Settings", "Login"]
    image_paths = []
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    api_url = f"https://api-inference.huggingface.co/models/{MODEL_ID}"

    for screen in screens:
        screen_prompt = f"{prompt}, {screen} screen of the mobile app interface, modern, professional, 3D UI, pastel colors, minimal design"
        print(f"🎨 Generating {screen} screen...")
        response = requests.post(api_url, headers=headers, json={"inputs": screen_prompt})
        if response.status_code != 200:
            print(f"⚠️ Failed to generate {screen} screen: {response.text}")
            continue

        image_path = static_dir / f"app_mockup_{screen.lower()}.png"
        with open(image_path, "wb") as f:
            f.write(response.content)
        image_paths.append(str(image_path.name))  # relative for Flask

    if not image_paths:
        return "❌ No images were successfully generated."

    print(f"✅ Generated mockups: {image_paths}")
    return str(image_paths)
