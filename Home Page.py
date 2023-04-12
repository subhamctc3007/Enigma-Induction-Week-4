import streamlit as st
import requests
from streamlit_lottie import st_lottie
import cv2

# creating the page
st.set_page_config(layout="wide", page_title="My App", page_icon=":frog:")

# Function definitions
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Assets
lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_4kx2q32n.json")
file = 'Media/bicycle.webp'

# Sidebar
st.sidebar.write("Upload Your File")
file_type = st.sidebar.radio("Choose file type", ("Image", "Video"))

# Header
with st.container():
    text_column, lottie_column = st.columns((2,1))
    with text_column:
        st.title("Hello There.. :wave:")
        st.subheader("""I am Subham Mishra :smile:, from Dept of Electronics & Telecommunication Engg. I am really passionate about AI/ML and Web Developement. I would love to learn all about it.""")
        st.write("""This App has an option in sidebar to upload an Image or a Video and display it along with a provided caption""")
    # Adding a Lottie Animation
    with lottie_column:
        st_lottie(lottie_coding, height=300, key="coding")

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
            caption = st.sidebar.text_input('Caption: ', 'This is a Caption') # caption input
            if file is not None and caption != "":
                with media_column:
                    st.image(file, caption=caption)
                    st.balloons()
    # Showing the Video
    elif file_type == "Video":
        media_column, empty_column = st.columns((2,1))
        st.sidebar.write("Video")
        option = st.sidebar.selectbox('Choose..', ('Upload a Video', 'Capture a Video'))
        if option == 'Capture a Video':
            st.sidebar.write("Loading..")
            st.sidebar.write("Press 'r' to Start and Stop Recording")
            # Recording a Video
            with media_column:
                cap = cv2.VideoCapture(0)

                height = 720
                width = 1280
                frame_rate = 30.0

                cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
                cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

                fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
                writer = cv2.VideoWriter("Video.mp4", fourcc, frame_rate, (width, height))
                recording = False

                while True:
                    ret, frame = cap.read()
                    if ret:
                        cv2.imshow("Video", frame)
                        #st.sidebar.video(frame)
                        if recording:
                            writer.write(frame)
                    key = cv2.waitKey(1)
                    if key == ord('r'):
                        recording = not recording
                        if recording:
                            st.sidebar.write("Recording Started")
                            print("Recording Started")
                        else:
                            st.sidebar.write("Recording Stopped")
                            print("Recording Started")
                            break
                cap.release()
                writer.release()
                cv2.destroyAllWindows()
                caption = st.sidebar.text_input('Caption: ', 'This is a Caption') # caption input

                file = open('Video.mp4', 'rb')
                video_bytes = file.read()
                st.video(video_bytes)
        else:   
            file = st.sidebar.file_uploader("Choose a Video", type=["mov", "mp4"])
            caption = st.sidebar.text_input('Caption: ', 'This is a Caption') # caption input
            if file is not None and caption != "":
                with media_column:
                    video_bytes = file.read()
                    st.video(video_bytes)
                    st.markdown(f"<center>{caption}</center>", unsafe_allow_html=True)
                    st.balloons()