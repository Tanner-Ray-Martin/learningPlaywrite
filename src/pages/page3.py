import streamlit as st
from PIL import Image

st.title("Page 3 - Multimedia and Layouts")

# Image
image = Image.open("sample_image.png")  # Replace with your image file
st.image(image, caption="Sample Image", use_column_width=True)

# Audio
audio_file = open("sample_audio.mp3", "rb")  # Replace with your audio file
audio_bytes = audio_file.read()
st.audio(audio_bytes, format="audio/mp3")

# Video
video_file = open("sample_video.mp4", "rb")  # Replace with your video file
video_bytes = video_file.read()
st.video(video_bytes)

# Columns
col1, col2 = st.columns(2)

with col1:
    st.header("Column 1")
    st.write("This is column 1.")

with col2:
    st.header("Column 2")
    st.write("This is column 2.")

# Expander
with st.expander("See Explanation"):
    st.write("""
        The charts above show various data visualizations.
        Expand this section to see more details.
    """)
