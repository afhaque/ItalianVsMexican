# Dependencies
import numpy as numpy
import pandas as pd 
import matplotlib.pyplot as plt 
import requests 
import time 

# API Keys
gkey = "AIzaSyA_Clyz3478YAUnsESNHE5dyktvvMoa-vw"
ykey = ""

# Data Retrieval 
census_data = pd.read_csv("Census_Data.csv")

# Preview the data
census_pd.head()

# Randomly select 2000 zip code locations with at least 100 residents
selected_zip = census_pd.sample(n=2000)
selected_zip = selected_zip[selected_zip["Population"].astype(int) > 100]

# Visualize
# selected_zips.count()
selected_zips.head()
