import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Size of the Array
M = 8
N = 8
 
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
 
def floodFill(two_d_array, x, y, newColor):
    oldColor = two_d_array[x][y]
    if(oldColor==newColor):
      return
    fillChecker(two_d_array, x, y, oldColor, newColor)

    plt.imshow(two_d_array, interpolation = 'none', cmap = 'gray_r')
    st.pyplot()

def boundaryFill(two_d_array, x, y, newColor):
    oldColor = two_d_array[x][y]
    if(oldColor==newColor):
      return
    fillChecker(two_d_array, x, y, oldColor, newColor)

    plt.imshow(two_d_array, interpolation = 'none', cmap = 'gray_r')
    st.pyplot()


def main():
    st.title("Flood Fill Algorithm")
    st.subheader("Fill Status: ")

    while True:
        x = int(M / 2)# Since it's starting from the center of the grid
        y = int(N / 2) # Since it's starting from the center of the grid
        function = st.selectbox("Function Choices",options=['Flood Fill', 'Boundary Fill'])
        fill = st.checkbox("Fill Status: ", value=True, key=None, help=None)
        if fill == False and function == 'Flood Fill':
            plt.imshow(original_array, interpolation = 'none', cmap = 'gray_r')
            st.pyplot()
        elif fill == False and function == 'Boundary Fill':
            plt.imshow(two_d_array, interpolation = 'none', cmap = 'gray_r')
            st.pyplot()
        elif function == 'Flood Fill':
            newColor = 1
            floodFill(two_d_array, x, y, 1)
        elif function == 'Boundary Fill':
            newColor = 1
            boundaryFill(two_d_array, x, y, newColor)

if __name__ == '__main__':
    main()
 