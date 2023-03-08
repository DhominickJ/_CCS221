
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pages.Activity1 as act1
import pages.Activity2 as act2
import pages.Activity3 as act3
# import pages.Activity4 as act4

def main():
    st.title("Midterm Exam in CCS221")
    func = st.selectbox("Function Choices",options=['DDALine' , 'Flood Fill', 'Boundary Fill', 'Open CV', '3D Shapes'])
    if (func == 'DDALine'):
        while(True):
            st.header("Task 1")
            st.subheader("DDA Line Algorithm")
            x1 = st.slider("Enter X1: ", 1, 100, 1) #slider for the x1 coordinate
            y1 = st.slider("Enter Y1: ", 1, 100, 1) #slider for the y1 coordinate
            x2 = st.slider("Enter X2: ", 1, 100, 1) #slider for the x2 coordinate
            y2 = st.slider("Enter Y2: ", 1, 100, 1) #slider for the y2 coordinate
            color = "r." #red color for the plotted line
            color_midpoint = "b." #the color of the midpoint will be blue
            choice = st.selectbox("Function", options = ["DDALine", "Brensenham"])
            act1.DDALine (x1, y1, x2, y2, color, color_midpoint)
    elif (func == 'Flood Fill'):
        st.write("To be Fixed")
    elif (func == 'Boundary Fill'):
        st.write("To be Fixed")
    elif (func == 'Open CV'):   
        st.write("To be Fixed")
    elif (func == '3D Shapes'):
        st.write("To be Fixed")




if  __name__ == "__main__":
    main()

