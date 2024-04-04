import streamlit as st
from logic import image_to_text
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
    img = st.file_uploader('Upload an image')
    wav_audio_data = st_audiorec()
    ln = st.radio('Select a language', ['English', 'Danish'])

############## MAIN APP #####################

_, colB, _ = st.columns(3, gap='small')
with colB:
    st.title('Reading APP📖')

if img is not None:
    _, colb, _ = st.columns((1, 2, 1), gap='small')
    with colb:
        st.image(img, use_column_width=True)
        res = image_to_text(img, lang=ln)
        st.write(f'Image Description: {res}')

# if input is not None:
    # st.write(f'Input Text: {input}')

if wav_audio_data is not None:
    st.audio(wav_audio_data, format='audio/wav')
#     res = speech_to_text(wav_audio_data, lang=ln)
# st.audio()

model_size = "tiny"

# model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
# or run on CPU with INT8
# model = WhisperModel(model_size, device="cpu", compute_type="int8")

segments, info = model.transcribe("audio.mp3", beam_size=5)

print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))