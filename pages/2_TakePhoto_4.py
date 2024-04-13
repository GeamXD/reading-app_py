import streamlit as st

st.set_page_config(
    page_title="Take Photos",
    page_icon="📸",
    layout="centered",
    initial_sidebar_state="collapsed")


st.markdown('##### Take a Picture')
picture = st.camera_input("Image Captured", label_visibility='collapsed')

if picture:
    with open('captured/image_4.jpg', 'wb') as f:
        pic = picture.read()
        f.write(pic)

st.warning('Photos Limit Reached. Please proceed to the next step.')

bt_1, bt_2, bt_3 = st.columns(3)
with bt_1:
    if st.button('Start Reading', use_container_width=True):
        st.switch_page('pages/4_start_reading.py')
with bt_3:
    if st.button('Go to Overview', use_container_width=True):
        st.switch_page('pages/3_overview.py')