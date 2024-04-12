import os
from pathlib import Path
import base64
from openai import OpenAI
from anthropic import Anthropic
from dotenv import load_dotenv
from faster_whisper import WhisperModel

###### load env ########
load_dotenv()

# ###### API KEY ########
OPEN_API_KEY = os.getenv('OPEN_AI_API_KEY')
CLAUDE_API_KEY = os.getenv('CLAUDE_API_KEY')

client = OpenAI(api_key=OPEN_API_KEY)
speech_file_path = Path(__file__).parent / "speech.mp3"



def text_to_speech_openai(text: str) -> None:
    response = client.audio.speech.create(
    model="tts-1",
    voice="nova",
    input=f"{text}"
    )
    response.stream_to_file(speech_file_path)
    return 'Success'

def speech_to_text(audio_file):
    with open(audio_file, "rb") as file:
        aud_file = open(audio_file, "rb")
        translation = client.audio.translations.create(
        model="whisper-1", 
        file=aud_file
        )
    return translation.text

############ FAST WHISPER MODEL ###############################
def speech_to_text_whisper(audio_file_src):
    model_size = "small"
    
    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    
    segments, info = model.transcribe(audio_file_src, beam_size=5)
    text_list = []
    for segment in segments:
        text_list.append(segment.text)
    text = ' '.join(text_list)
    return text



# ############################# claude #################################

client_2 = Anthropic(api_key=CLAUDE_API_KEY)
MODEL_NAME = "claude-3-haiku-20240307"

def get_base64_encoded_image(image):
    binary_data = image.read()
    base_64_encoded_data = base64.b64encode(binary_data)
    base64_string = base_64_encoded_data.decode('utf-8')
    return base64_string

def image_to_text(img):
    message_list = [
        {
            "role": 'user',
            "content": [
                {"type": "image", "source": {"type": "base64",
                                             "media_type": "image/jpeg", "data": get_base64_encoded_image(img)}},
                {"type": "text", "text": f"Transcribe this text. Only output the text and nothing else?"}
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
