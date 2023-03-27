
# """ 
# Group 1: CriDhomJephEls

# Name: Billena, Dhominick John
#       Artacho, Cristopher Ian
#       Torre, Jephone Israel Jireh
#       Constantino, Els Dave

# Filename: No. of Image. 1.jpg
# """

import matplotlib.pyplot as plt
import numpy as np
import cv2 
import streamlit as st
from PIL import Image


def loadImage(img_):
    converted_img = np.array(img_.convert('RGB'))
    img_ = cv2.cvtColor(converted_img, cv2.COLOR_BGR2RGB)
    return img_

def translation(img_, Bx_old, By_old, Tx, Ty, rows, cols):

    Tx_new = Bx_old + Tx
    Ty_new = By_old + Ty

    matrix_translation = np.float32([[1, 0, Tx_new],
                                    [0, 1, Ty_new],
                                    [0, 0, 1]]) 


    translated_img_ = cv2.warpPerspective(img_, matrix_translation, (rows, cols))
 
    return translated_img_

def print_plot(new_image):
    plt.axis('off')
    plt.imshow(new_image)
    st.pyplot(plt.gcf())

def main():
    
    with st.sidebar:
        uploaded_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])

        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            Bx_old = st.slider("Bx_old", 1, 100, 1)
            By_old = st.slider("By_old", 1, 100, 1)
            Tx = st.slider("Tx", 1, 100, 1)
            Ty = st.slider("Ty", 1, 100, 1)

            img = loadImage(image)
            rows, cols, dimms = img.shape
            translated_image = translation(img, Bx_old, By_old, Tx, Ty, rows, cols)

            print_plot(translated_image)
        else:
            st.sidebar.error("Upload an Image")

if __name__ == '__main__':
    main()
