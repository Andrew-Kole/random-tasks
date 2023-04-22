"""
The following program produces the same exact web app which we built in today's coding exercise. The only difference is that the code has been refactored (i.e., better organized) by moving the grayscale functionality into a function in a separate converter.py file:

converter.py:

from PIL import Image
 
 
def convert_image(input_image):
    """"""Gets a PIL image file and returns its grayscale version"""""""
    img = Image.open(input_image)
    gray_img = img.convert('L')


We also have the main.py file where we call the above function to get grayscale images for both the camera image and the uploaded image:

main.py:

# Note: This script runs only on a local IDE with "streamlit run main.py"
import streamlit as st
 
from converter import convert_image
 
st.subheader("Color to Grayscale Converter")
 
# Create a file uploader component allowing the user to upload a file
uploaded_image = st.file_uploader("Upload Image")
 
with st.expander("Start camera"):
    camera_image = st.camera_input("Camera")
 
if camera_image:
    # Supply camera_image to convert_image to get the grayscale version
    gray_camera_image = convert_image(camera_image)
    st.image(gray_camera_image)
 
# Check if the image exists meaning the user has uploaded a file
if uploaded_image:
    # Supply camera_image to convert_image to get the grayscale version
    gray_uploaded_image = convert_image(camera_image)
    st.image(gray_uploaded_image)
However, there is one error in one of the above scripts. Hunt it down and fix it.
"""

# Note: This script runs only on a local IDE with "streamlit run main.py"
import streamlit as st
import sys
sys.path.insert(1, "C://Users/Acer/PycharmProjects/pythonProject")
import modules.bf_day19task1_func as mbf

st.subheader("Color to Grayscale Converter")

# Create a file uploader component allowing the user to upload a file
uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start camera"):
    camera_image = st.camera_input("Camera")

if camera_image:
    # Supply camera_image to convert_image to get the grayscale version
    gray_camera_image = mbf.convert_image(camera_image)
    st.image(gray_camera_image)

# Check if the image exists meaning the user has uploaded a file
if uploaded_image:
    # Supply camera_image to convert_image to get the grayscale version
    gray_uploaded_image = mbf.convert_image(uploaded_image)
    st.image(gray_uploaded_image)

