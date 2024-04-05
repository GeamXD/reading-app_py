import os
from pathlib import Path
import base64
from openai import OpenAI
from anthropic import Anthropic
from dotenv import load_dotenv

###### load env ########
load_dotenv()

# ###### API KEY ########
OPEN_API_KEY = os.getenv('OPEN_AI_API_KEY')
CLAUDE_API_KEY = os.getenv('CLAUDE_API_KEY')

client = OpenAI(api_key=OPEN_API_KEY)
speech_file_path = Path(__file__).parent / "speech.mp3"


def text_to_speech(text: str) -> None:
    response = client.audio.speech.create(
    model="tts-1",
    voice="nova",
    input=f"{text}"
    )
    return response.stream_to_file(speech_file_path)

def speech_to_text(audio_file, lang='English'):
    with open(audio_file, "rb") as audio_file:
        audio_file= open("/path/to/file/german.mp3", "rb")
        translation = client.audio.translations.create(
        model="whisper-1", 
        file=audio_file
        )
    return translation.text

# text_1 = 'Hello'
# text_to_speech(text_1)

# speech_file_path = Path(__file__).parent / "speech.mp3"




############ SPEECH TO TEXT ################################

# with open("Audio/marvin_minsky.mp3", "rb") as audio_file:
# transcript = openai.Audio.transcribe(
#         file = audio_file,
#         model = "whisper-1",
#         response_format="text",
#         language="en"
#     )
# print(transcript)
# from openai import OpenAI
# client = OpenAI()

# audio_file= open("/path/to/file/german.mp3", "rb")
# translation = client.audio.translations.create(
#   model="whisper-1", 
#   file=audio_file
# )
# print(translation.text)




# ############################# claude #################################

client_2 = Anthropic(api_key=CLAUDE_API_KEY)
MODEL_NAME = "claude-3-haiku-20240307"

def get_base64_encoded_image(image):
    binary_data = image.read()
    base_64_encoded_data = base64.b64encode(binary_data)
    base64_string = base_64_encoded_data.decode('utf-8')
    return base64_string

def image_to_text(img, lang='English'):

    message_list = [
        {
            "role": 'user',
            "content": [
                {"type": "image", "source": {"type": "base64",
                                             "media_type": "image/jpeg", "data": get_base64_encoded_image(img)}},
                {"type": "text", "text": f"Briefly describe this image in {lang}?"}
            ]
        }
    ]

    response = client_2.messages.create(
        model=MODEL_NAME,
        max_tokens=512,
        messages=message_list,
        temperature=0.2,
    )
    
    return response.content[0].text
