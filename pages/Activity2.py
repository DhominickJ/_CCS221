import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
"""
Members: Billena, Dhominick John
         Torre, Jephone Israel Jireh
         Artacho, Cristopher Ian
         Constantino, Els Dave 
"""
# Size of the Array
M = 8
N = 8
 #number of dimensions in the rank of the array (grid of values)
original_array = np.array([[0,0,0,0,0,0,0],
                        [0,1,1,1,1,1,0],
                        [0,1,0,0,0,1,0],
                        [0,1,0,0,0,1,0],
                        [0,1,0,0,0,1,0],
                        [0,1,1,1,1,1,0],
                        [0,0,0,0,0,0,0]]) #7x7 grid

two_d_array = np.array([[0,0,0,0,0,0,0],
                        [0,1,1,1,1,1,0],
                        [0,1,0,0,0,1,0],
                        [0,1,0,0,0,1,0],
                        [0,1,0,0,0,1,0],
                        [0,1,1,1,1,1,0],
                        [0,0,0,0,0,0,0]]) #7x7 grid

#checks if the file(array) exists
def fillChecker(two_d_array, x, y, oldColor, newColor):
     
    # Base cases
    if (x < 0 or x >= M or y < 0 or
        y >= N or two_d_array[x][y] != oldColor or
        two_d_array[x][y] == newColor):
        return
 
    # Replace the color at (x, y)
    two_d_array[x][y] = newColor
 
    # Recur for north, east, south and west
    fillChecker(two_d_array, x + 1, y, oldColor, newColor)
    fillChecker(two_d_array, x - 1, y, oldColor, newColor)
    fillChecker(two_d_array, x, y + 1, oldColor, newColor)
    fillChecker(two_d_array, x, y - 1, oldColor, newColor)
 
 #to replace values within a given boundary
def floodFill(two_d_array, x, y, newColor):
    oldColor = two_d_array[x][y]
    if(oldColor==newColor):
      return
    fillChecker(two_d_array, x, y, oldColor, newColor)
#creates an image from a 2-dimensional numpy array
    plt.imshow(two_d_array, interpolation = 'none', cmap = 'gray_r')

    #displays a matplotlib.pyplot figure
    st.pyplot(plt.gcf())

#fill the new color inside the old color
def boundaryFill(two_d_array, x, y, newColor):
    oldColor = two_d_array[x][y]
    if(oldColor==newColor):
      return
    fillChecker(two_d_array, x, y, oldColor, newColor)

    plt.imshow(two_d_array, interpolation = 'none', cmap = 'gray_r')
    st.pyplot(plt.gcf())


def main():
    
    x = int(M / 2)# Since it's starting from the center of the grid
    y = int(N / 2) # Since it's starting from the center of the grid
    options=['Flood Fill', 'Boundary Fill']
    function = st.selectbox("Function Choices", options, key="act2.function.selectbox", help='Select a function to be executed')
    fill = st.checkbox("Fill Status: ", value=True, key="act2.fillchecker", help='Check to fill the function')
    if fill == False:
        plt.imshow(original_array, interpolation = 'none', cmap = 'gray_r')
        st.pyplot(plt.gcf())
    elif function == 'Flood Fill':
        newColor = 1
        floodFill(two_d_array, x, y, 1)
    elif function == 'Boundary Fill':
        newColor = 1
        boundaryFill(two_d_array, x, y, newColor)

if __name__ == '__main__':
    while True:
        main()
 