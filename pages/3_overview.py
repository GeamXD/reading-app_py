import streamlit as st
import logic as lg

st.set_page_config(
    page_title="Take Photo",
    page_icon="📸",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.title('Upload Pages')
for i in range(1, 5):
    try:
        st.image(f'captured/image_{i}.jpg', use_column_width=True)
    except Exception as e:
        st.error(f'Page {i} not uploaded')


bt_1, bt_2, bt_3 = st.columns(3)
with bt_1:
    if st.button('Retake Photos', use_container_width=True):
        for i in range(1, 5):
            lg.delete_file(f'captured/image_{i}.jpg')
    # switch to pages/2_TakePhoto_1.py
        st.switch_page('pages/1_TakePhoto_btn.py')
with bt_3:
    if st.button('Start Reading', use_container_width=True):
        st.switch_page('pages/4_start_reading.py')
