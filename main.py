# Note: This script runs only on a local IDE with "streamlit run main.py"
import streamlit as st
from converter import converter_image

st.title("Color to Grayscale Converter")

# Create a file uploader component allowing the user to upload a file
uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start camera"):
    camera_image = st.camera_input("Camera")

if camera_image:
    # Supply camera image to convert_image to get the grayscale version
    gray_camera_img = converter_image(camera_image)
    # Display the grayscale image on the webpage
    st.image(gray_camera_img)

if uploaded_image:
    # Convert the image to grayscale
    gray_uploaded_img = converter_image(uploaded_image)
    # Display the grayscale image on the webpage
    st.image(gray_uploaded_img)
