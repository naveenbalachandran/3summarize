import re
import requests
def extract_video_id(url):
    regex_pattern = r"(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?&v=|watch\?.+&v=))([^&?\/\s]{11})"

    match = re.search(regex_pattern, url)
    if match:
        return match.group(1)

    return None

def generate_transcript_url(video_id):
    return f"https://youtubetranscript.com/?server_vid={video_id}"

def extract_text_from_transcript(url):
    response = requests.get(url)
    transcript_data = response.text
    # Use regular expressions to extract the text content within <text> tags
    text_pattern = r"<text.*?>(.*?)<\/text>"
    extracted_text = re.findall(text_pattern, transcript_data, re.DOTALL)
    
    # Remove any extra whitespace or newline characters
    extracted_text = [text.strip() for text in extracted_text]
    return extracted_text