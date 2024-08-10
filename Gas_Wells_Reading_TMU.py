
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
Date=datetime.date.today()
Date=Date.strftime('%d-%m-%Y')
#st.write(Date)

st.markdown(" <center>  <h1> Well Production Parameters </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)

CK = st.slider("C.K %", 0.00,100.00)

WHP = st.slider("WHP Psi", 300.0,5000.0)
SEP_Pressure= st.slider("Separator Pressure Psi", 0.00,2000.00)
SEP_Temperature= st.slider("Separator Temp. F", 0.00,200.00)

FLP= st.slider("FLP Psi", 0.00,1400.00)
FLT = st.slider("FLT F", 0.00,200.00)


Gas_Rate = st.text_input("Gas Rate (MMSCF/Day)")
Condensate = st.text_input("Condensate (BPD)")
Water = st.text_input("Water (BPD)")
GOR = st.text_input("Gas Oil Ratio")

API = st.slider("API Degree", 0.00,60.00)
BSW = st.slider("BS & W %", 0.00,100.00)


st.markdown(" <center>  <h1> Well Impurities Parameters </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)

CO2 = st.slider("CO2 %", 0.00,100.00)
H2S = st.slider("H2S PPM", 0.00,50.00)
Salinity = st.slider("Salinity KPPM", 0.00,300.00)


if st.button('Save'):
 with open("games.txt", "a") as text_file



