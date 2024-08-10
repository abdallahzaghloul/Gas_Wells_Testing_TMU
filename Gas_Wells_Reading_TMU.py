
from PIL import Image
import streamlit as st
import numpy as np #1
import pandas as pd #2
import datetime
#File="Client_EPIS_Daily_Progress.xlsx"
im = Image.open("KPC.jpg")
image = np.array(im)
st.image('image')
