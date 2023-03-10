
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pages.Activity1 as act1
import pages.Activity2 as act2
import pages.Activity3 as act3
import pages.Activity4 as act4

def main():
    st.title("Midterm Exam in CCS221")
    func = st.selectbox("Function Choices",options=['DDALine and Brensenham' , 'Flood Fill and Boundary Fill', 'Open CV', '3D Shapes'])
    if (func == 'DDALine'):
        st.subheader("DDA Line Algorithm")
        act1.main()
    elif (func == 'Flood Fill'):
        st.subheader("Flood Fill Algorithm")
        act2.main()
    elif (func == 'Open CV'):
        st.subheader("Open CV")
        act3.main()
    elif (func == '3D Shapes'):
        st.subheader("Open CV")
        act4.main()

if  __name__ == "__main__":
    main()

