import streamlit as st
import numpy as np
import pandas as pd
from streamlit_autorefresh import st_autorefresh

st.set_page_config(
     page_title="Ex-stream-ly Cool App",
     page_icon=":shark:",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
 )

from PIL import Image
image = Image.open('BeeIN Logo v11.png')

st.image(image, width=300)

# Run the autorefresh about every 2000 milliseconds (2 seconds) and stop
# after it's been refreshed 100 times.
count = st_autorefresh(interval=30000, limit=100, key="fizzbuzzcounter")

def refresh():
    #st.write('Hello, *World!* :sunglasses:')
    pass

df = pd.read_csv("out.csv")








with st.sidebar:
    global visualization
    visualization = st.radio(
        "Choose a visualization",
        ("Table", "Graph")
    )

    b =  st.button('Refresh', on_click=refresh)


if visualization=="Table":
    st.dataframe(df.style.highlight_max(axis=0),400,800)
else:
    df = df.set_index('Timestamp')
    st.line_chart(df)


forelast = int(df.tail(2).iloc[0][0])
mylast  = int(df.tail(2).iloc[1][0]) 
diff  =  mylast - forelast
bat_string = str(mylast) + "%"
diff_string = str(diff) + "%"

col1, col2, col3 = st.columns(3)
col1.metric("Temperature (Dummy)", "24 °C", "1 °F")
col2.metric("Wind (Dummy)", "9 kmh", "-8%")
col3.metric("Battery Level", bat_string, diff_string)
