
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.spatial import Delaunay
import tensorflow as tf
import streamlit as st

#to get the points and be used on a 3D object function
def plt_basic_object_(points):

    tri = Delaunay(points). convex_hull

    shape_fig = plt.figure(figsize=(8, 8))
    ax = shape_fig.add_subplot(111, projection = '3d') #111 means 1x1 grid and projection '3d' enables the z axis
    S = ax.plot_trisurf(points[:,0], points[:,1], points[:,2], #.plot trisurf means plot a triangulated surface
                        triangles = tri,
                        shade = True, cmap = cm.rainbow, lw=0.5)
    
    
    ax.set_xlim3d (-5, 5) #sets the graph of x from -5 to 5
    ax.set_ylim3d (-5, 5)  #sets the graph of y from -5 to 5
    ax.set_zlim3d (-5, 5)  #sets the graph of z from -5 to 5


    ax.set_xlabel ("X Axis") #label for the x Axis
    ax.set_ylabel ("Y Axis") #label for the Y Axis
    ax.set_zlabel ("Z Axis")  #label for the Z axis

    st.pyplot(fig=shape_fig)


#function for cube
def _cube_(bottom_lower =(0, 0, 0), side_length = 5):

    bottom_lower = np.array(bottom_lower) #bottom_lower becomes an array containing the values [0, 0, 0]

    points = np.vstack([ #concatenates all values below vertically
        bottom_lower,  #value will be [0, 0, 0] and located at the middle
        bottom_lower + [0, side_length, 0], #value will be [0, 3, 0] 
        bottom_lower + [side_length, side_length, 0], #value will be [3, 3, 0]
        bottom_lower + [side_length, 0, 0], #value will be [3, 0, 0]
        bottom_lower + [0, 0, side_length], #value will be [0, 0, 3]
        bottom_lower + [0, side_length, side_length], #value will be [0, 3, 3]
        bottom_lower + [side_length, side_length, side_length], #value will be [3, 3, 3]
        bottom_lower + [side_length, 0, side_length], #value will be [3, 0, 3]
        bottom_lower,   #value will be [0, 0, 0]
        #note that using np.vstack will not destroy the array and split them 
    ])

     
    return points


#function for triangle
def triangle(bottom_lower =(0, 0, 0), side_length = 5, negative = -5):

    bottom_lower = np.array(bottom_lower) #bottom_lower becomes an array containing the values [0, 0, 0]

    points = np.vstack([ #concatenates all values below vertically
        bottom_lower,  #value will be [0, 0, 0] and located at the middle
        bottom_lower + [0, side_length, 0], #value will be [0, 3, 0] 
        bottom_lower + [side_length, 0, 0], #value will be [3, 0, 0]
        bottom_lower + [0, negative, 0], #value will be [0, -3, 0]
        bottom_lower + [negative, 0, 0], #value will be [-3, 0, 0]
        bottom_lower + [0, 0, side_length], #value will be [0, 0, 3]
        bottom_lower,   #value will be [0, 0, 0]
        #note that using np.vstack will not destroy the array and split them 
    ])

    return points

#function for diamond
def diamond(bottom_lower =(0, 0, 0), side_length_top = 5, negative_top = -5, side_length = 3, negative = 3):

    bottom_lower = np.array(bottom_lower) #bottom_lower becomes an array containing the values [0, 0, 0]

    points = np.vstack([ #concatenates all values below vertically
        bottom_lower,  #value will be [0, 0, 0] and located at the middle
        bottom_lower + [0, negative, 0], #value will be [0, -3, 0] 
        bottom_lower + [0, 0, side_length_top], #value will be [0, 0, -5]
        bottom_lower + [side_length, 0, 0], #value will be [3, 0, 0]
        bottom_lower + [0, 0, negative_top], #value will be [0, 0, -5]
        bottom_lower + [negative, 0, 0], #value will be [-3, 0, 0]
        bottom_lower + [0, side_length, 0],   #value will be [0, 3, 0]
        bottom_lower
        #note that using np.vstack will not destroy the array and split them 
    ])
    return points

#function for prism
def prism(bottom_lower =(0, 0, 0), side_length = 3, negative = 3):

    bottom_lower = np.array(bottom_lower) #bottom_lower becomes an array containing the values [0, 0, 0]

    points = np.vstack([ #concatenates all values below vertically
        bottom_lower,  #value will be [0, 0, 0] and located at the middle
        bottom_lower + [0, side_length, 0], #value will be [0, 3, 0] 
        bottom_lower + [side_length, side_length, 0], #value will be [3, 3, 0]
        bottom_lower + [side_length, negative, 0], #value will be [3, -3, 0]
        bottom_lower + [negative, negative, 0], #value will be [-3, -3, 0]
        bottom_lower + [negative, side_length, 0], #value will be [-3, 3, 0]
        bottom_lower + [0, side_length, side_length],   #value will be [0, 3, 3]
        bottom_lower + [0, 0, 3], #value will be [0, 0, 3]
        bottom_lower + [0, negative, side_length], #value will be [0, -3, 3]
        bottom_lower #value will be [0, -3, 3]
        #note that using np.vstack will not destroy the array and split them 
    ])
     
    return points

def rotate_shape(points, angle, type):

    angle = float(angle) #converts the angle to float because the matrix only accepts float is in float32
    if type == 'x': #if type is x, then the rotation matrix will move from left to right
        rotation_matrix = tf.stack([[1, 0, 0],
                                    [0, tf.cos(angle), tf.sin(angle)],
                                    [0, -tf.sin(angle), tf.cos(angle)]
                                    ])
    elif type == 'y': #if type is y, then the rotation matrix will move from bottom to top
        rotation_matrix = tf.stack([[tf.cos(angle), 0, -tf.sin(angle)],
                                    [0, 1, 0],
                                    [tf.sin(angle), 0, tf.cos(angle)]
                                    ])
    elif type == 'z': #if type is z, then the rotation matrix will move from front to back
        rotation_matrix = tf.stack([[1, 0, 0],
                                    [0, tf.cos(angle), tf.sin(angle)],
                                    [0, -tf.sin(angle), tf.cos(angle)]
                                    ])

    return tf.matmul(tf.cast(points, tf.float32), tf.cast(rotation_matrix, tf.float32)) 

def translate_shape(points, amount, translate_type): #shifts the object's position based on what is added by the slider

    if translate_type == 'x':
        translate_matrix = tf.stack([[1, 0, 0],
                                    [0, 1, 0],
                                    [amount, 0, 1]
                                    ])
    elif translate_type == 'y':
        translate_matrix = tf.stack([[1, 0, 0],
                                    [0, 1, amount],
                                    [0, 0, 1]
                                    ])
    elif translate_type == 'z':
        translate_matrix = tf.stack([[1, 0, amount],
                                    [0, 1, 0],
                                    [0, 0, 1]
                                    ])
    
    return tf.matmul(tf.cast(points, tf.float32), tf.cast(translate_matrix, tf.float32))

def scale_obj (points, amount):
##Update the values here to move the cube around x,y,z axis
    scale_matrix = tf.stack([[-amount, 0, 0],
                            [0, amount, 0],
                            [0, 0, -amount]
                            ])
    return tf.matmul(tf.cast(points, tf.float32), tf.cast(scale_matrix, tf.float32))

def shear_obj(points, yold, ynew, zold, znew, xold, xnew, type_shear):

    sh_y = tf.multiply(yold, ynew)
    sh_z = tf.multiply(zold, znew)

    if type_shear == 'x':
      shear_points = tf.stack([
                            [sh_y, 0, 0],
                            [sh_z, 1, 0],
                            [0, 0, 1]
                             ])
    elif type_shear == 'y':
        shear_points = tf.stack([
                            [1, 0, 0],
                            [sh_y, sh_z, 0],
                            [0, 0, 1]
                             ])
    elif type_shear == 'z':
        shear_points = tf.stack([
                            [1, 0, 0],
                            [0, 1, 0],
                            [sh_y, sh_z, 1]
                             ])
      
    shear_object = tf.matmul(tf.cast(points, tf.float32), tf.cast(shear_points, tf.float32))

    return shear_object

##Shear2

def main():

    choices = ['Cube', 'Pyramid', 'Diamond', 'Prism']
    choice = st.sidebar.selectbox('Select a shape', choices, key="act4.main.selectbox")
    if choice == 'Cube':
        init_shape_ = _cube_(side_length=3)
    elif choice == 'Pyramid':
        init_shape_ = triangle(side_length=3, negative=-3)
    elif choice == 'Diamond':
        init_shape_ = diamond(side_length_top=5, negative_top=-5, side_length=3, negative=-3)
    elif choice == 'Prism':
        init_shape_ = prism(side_length=3, negative=-3)
    else:
        print("Invalid choice, exiting the program")
        exit(1)
    
    with st.sidebar:
        st.title("Functions: ")
        function= st.selectbox('Select a function', ['Translate', 'Rotate', 'Scale', 'Shear'], key="act4.function.selectbox")
        # translate = st.checkbox('Translate', key="act4.function.checkbox1")
        # rotate = st.checkbox('Rotate', key="act4.function.checkbox2")

    if function == 'Translate': #shifts the object's location
        with st.sidebar:
            trans_type = st.selectbox('Select a translation axis', ['x', 'y', 'z'], key="act4.translate.selectbox")
            amount = st.slider("Movement Amount: ", -5, 5, 1, key="act4.translate.slider")
        with tf.compat.v1.Session() as session:
            translated_object = session.run(translate_shape(init_shape_, amount, trans_type))
        plt_basic_object_(translated_object)
    elif function == 'Rotate': #rotates the x, y and z axes
        with st.sidebar:
            type = st.selectbox('Select a rotation axis', ['x', 'y', 'z'], key="act4.rotate.selectbox")
            angle = st.slider("Rotation Angle: ", 1, 100, 1, key="act4.rotate.slider")
        with tf.compat.v1.Session() as session:
            rotated_object = session.run(rotate_shape(init_shape_, angle, type))
        plt_basic_object_(rotated_object)
    elif function == 'Scale': #scales the object
        amount = st.sidebar.slider("Scale Amount: ", -10, 10, 1, key="act4.scale.slider")
        with tf.compat.v1.Session() as session:
            scaled_object = session.run(scale_obj(init_shape_, amount))
        plt_basic_object_(scaled_object)
    elif function == 'Shear': #shears the object
        with st.sidebar:
            type_shear = st.selectbox('Select a shear axis', ['x', 'y', 'z'], key="act4.shear.selectbox")
            st.write("Old Values:")
            xold = st.slider("Xold: ", -10, 10, 1, key="act4.shear.slider1")
            yold = st.slider("Yold: ", -10, 10, 1, key="act4.shear.slider2")
            zold = st.slider("Zold: ", -10, 10, 1, key="act4.shear.slider3")
            st.write("New Values:")
            xnew = st.slider("Xnew: ", -10, 10, 1, key="act4.shear.slider4")
            ynew = st.slider("Ynew: ", -10, 10, 1, key="act4.shear.slider5")
            znew = st.slider("Znew: ", -10, 10, 1, key="act4.shear.slider6")
        with tf.compat.v1.Session() as session:
            sheared_object = session.run(shear_obj(init_shape_, yold, ynew, zold, znew, xold, xnew, type_shear))
        plt_basic_object_(sheared_object)

if __name__ == '__main__':
    main()