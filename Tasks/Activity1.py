import matplotlib.pyplot as plt
import streamlit as st

# """
# Members: Artacho, Cristopher Ian
#          Billena, Dhominick John
#          Torre, Jephone Issiah Jireh
#          Constantino, Els Dave
# """

# """
# Formula for the Brensenham's Line Algorithm: Source: Wolfram Alpha
#     m = dx / dy
#     c = 1
#     x = x            # The value of x increments and affects the value of y
#     y = mx + c       # The value of y is affected by the slope of m * x the c is the value which influences the increment of the value

# Formula for the DDA Line's Algorithm Midpoint
#     midpoint = x = (x1 + x2) / 2 #Finding the locaition of the middle point of the xlines
#                y = (y1 + y2) / 2 #Finding the location of the middle for the ylines
# """


st.title("Mid Point Line Assignment") #title for the plot/graph
plt.xlabel("Horizontal Axis") #name for the x coordinate
plt.ylabel("Vertical Axis") #name for the y coordinate

def DDALine(x1, y1, x2, y2, color, color_midpoint): #function
    fig = plt.figure()
    dx = x2 - x1 
    dy = y2 - y1
    x3 = (x1 + x2) /2 #coordinates for the midpoint on the horizontal axis
    y3 = (y1 + y2) /2 #coordinates for the midpoint on the vertical axis
    
    #calculate steps required for generating pixels 

    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy) #will take the value of dx if ds is more than dy. Otherwise, will take the value of dy

    #calculate increment in x and y for each steps

    Xinc = float(dx / steps)
    Yinc = float(dy / steps)

    for i in range(0, int(steps + 1)):
        #draw pixels 
        plt.plot (int(x1), int(y1), color) #plots first the looped coordinates of x and y
        plt.plot (x3, y3, color_midpoint) #plot for the midpoint's location
        x1 += Xinc
        y1 +=Yinc 

    return fig

def Brensenham(x1, y1, x2, y2, color, color_midpoint):
    fig = plt.figure()
    x3 = float(x1 + x2) /2 #coordinates for the midpoint on the horizontal axis
    y3 = float(y1 + y2) /2 #coordinates for the midpoint on the vertical axis
    m = (y2 - y1) / (x2 - x1)
    c = 1 * (y2 - y1) - (x2 - x1)

    for x in range(x1, x2 + 1): #Increase the value of the second because it is rounded?
        y = round(m*x + c) 
        plt.plot(int(x), int(y), color)
        plt.plot(int(x3), int(y3), color_midpoint) #plot for the midpoint's location
    
    return fig

def main():
    with st.sidebar:
        st.title("DDA Line and Brensenham Algorithm")
        choice = st.selectbox("Function", options = ["DDALine", "Brensenham"], key="act1.selectbox") #selectbox for the function to be used
        x1 = st.slider("Enter X1: ", 1, 100, 1, key = "x1.slider.1") #slider for the x1 coordinate
        y1 = st.slider("Enter Y1: ", 1, 100, 1, key="2") #slider for the y1 coordinate
        x2 = st.slider("Enter X2: ", 10, 100, 10, key="3") #slider for the x2 coordinate
        y2 = st.slider("Enter Y2: ", 10, 100, 10, key="4") #slider for the y2 coordinate
    color = "r." #red color for the plotted line
    color_midpoint = "b." #the color of the midpoint will be blue
    if choice == "DDALine":
        st.pyplot(DDALine (x1, y1, x2, y2, color, color_midpoint))
    else:
        st.pyplot(Brensenham(x1, y1, x2, y2, color, color_midpoint))

if __name__ == '__main__':
    while True:
        main()


