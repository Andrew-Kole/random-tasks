import streamlit as st
from PIL import Image


with st.expander("Start camera"):
    #start camera
    camera_image = st.camera_input("Camera")

if camera_image:
    #create a pillow img instance
    img = Image.open(camera_image)

    #converting pillow img to grayscale
    grey_img = img.convert("L")

    #show it on web page
    st.image(grey_img)