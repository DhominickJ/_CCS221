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
M = 7
N = 7
 #number of dimensions in the rank of the array (grid of values)
flood_array = np.array([[1,1,1,1,1,1,1],
                        [1,1,1,1,1,1,1],
                        [1,1,0,0,0,1,1],
                        [1,1,0,0,0,1,1],
                        [1,1,0,0,0,1,1],
                        [1,1,1,1,1,1,1],
                        [1,1,1,1,1,1,1]]) #7x7 grid

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
def floodFill(flood_array, old_value, new_value):

    for row in range(M):
        for column in range(N):
            prev_val = flood_array[row][column]
            if (old_value == prev_val):
                flood_array[row][column] = new_value

    plt.imshow(flood_array, interpolation = 'none', cmap = 'rainbow')
    plt.colorbar()
    st.pyplot(plt.gcf())


#fill the new color inside the old color
def boundaryFill(two_d_array, x, y, newColor):
    oldColor = two_d_array[x][y]
    if(oldColor==newColor):
      return 
    fillChecker(two_d_array, x, y, oldColor, newColor)
    plt.imshow(two_d_array, interpolation = 'none', cmap = 'gray_r')
    plt.colorbar()
    st.pyplot(plt.gcf())

def main():
    
    x = int(M / 2)# Since it's starting from the center of the grid
    y = int(N / 2) # Since it's starting from the center of the grid
    filled = False
    with st.sidebar:
        options=['Flood Fill', 'Boundary Fill']
        function = st.selectbox("Function Choices", options, key="act2.function.selectbox", help='Select a function to be executed')
        fill = st.button("Fill", key="act2.fillchecker", help='Check to fill the function')
        unfill = st.button("Unfill", key="act2.unfillchecker", help='Check to unfill the function')
        old_value = st.slider("Old_Value: ", 1, 3, 1)
        new_value = st.slider("New Value: ", 1, 3, 1)
    if function == 'Boundary Fill' and unfill:
        plt.imshow(original_array, interpolation = 'none', cmap = 'gray_r')
        plt.colorbar()
        st.pyplot(plt.gcf())
        print(original_array)
    elif function == 'Flood Fill' and unfill:
        plt.imshow(flood_array, interpolation = 'none', cmap = 'gray_r')
        plt.colorbar()
        st.pyplot(plt.gcf())
        print(flood_array)
    elif function == 'Flood Fill' and fill == True:
        floodFill(flood_array, old_value, new_value)
        print(flood_array)
    elif function == 'Boundary Fill' and fill == True:
        boundaryFill(two_d_array, x, y, new_value)
        filled = True
        print(two_d_array)
    elif function == 'Boundary Fill' and fill == True and filled == True:
        plt.imshow(two_d_array, interpolation = 'none', cmap = 'gray_r')
        plt.colorbar()
        st.pyplot(plt.gcf())

# if __name__ == '__main__':
#     # main()
#     # floodFill(flood_array, 0, 1)
#     # print(flood_array)
 