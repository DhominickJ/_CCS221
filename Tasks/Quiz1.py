
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


def loadImage(img_number):
    img_ = cv2.imread("Tasks/" + str(img_number) + ".jpg")
    img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)
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
        Bx_old = st.slider("Bx_old", 1, 100, 1)
        By_old = st.slider("By_old", 1, 100, 1)
        Tx = st.slider("Tx", 1, 100, 1)
        Ty = st.slider("Ty", 1, 100, 1)

    for num in range(1,6):
        img = loadImage(num)
        rows, cols, dimms = img.shape
        translated_image = translation(img, Bx_old, By_old, Tx, Ty, rows, cols)

        print_plot(translated_image)

if __name__ == '__main__':
    main()
