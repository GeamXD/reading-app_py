import base64
import streamlit as st
from audio_recorder_streamlit import audio_recorder
import logic as lg
from st_audiorec import st_audiorec

st.set_page_config(
    page_title="Start Reading",
    page_icon="📖",
    layout="centered",
    initial_sidebar_state="collapsed")

# page_Text = {}

def get_text():
    page_text = {}
    for i in range(1, 5):
        try:
            page_text[f'page_{i}'] = lg.image_to_text(f'captured/image_{i}.jpg')
        except Exception as e:
            print(e)
    return page_text

# Auto play function
def auto_play_audio(audio_file):
    with open(audio_file, 'rb') as audio_file:
        audio_bytes = audio_file.read()
    base64_audio = base64.b64encode(audio_bytes).decode('utf-8')
    audio_html = f'<audio src="data:audio/mp3;base64, {base64_audio}" controls autoplay>'
    st.markdown(audio_html, unsafe_allow_html=True)




######## Front-end #########
def start_reading(page_Text):
    st.subheader('Start reading')
    
    ### initiates recorder
    recorded_audio = st_audiorec()

    ### Check if recorded audio is available
    if recorded_audio:
        audio_file = 'audio.mp3'
        with open(audio_file, 'wb') as f:
            f.write(recorded_audio)
    
        ## Create the transcribed text using openai
        transcribed_text = lg.speech_to_text(audio_file)
        
        # replace with something visually appealing
        with st.container(border=True):
            st.subheader('Transcribed Text')
            st.write(transcribed_text)
        
        # Get text from images
        # page_Text = get_text()

        # Get Comparison from ai
        ai_response, ai_score = lg.feedback(page_Text, transcribed_text)
        
        # Store reading score
        st.session_state['reading_score'] = ai_score

        # Store ai response
        st.session_state['ai_response'] = ai_response
    
        # Audio file name for tts
        response_audio_file = 'audio_response.mp3'

        ## functiion below saves response audio to locale
        lg.text_to_speech(ai_response, response_audio_file)

        # Autoplays ai response
        auto_play_audio(response_audio_file)

        ## Writes ai response
        with st.container(border=True):
            st.subheader('AI Response')
            st.write(ai_response)

page_text = get_text()
start_reading(page_Text=page_text)

bt_1, bt_2, bt_3 = st.columns(3)
with bt_1:
    if st.button('Feedback', use_container_width=True):
        st.switch_page('pages/5_feedback.py')
with bt_3:
    if st.button('Go to Overview', use_container_width=True):
        st.switch_page('pages/3_overview.py')

