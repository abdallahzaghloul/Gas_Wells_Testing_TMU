
from PIL import Image
import streamlit as st
import numpy as np #1
import pandas as pd #2
import datetime
im = Image.open("KPC.png")
image= np.array(im)
st.image(image)
st.markdown(" <center>  <h1> Well_Name Testing Follow UP </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)

Well_Name = st.selectbox('The Well Name for current Testing',('BARAKAT-D01X','BARAKAT-D02X','BARAKAT-D06X','FUSTAT-N01X','IO-01X','BAT-10X','NUT-01X','SHAI-01X','ATOUN-N01X','APRIES-E01X','APRIES-E03X','ANTI-01X'))


from datetime import time

Reading_Registeration = st.slider("Reading Registeration:", value=(time(11, 30)))
st.write(datetime.date.today())

from st_radial import st_radial
val = st.slider('Percentage Input',min_value=0, max_value=100)  
st_radial('You selected',val) 




