import streamlit as st
import logic as lg
from st_audiorec import st_audiorec
from faster_whisper import WhisperModel



st.set_page_config(
    page_title="Reading App",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded")

###################### SLIDER ###############################
with st.sidebar:
    # input = st.text_input('Enter text')
    st.subheader('Upload an Image')
    img = st.file_uploader('Image uploads')
    wav_audio_data = st_audiorec()
    # ln = st.radio('Select a language', ['English', 'Danish'])

############## MAIN APP #####################

_, colB, _ = st.columns(3, gap='small')
with colB:
    st.title('Reading APP 📖')

if img is not None:
    with colB:
        st.image(img, width=400)
    t_btn = st.button('Load text from image')
    if t_btn:
        extracted_text = lg.image_to_text(img)
        st.write('')
        st.subheader('Text')
        st.write(f'{extracted_text}')
        st.session_state['text_from_image'] = extracted_text

if wav_audio_data is not None:
    with open('audio.wav', mode='bw') as audio_file:
        audio_file.write(wav_audio_data)


###### TEXT TO SPEECH ###########
st.write('')
st.write('')
bt_1, bt_2, bt_3 = st.columns(3)
with bt_1:
    opn_tts_btn = st.button('Open-(text-to-speech)')
with bt_2:
    opn_stt_btn = st.button('Open-(speech-to-text)')
with bt_3:
    whis_stt_btn = st.button('Whisp-(speech-to-text)')

if opn_tts_btn:
    lg.text_to_speech_openai(st.session_state['text_from_image']) # only this has text to speech
    st.subheader('Audio(from extracted text)')
    st.audio('speech.mp3', format='audio/mp3')

if opn_stt_btn:
    text_0 = lg.speech_to_text('audio.wav')
    st.write('')
    st.subheader('Transcribed Text(from audio)')
    st.write(text_0)

if whis_stt_btn:
    text = lg.speech_to_text_whisper('audio.wav') # speech to text
    st.write('')
    st.subheader('Transcribed Text(from audio)')
    st.write(text)