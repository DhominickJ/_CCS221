import numpy as np
import cv2
import matplotlib.pyplot as plt

"""
Creating Different Functions using Open CV

Note to Self: The FileName of the Image must be in the following format: 1.jpg, 2.jpg, 3.jpg, 4.jpg, 5.jpg

Group Name: CriDhomJeph

Members: Billena, Dhominick John
         Torre, Jephone Israel Jireh
         Artacho, Cristopher Ian
         Constantino, Els Dave
"""

#Translation


def rotation_(img_, angle, rows, cols):
    img_angle = np.radians(angle)
    m_rotation = np.float32([[np.cos(img_angle), -(np.sin(img_angle)), 0],
                             [np.sin(img_angle), np.cos(img_angle), 0],
                             [0, 0, 1]])

    rotated_img_ = cv2.warpPerspective(img_, m_rotation, (int(cols), int(rows)))

    return rotated_img_

def scaling_(img_, scale, rows, cols):
    # m_scaling = np.float32([[1.5, 0, 100],
    #                         [0, 1.8, 50],
    #                         [0, 0, 1]])

    # scaled_img_ = cv2.warpPerspective(img_, m_scaling, (rows*scale, cols*scale))
    # rows, cols, dimms = scaled_img_.shape
    # return scaled_img_

    resized_img_ = cv2.resize(img_, None, fx = scale, fy = scale, interpolation= cv2.INTER_CUBIC)
    rows, cols, dimms = resized_img_.shape

    print(rows)
    print(cols)

    return resized_img_
    

def shearing(shear, img_, rows, cols, type):
    #Create a matrix for shearing

    if(type == 1):
        m_shearing_x = np.float32([[1, shear, 0],
                                [0, 1, 0],
                                [0, 0, 1]])
        sheared_img_ = cv2.warpPerspective(img_, m_shearing_x, (rows, cols))

    else:
        m_shearing_y = np.float32([[1, 0, 0],
                                    [shear, 1, 0],
                                    [0, 0, 1]])
        sheared_img_ = cv2.warpPerspective(img_, m_shearing_y, (rows, cols))
    
    

    return sheared_img_

def reflection_(img_, rows, cols):
    # Using the original method

    # m_reflection = np.float32([[1, 0, 0],
    #                             [0, -1, rows],
    #                             [0, 0, 1]])

    # m_reflection_normal = np.float32([[-1, 0, cols],
    #                                   [0, 1, 0],
    #                                   [0, 0, 1]])

    # reflected_img_ = cv2.warpPerspective(img_, m_reflection_normal, (int(rows), int(cols)))

    reflected_img_flipped_ = cv2.flip(img_, 0)

    return reflected_img_flipped_
    # return reflected_img_

def read_img(img_number):
    img_ = cv2.imread(str(img_number) + ".jpg")
    img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)
    return img_

def show_plot(new_image):
    plt.axis('off')
    plt.imshow(new_image)
    plt.show()

def main():
    print("Available Functions:")
    print("1. Translation")
    print("2. Rotation")
    print("3. Scaling")
    print("4. Shearing")
    print("5. Reflection")
    print("6. Exit")
    choice = int(input("What function do you want to do?: "))
     
    if(choice == 1):
        x = int(input("X Coordinates to Move Location: "))
        y = int(input("Y Coordinates to Move Location: "))
        for img_number in range(1, 6): #Replace the value of the range if you wish to place a custom number of items
            img_ = read_img(img_number)
            rows, cols, dimm = img_.shape
            translated_image = translation_(img_, x, y, rows, cols)
            show_plot(translated_image)
    elif(choice == 2):
        angle = int(input("Rotation Degrees?: ")) # This prompt can be moved to the for loop in order to define the angle differently for each image
        for img_number in range(1, 6):
            img_ = read_img(img_number)
            rows, cols, dimms = img_.shape
            img_rotated = rotation_(img_, angle, rows, cols)
            show_plot(img_rotated)
    elif(choice == 3):
        scale = int(input("How much do you want to Scale?: "))
        for img_number in range(1, 6):
            img_ = read_img(img_number)
            rows, cols, dimms = img_.shape
            print("Image " + str(img_number))
            img_scaled_ = scaling_(img_, scale, rows, cols)
            show_plot(img_scaled_)
    elif(choice == 4):
        type = int(input("Shearing Type (1 = x or 2 = y): "))
        shear = float(input("How much do you want to shear? (0.5 - 2.0): "))
        for img_number in range(1, 6):
            img_ = read_img(img_number)
            rows, cols, dimms = img_.shape
            img_sheared_ = shearing(shear, img_, rows, cols, type)
            show_plot(img_sheared_)
    elif(choice == 5):
        for img_number in range(1, 6):
            img_ = read_img(img_number)
            rows, cols, dimms = img_.shape
            img_reflected_ = reflection_(img_, rows, cols)
            show_plot(img_reflected_)
    elif(choice == 6):
        print("Exiting...")
        exit()
    else:
        print("Invalid Choice")

if __name__ == '__main__':
    main()
