import streamlit as st



st.title("Configuration")

st.header("Places")

st.markdown("###### Record your relevent locations. This will allow the app to tell you how far the property is from your important locations.")

col1,col2,col3 = st.columns(3)
with col1:
    number_of_places = st.number_input("Number of Places", step=1, value=0)
Places = {}

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
    
    Places[i] = {
                            "place_name" : Place_Name,
                            "place_catergory" : Place_Category,
                            "Place_Address" : Place_Address
                        }
    

st.write(st.session_state)