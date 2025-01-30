import requests
from config import GEMINI_API_KEY

# Function to analyze image (or file)
def analyze_image(file_path):
    url = "https://api.generativeai.google.com/v1/images:describe"
    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
    }
    files = {'file': open(file_path, 'rb')}
    response = requests.post(url, headers=headers, files=files)
    return response.json()
