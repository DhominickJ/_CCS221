
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import Tasks.Activity1 as act1
import Tasks.Activity2 as act2
import Tasks.Activity3 as act3
import Tasks.Activity4 as act4
import Tasks.Quiz1 as quiz1


def main():
    with st.sidebar:
        st.title("Midterm Exam in CCS221")
        func = st.selectbox("Function Choices",options=['DDALine and Brensenham' , 'Flood Fill and Boundary Fill', 'Open CV', '3D Shapes', 'Quiz'], key = "main1")
    if (func == 'DDALine and Brensenham'):
        st.subheader("DDA Line Algorithm and Brensenham")
        act1.main()
    elif (func == 'Flood Fill and Boundary Fill'):
        st.subheader("Flood Fill Algorithm and Boundary Fill")
        act2.main()
    elif (func == 'Open CV'):
        st.subheader("Open CV")
        act3.main()
    elif (func == '3D Shapes'):
        st.subheader("Open CV")
        act4.main()
    elif (func == 'Quiz'):
        st.subheader("Quiz")
        quiz1.main()

if  __name__ == "__main__":
    main()

