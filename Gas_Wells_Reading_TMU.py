
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

st.markdown(" <right>  <h1> Well Production Parameters </h1> </font> </right> </h1> ",
            unsafe_allow_html=True)

CK = st.slider("C.K %", 0.00,100.00,value=30.00,key="CK")

WHP = st.slider("WHP Psi", 300.0,5000.0,value=700.00,key="WHP")
SEP_Pressure= st.slider("Separator Pressure Psi", 0.00,2000.00,value=400.00,key="SEP_Pressure")
SEP_Temperature= st.slider("Separator Temp. F", 0.00,250.00,value=100.00,key="SEP_Temp")

FLP= st.slider("FLP Psi", 0.00,1400.00,value=400.00,key="FLP")
FLT = st.slider("FLT F", 0.00,250.00,value=100.00,key="FLT")


Gas_Rate = st.text_input("Gas Rate (MMSCF/Day)",key="Gas_Rate")
Condensate = st.text_input("Condensate (BPD)",key="Condensate")
Water = st.text_input("Water (BPD)",key="Water")
GOR = st.text_input("Gas Oil Ratio",key="GOR")


API = st.slider("API Degree", 0.00,60.00,value=32.00,key="API")
BSW = st.slider("BS & W %", 0.00,100.00,value=20.00,key="BSW")


st.markdown(" <center>  <h1> Well Impurities Parameters </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)

CO2 = st.slider("CO2 %", 0.00,100.00,value=12.00,key="CO2")
H2S = st.slider("H2S PPM", 0.00,50.00,value=8.00,key="H2S")
Sal = st.slider("Salinity KPPM", 0.00,300.00,value=281.00,key="Sal")




Data = {'Well_Name': Well_Name,'Date':Date,'C.K%': CK,'WHP': WHP,'SEP_Pressure': SEP_Pressure,'SEP_Temperature': SEP_Temperature,'FLP': FLP,'FLT': FLT,'Gas_Rate': Gas_Rate,'Condensate': Condensate,'Water': Water,'GOR': GOR,'API': API,'BSW': BSW}
df=pd.DataFrame([Data])

df["Date"]=pd.to_datetime(df["Date"])
df["C.K %"]=df["C.K %"].astype("str")+ "%"







































st.dataframe(df)
st.write("CO2 %  = ",CO2)
st.write("H2S PPM  = ",H2S)
st.write("SAL KPPM  = ",Sal)



st.button('Save')
















