import streamlit as st


st.set_page_config(
    page_title="FeedBack",
    page_icon="📖",
    layout="centered",
    initial_sidebar_state="collapsed")

st.title('Feedback')
st.caption('Provide feedback on the accuracy of the spoken text.')


try:
    score = st.session_state.get('reading_score')
    st.markdown(f'#### Score: {score}')
except:
    pass

with st.container(border=True):
    try:
        st.markdown(st.session_state['ai_response'])
    except:
        pass


bt_1, bt_2, bt_3 = st.columns(3)
with bt_1:
    if st.button('Retake Exercise', use_container_width=True):
    # remove all photos from session state
        st.session_state['ai_response'] = None
        st.session_state['reading_score'] = None
    # switch to pages/2_TakePhoto_1.py
        st.switch_page('pages/4_start_reading.py')
with bt_3:
    if st.button('Go to Overview', use_container_width=True):
        st.switch_page('pages/3_overview.py')
