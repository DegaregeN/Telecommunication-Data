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

    df = pd.read_csv('./data/cleaned_data2.csv', nrows=number)
    st.write(df)

    st.header("Top 10 handsets used by customers")
    top_df = pd.read_csv('./data/top_10_handset.csv')

    fig = px.bar(top_df, x='handset_type', y='count', height=500)
    st.plotly_chart(fig)

    st.header("Top 3 handsets Manufacturers")
    top_3_df = pd.read_csv('./data/top_3_manuf.csv')
    fig = px.bar(top_3_df, x='handset_manufacturer', y='count', height=500)
    st.plotly_chart(fig)

    st.header("Top 5 handsets type manufactured by apple")
    top_5_app = pd.read_csv('./data/top_5_apple.csv')
    fig = px.bar(top_5_app, x='Handset', y='count', height=500)
    st.plotly_chart(fig)

    st.header("User's with most sessions")
    top_5_session = pd.read_csv('./data/top_5_session.csv', nrows=5)

    # print(top_5_session)
    st.write(top_5_session)

    st.header("Duration Distribution")
    image = Image.open('./assets/Durationdist.png')
    st.image(image, caption="Duration Distribution", use_column_width=True)

    st.header("Top data usage per applications")
    image = Image.open('./assets/top_data_usage.png')
    st.image(image, caption="Applications Data usage", use_column_width=True)

    st.header("Application Duration distribution using deciles")
    image = Image.open('./assets/DurationDeciles.png')
    st.image(image, caption="Applications Duration Distribution",
             use_column_width=True)

    st.header("Clustering users based on their Engagement score")
    image = Image.open('./assets/userEngagCluster.png')
    st.image(image, caption="Users clustering into 3 groups based on Engagement score",
             use_column_width=True)

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