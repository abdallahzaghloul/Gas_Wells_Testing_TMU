# -*- coding: utf-8 -*-
"""Gas_Wells_Testing_TMU.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AEkmEYb41fwlGcA6rl1GL3D_UEhPGUEv
"""

from PIL import Image
import streamlit as st
import numpy as np #1
import pandas as pd #2
import datetime
File="Client_EPIS_Daily_Progress.xlsx"
im = Image.open("EPIS.png")
image = np.array(im)