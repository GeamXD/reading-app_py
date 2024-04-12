import streamlit as st


st.set_page_config(
    page_title="Reading App",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="collapsed")


############# Intro Page ############################
subheader_col = st.columns(3)
subheader_col[1].subheader('Reading App 📖')

_, newcol, _ = st.columns([1, 3, 1])
with newcol:
    st.image('images/pic1.jpg')
    st.write('')
    st.markdown('###### **Take your reading skills to the next level with our Reading App.** ')
    
    
_, col1, _ = st.columns(3, gap='large')
with col1:
    if st.button('Start', use_container_width=True):
        st.switch_page('pages/1_TakePhoto_btn.py')
