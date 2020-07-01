import cv2
import numpy as np
import streamlit as st

st.title('OpenCV Thresholding')

st.write("""
    Adding threshold to images to further simplify visual data analysis.
""")

st.sidebar.header('User Input Features')
uploaded_img = st.sidebar.file_uploader("Upload your image", type=["png","jpg","jpeg"])
#file_name = cv2.imread(st.sidebar.text_input("Copy the uploaded filename and location"))
isGray = st.sidebar.checkbox('Convert to Grayscale')

if uploaded_img is not None:
    file_bytes = np.asarray(bytearray(uploaded_img.read()), dtype=np.uint8)
    opencv_img = cv2.imdecode(file_bytes,1)
    #cv2.imwrite('input.jpg', cv2.resize(uploaded_img, (50,50), interpolation=cv2.INTER_LINEAR))
    #test_img = cv2.imread('input.jpg')
    if isGray:
        new_img = cv2.cvtColor(opencv_img, cv2.COLOR_BGR2GRAY)
        thresh_type = st.sidebar.selectbox('Threshold Type',('Ordinary','Adaptive Threshold'))
        if thresh_type == 'Ordinary':
            thresh_value = st.sidebar.slider('Threshold Value', 1, 255, 12)
            retval, data = cv2.threshold(new_img, thresh_value, 255, cv2.THRESH_BINARY)
        else:
            block_size = st.sidebar.slider('Block Size', 3, 255, 115, 2)
            data = cv2.adaptiveThreshold(new_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, 1)
    else:

        new_img = opencv_img
        thresh_value = st.sidebar.slider('Threshold Value', 1, 255, 12)
        retval, data = cv2.threshold(new_img, thresh_value, 255, cv2.THRESH_BINARY)

    st.subheader('Original Image')
    st.image(new_img, caption='Ouput Image')
    
    cv2.imwrite('output.jpg',data)
    st.subheader('Output Image')
    st.image('output.jpg', caption='Ouput Image')
