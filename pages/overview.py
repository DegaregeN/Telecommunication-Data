import os
# from matplotlib.pyplot import plt
import sys

import pandas as pd
import plotly.express as px
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

sys.path.append(os.path.abspath(os.path.join('./scripts')))


def overview_app():
    st.title("Overview")
    st.write(
        "Customer Data's Overview")
    number = st.number_input("Enter the number of rows and press enter: ", min_value=None, max_value=None, value=0,
                             step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)

    df = pd.read_csv('./data/cleaned telecom data.csv', nrows=number)
    st.write(df)

    st.header("Top 5 handsets type manufactured by apple")
    top_5_app = pd.read_csv('./data/app data.csv')
    fig = px.bar(top_5_app, x='Handset', y='count', height=500)
    st.plotly_chart(fig)


    st.header("Duration Distribution")
    image = Image.open('./assets/Durationdist.png')
    st.image(image, caption="Duration Distribution", use_column_width=True)

    st.header("Top data usage per applications")
    image = Image.open('./assets/top_data_usage.png')
    st.image(image, caption="Applications Data usage", use_column_width=True)

    st.header("TCP retransmissions")
    image = Image.open('./assets/tcpretransmission.png')
    st.image(image, caption="Top TCP retransmissions",
             use_column_width=True)

    st.header("Top throughputs")
    image = Image.open('./assets/TopTP.png')
    st.image(image, caption="Top 10 througputs",
             use_column_width=True)

    st.header("Experience Distribution")
    image = Image.open('./assets/ClusterDist.png')
    st.image(image, caption="Experience distribution of user",
             use_column_width=True)