import numpy as np
import cv2
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image

# """
# Creating Different Functions using Open CV

# Note to Self: The FileName of the Image must be in the following format: 1.jpg, 2.jpg, 3.jpg, 4.jpg, 5.jpg

# Group Name: CriDhomJeph

# Members: Billena, Dhominick John
#          Torre, Jephone Israel Jireh
#          Artacho, Cristopher Ian
#          Constantino, Els Dave
# """

def translation_(img_, x, y, rows, cols):

    #function to shift an image
    m_translation = np.float32([[1, 0, x],
                                [0, 1, y],
                                [0, 0, 1]])

    translated_img = cv2.warpPerspective(img_, m_translation, (rows, cols))

    return translated_img

def rotation_(img_, angle, rows, cols):
    #function to rotate an image
    img_angle = np.radians(angle)
    m_rotation = np.float32([[np.cos(img_angle), -(np.sin(img_angle)), 0],
                             [np.sin(img_angle), np.cos(img_angle), 0],
                             [0, 0, 1]])

    rotated_img_ = cv2.warpPerspective(img_, m_rotation, (int(cols), int(rows)))

    return rotated_img_

def scaling_(img_, scale, rows, cols):
    #function to scale an image
    # Longhand method for scaling:
    m_scaling = np.float32([[1.5, 0, scale],
                            [0, 1.5, scale],
                            [0, 0, 1]])
    scaled_img_ = cv2.warpPerspective(img_, m_scaling, (rows*-scale, cols*-scale))
    rows, cols, dimms = scaled_img_.shape
    return scaled_img_

    #Shorthand method for scaling:
    # resized_img_ = cv2.resize(img_, None, fx = scale, fy = scale, interpolation= cv2.INTER_CUBIC)
    # rows, cols, dimms = resized_img_.shape

    # print(rows)
    # print(cols)

    # return resized_img_
    

def shearing(shear, img_, rows, cols, type):
    #function to shear an image

    if(type == 1):#types of shearing
        m_shearing_x = np.float32([[1, shear, 0], #Create a matrix for type 1 shearing
                                [0, 1, 0],
                                [0, 0, 1]])
        sheared_img_ = cv2.warpPerspective(img_, m_shearing_x, (rows, cols))

    else:
        m_shearing_y = np.float32([[1, 0, 0], #Create a matrix for shearing
                                    [shear, 1, 0],
                                    [0, 0, 1]])
        sheared_img_ = cv2.warpPerspective(img_, m_shearing_y, (rows, cols))
    
    

    return sheared_img_

def reflection_(img_, rows, cols):
    #function for reflecting an image

    #Longhand method for flipping the image upside down:

    # m_reflection = np.float32([[1, 0, 0],
    #                             [0, -1, rows],
    #                             [0, 0, 1]])
    # m_reflection_normal = np.float32([[-1, 0, cols],
    #                                   [0, 1, 0],
    #                                   [0, 0, 1]])
    # reflected_img_ = cv2.warpPerspective(img_, m_reflection_normal, (int(rows), int(cols)))
    # return reflected_img_


    #shorthand method for flipping the image upside down:
    reflected_img_flipped_ = cv2.flip(img_, 0)
    return reflected_img_flipped_
    

def read_img(image): #reads the image name, used to allow the image to be processed for the whole 
    # img_ = cv2.imread("Tasks/" + str(image) + ".jpg")
    converted_img = np.array(image.convert('RGB'))
    img_ = cv2.cvtColor(converted_img, cv2.COLOR_BGR2RGB)
    return img_

def show_plot(new_image): #plots the image and prints it in a streamlit app
    plt.axis('off')
    plt.imshow(new_image)
    st.pyplot(plt.gcf())

def main():
    with st.sidebar:
        st.title("Image Transformation")
        options = ['Translation', 'Shearing', 'Reflection', 'Rotation', 'Scaling']
        choice = st.selectbox("Choose a Function: ", options, key="act3.selectbox")
        uploaded_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])
        # image = uploaded_file.getvalue()

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
    else:
        st.sidebar.error("Upload an Image")
            
    if(choice == 'Translation'):
        with st.sidebar:
            x = st.slider("X Coordinates to Move Location: ", 1, 10, 10, key="x.trans.slider")
            y = st.slider("Y Coordinates to Move Location: ", 1, 10, 5, key="y.trans.slider")
        img_ = read_img(image)
        rows, cols, dimm = img_.shape
        translated_image = translation_(img_, x, y, rows, cols)
        show_plot(translated_image)
    elif(choice == 'Rotation'):
        with st.sidebar:
            angle = st.slider("Rotation Degrees?: ", 1, 360, 1, key="angle.rot.slider")
        img_ = read_img(image)
        rows, cols, dimms = img_.shape
        img_rotated = rotation_(img_, angle, rows, cols)
        show_plot(img_rotated)
    elif(choice == 'Scaling'):
        with st.sidebar:
            scale = st.slider("How much do you want to Scale?: ", -10, 10, 1, key="scale.scal.slider")
        img_ = read_img(image)
        rows, cols, dimms = img_.shape
        img_scaled_ = scaling_(img_, scale, rows, cols)
        show_plot(img_scaled_)
    elif(choice == 'Shearing'):
        with st.sidebar:
            type = st.selectbox("Shear Type: ", ("Horizontal", "Vertical"), key="shear.type.selectbox")
            shear = st.slider("How much do you want to shear? (0.5 - 2.0): ", 0.5, 2.0, 0.5, key="shear.scal.slider")
        img_ = read_img(image)
        rows, cols, dimms = img_.shape
        img_sheared_ = shearing(shear, img_, rows, cols, type)
        show_plot(img_sheared_)
    elif(choice == 'Reflection'):
        img_ = read_img(image)
        rows, cols, dimms = img_.shape
        img_reflected_ = reflection_(img_, rows, cols)
        show_plot(img_reflected_)
    else:
        print("Invalid Choice")

if __name__ == '__main__':
    main()

