import streamlit as st


st.set_page_config(
    page_title="Take Photo",
    page_icon="📸",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.title('Upload Pages')
for i in range(1, 5):
    if st.session_state.get(f'photo_{i}'):
        st.image(st.session_state[f'photo_{i}'], use_column_width=True)
    else:
        st.error(f'Page {i} not uploaded')




bt_1, bt_2, bt_3 = st.columns(3)
with bt_1:
    if st.button('Retake Photos', use_container_width=True):
    # remove all photos from session state
        st.session_state['photo_1'] = None
        st.session_state['photo_2'] = None
        st.session_state['photo_3'] = None
        st.session_state['photo_4'] = None
        st.session_state['ai_response'] = None
        st.session_state['reading_score'] = None
    # switch to pages/2_TakePhoto_1.py
        st.switch_page('pages/1_TakePhoto_btn.py')
with bt_3:
    if st.button('Start Reading', use_container_width=True):
        st.switch_page('pages/4_start_reading.py')
