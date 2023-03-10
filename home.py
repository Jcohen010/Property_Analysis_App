import streamlit as st
from googlemaps import geocoding
import googlemaps


gmaps = googlemaps.Client("AIzaSyBwyi-9qqOnlnu5VN5wxByzI7svpbNbfkY")


st.title("Configuration")

st.header("Places")

st.caption(" *Record your relevent locations. This will allow the app to tell you how far the property is from your important locations.*")

place_dict = {}
lat = ''
lon = ''

col1,col2,col3 = st.columns(3)
with col1:
    number_of_places = st.number_input("Number of Places", step=1, value=0)
if 'coordinates_dict' not in st.session_state:
    st.session_state.coordinates_dict = {}

python_coordinates_dict = {
            'coordinates' : {
                'home' : [],
                'work' : []}
        }

if 'n_rows' not in st.session_state:
    st.session_state.n_rows = 0

if number_of_places:
    st.session_state.n_rows = number_of_places

for i in range(st.session_state.n_rows):
    #add text inputs here
    col1, col2, col3 = st.columns(3)

    with col1:
        Place_Name = st.text_input(label=f"Name of Location", key=f"place_name{i}", help="Enter the name of the location")
    with col2:
        Place_Category = st.selectbox("Category", key=f"place_category{i}", help="Select a category for the location from the drop down menu.", options=['Home', 'Work'])
    with col3:
        Place_Address = st.text_input(label=f"Address of Location", key=f"place_address{i}", help="Copy and paste the address of the location")
        if Place_Address:
            geo_result = geocoding.geocode(client=gmaps, address=Place_Address)
            lat = geo_result[0]["geometry"]["location"]["lat"]
            lon = geo_result[0]["geometry"]["location"]["lng"]

        place_dict = {
            Place_Name : {
                'lat' : lat,
                'lon' : lon
            }
        }

    if Place_Category == 'Work':
        python_coordinates_dict["coordinates"]['work'].append(place_dict)

    if Place_Category == 'Home':
        python_coordinates_dict["coordinates"]['home'].append(place_dict)
    
    
st.session_state.coordinates_dict = python_coordinates_dict
st.session_state