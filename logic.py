import os
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


def claude_client(api_key):
    return Anthropic(api_key=api_key)

def openai_client(api_key):
    return OpenAI(api_key=api_key)


def speech_to_text(audio_path):
    client = openai_client(OPEN_API_KEY)
    with open(audio_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model='whisper-1',
            file=audio_file)
    return transcript.text


def text_to_speech(text, audio_path) -> None:
    client = openai_client(OPEN_API_KEY)
    response = client.audio.speech.create(
    model="tts-1",
    voice="nova",
    input=text
    )
    response.stream_to_file(audio_path)

def get_base64_encoded_image(image):
    binary_data = image.read()
    base_64_encoded_data = base64.b64encode(binary_data)
    base64_string = base_64_encoded_data.decode('utf-8')
    return base64_string

def image_to_text(img):

    client = claude_client(CLAUDE_API_KEY)
    message_list = [
        {
            "role": 'user',
            "content": [
                {"type": "image", "source": {"type": "base64",
                                             "media_type": "image/jpeg", "data": get_base64_encoded_image(img)}},
                {"type": "text", "text": "Transcribe this to text. Only output the text and nothing else?"}
            ]
        }
    ]

    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=512,
        messages=message_list,
        temperature=0.2,
    )
    return response.content[0].text


######## modified ai response ############
def feedback(page_Text, spoken_text):
    client = claude_client(CLAUDE_API_KEY)
    
    prompt = f"""Compare text in {page_Text} and spoken text in {spoken_text}.
    Provide feedback on the accuracy of the {spoken_text} based on page number in {page_Text} alone.
    Emphasis should be placed that text matches the page number and accompanying text. Be brief
    Feedback should be encouraging as you are accessing a child's reading abilities. Be brief
    Always respond in an encouraging way. Be brief and concise.
    Provide feedback on errors and improvement suggestions. Be brief and concise.
    No need to repeat what is in matching page.
    You are making a conversation with a child so be conversational in response but brief.
    """
    
    feed_message = {"role": "user", "content": [{"type": "text", "text": prompt}]}

    feed_response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1024,
        temperature=0.7,
        messages=[feed_message])
    
    
    score_message = {"role": "user", "content": [{"type": "text", "text": f"""
                                            Compare text in {page_Text} and spoken text in {spoken_text}.
                                            Take note that spoken words matches content in page number.
                                            and provide an assessment score within 1 - 10 for accuracy. Only provide the score and nothing else.
                                        """}]}
    
    
    score_response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=512,
        messages=[score_message],
        temperature=0.1)
    
    ai_feedback_text = feed_response.content[0].text
    ai_score_text = score_response.content[0].text

    return ai_feedback_text, ai_score_text




# ############ FAST WHISPER MODEL ###############################
# def speech_to_text_whisper(audio_file_src):
#     model_size = "small"
    
#     model = WhisperModel(model_size, device="cpu", compute_type="int8")
    
#     segments, info = model.transcribe(audio_file_src, beam_size=5)
#     text_list = []
#     for segment in segments:
#         text_list.append(segment.text)
#     text = ' '.join(text_list)
#     return text
