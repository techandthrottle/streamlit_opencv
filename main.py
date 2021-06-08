import cv2
import numpy as np
import streamlit as st

st.title('DynoWord Streamlit and OpenCV Tutorial')

st.write("""
    Streamlit and OpenCV image manipulation. Applying a threshold to an image to further simplify visual data analysis in OpenCV.
""")

st.sidebar.header('User Input Features')
uploaded_img = st.sidebar.file_uploader("Upload your image", type=["png","jpg","jpeg"])
isGray = st.sidebar.checkbox('Convert to Grayscale')
