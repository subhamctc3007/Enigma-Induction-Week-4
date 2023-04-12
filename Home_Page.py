import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Page Configuration
st.set_page_config(layout="wide", page_title="My App", page_icon=":frog:")

# Function to add Lottie animation in page
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Assets
lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_4kx2q32n.json")
file = 'Media/bicycle.webp'

# Sidebar basics
st.sidebar.write("Upload Your File")
file_type = st.sidebar.radio("Choose file type", ("Image", "Video"))

# Header
with st.container():
    text_column, lottie_column = st.columns((2,1))
    with text_column:
        st.title("Hello There.. :wave:")
        st.subheader("I am Subham Mishra :smile:, from Dept of Electronics & Telecommunication Engg. I am really passionate about AI/ML and Web Developement. I would love to learn all about it.")
        st.write("This App has an option in sidebar to upload an Image or a Video and display it along with a provided caption")
    # Adding a Lottie Animation
    with lottie_column:
        st_lottie(lottie_coding, height=300, key="coding")
    st.write("File you upload appears here: ")

# Main
with st.container():
    media_column, empty_column = st.columns((2,1))
    caption = "" # Setting caption to empty string
    # Showing the Image
    if file_type == "Image":
        st.sidebar.write("Image")
        option = st.sidebar.selectbox('Choose..', ('Upload a Picture', 'Take a Picture'))
        if option == 'Take a Picture':
            with media_column:
                picture = st.sidebar.camera_input('Take a Picture')
                caption = st.sidebar.text_input('Caption: ', 'This is a Caption') # caption input
                if picture is not None and caption != "":
                    st.image(picture, caption=caption)
        else:
            file = st.sidebar.file_uploader("Choose an Image", type=["png", "jpg", "jpeg", "webp"])
            caption = st.sidebar.text_input('Caption for Image: ', 'This is a Caption') # caption input
            if file is not None and caption != "":
                with media_column:
                    st.image(file, caption=caption)
                    st.balloons()
    # Showing the Video
    elif file_type == "Video":
        media_column, empty_column = st.columns((2,1))
        st.sidebar.write("Video")   
        file = st.sidebar.file_uploader("Choose a Video", type=["mov", "mp4"])
        caption = st.sidebar.text_input('Caption: ', 'This is a Caption') # caption input
        if file is not None and caption != "":
            with media_column:
                video_bytes = file.read()
                st.video(video_bytes)
                st.markdown(f"<center>{caption}</center>", unsafe_allow_html=True)
                st.balloons()