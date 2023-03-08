
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.spatial import Delaunay
import tensorflow as tf

#to gett the points and be used on a 3D object function
def plt_basic_object_(points):

    tri = Delaunay(points). convex_hull

    fig = plt.figure(figsize=(8, 8)) #width and size in inches?
    ax = fig.add_subplot(111, projection = '3d') #111 means 1x1 grid and projection '3d' enables the z axis
    S = ax.plot_trisurf(points[:,0], points[:,1], points[:,2], #.plot trisurf means plot a triangulated surface
                        triangles = tri,
                        shade = True, cmap = cm.rainbow, lw=0.5)
    
    
    ax.set_xlim3d (-5, 5) #sets the graph of x from -5 to 5
    ax.set_ylim3d (-5, 5)  #sets the graph of y from -5 to 5
    ax.set_zlim3d (-5, 5)  #sets the graph of z from -5 to 5


    ax.set_xlabel ("X Axis") #label for the x Axis
    ax.set_ylabel ("Y Axis") #label for the Y Axis
    ax.set_zlabel ("Z Axis")  #label for the Z axis

    plt.show()


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

def rotate_shape(points, angle):
    
    angle = float(angle)
    rotation_matrix = tf.stack([[tf.cos(angle), tf.sin(angle), 0],
                                [-tf.sin(angle), tf.cos(angle), 0],
                                [0, 0, 1]
                                ])

    return tf.matmul(tf.cast(points, tf.float32), tf.cast(rotation_matrix, tf.float32)) 

def translate_shape(points, amount):
    return tf.add(points, amount)

def main():
    print ("Available 3D Shapes:")
    print("1. Cube")
    print("2. Pyramid")
    print("3. Diamond")
    print("4. Prism")
    choice = int(input("Enter your choice: "))

    if(choice == 1):
        init_shape_ = _cube_(side_length=3)
    elif(choice == 2):
        init_shape_ = triangle(side_length=3, negative=-3)
    elif(choice == 3):
        init_shape_ = diamond(side_length_top=5, negative_top=-5, side_length=3, negative=-3)
    elif(choice == 4):
        init_shape_ = prism(side_length=3, negative=-3)
    else:
        print("Invalid choice, exiting the program")
        exit(1)
    
    print("Functions: ")
    print("1. Translate")
    print("2. Rotate")
    function = int(input("Function to Apply to Shape:  "))

    if(function == 1): #For Translation
        amount = int(input("Movement Amount: "))
        with tf.compat.v1.Session() as session:
            translated_object = session.run(translate_shape(init_shape_, amount))
        plt_basic_object_(translated_object)
    elif(function == 2): #For Rotation
        angle = int(input("Rotation Angle: "))
        with tf.compat.v1.Session() as session:
            rotated_object = session.run(rotate_shape(init_shape_, angle))
        plt_basic_object_(rotated_object)

if __name__ == '__main__':
    main()