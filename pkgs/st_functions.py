import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pkgs.data import clean_data


cleanData = clean_data

def selectbox(title, columName, key):
    feature =st.selectbox(title, cleanData[columName].unique().tolist(), key =key)
    return feature
####
def numericalDataInput(title,min_value, max_value, start_value):
    feature = st.number_input(label =title, min_value = min_value,max_value=max_value, value =start_value,step=0.1,format='%.1f')
    return feature
####
def textMarkdown(msg, font_size, border_color): 
    text = st.markdown(
        f'''
        <div style= "
        border: 2px solid {border_color};
        border-radius:10px;
        padding:15px;
        margin: 20px;         
        margin-top: 10px;
        margin-bottom: 25px;
        text-align:center;
        color: #333;
        background-color: #f9f9f9;
        font-size:{font_size};
        font-weight: bold;
        ">{msg}
        </div>
        ''',
        unsafe_allow_html=True)
    return text

def figure_set(functionName):
    fig, ax = plt.subplots(figsize = (6,5))
    ax =functionName()
    st.pyplot(fig)

print('done')