import streamlit as st
import pandas as pd
from functions.get_property_property import get_property
import requests
# zpid = st.text_input('Type the zillow property id of the house')

latitude = get_property(zpid='57804730',property='latitude')
longitude = get_property(zpid='57804730',property='longitude')

# coordinates = {
#     'lat' : [longitude, 41.33115142971489, 41.331497982773655],
#     'lon' : [latitude, -73.18608590196374, -73.44446180227342]
# }

# coordinates_df = pd.DataFrame(coordinates, columns=['lat', 'lon'])

# st.map(coordinates_df)