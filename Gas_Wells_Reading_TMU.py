
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


