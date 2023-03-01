import streamlit as st
import pandas as pd
from functions.get_property_property import get_property
from functions.generate_raw_coordinates_dict import generate_raw_coordinates_dict
from functions.get_driving_distance import get_driving_distance


### VARIABLES ###
dollarsformat = "${:,.2f}"
justin_income = 5400
syd_income = 4800

coordinates_dict = {
        'coordinates' : [
            {'Justin' : {
                'lat' : 41.33115142971489,
                'lon' : -73.18608590196374
                        }},
            {'Syd' : {
                'lat' : 41.331497982773655,
                'lon' : -73.44446180227342
            }},
            {'Curtis Packaging' : {
                'lat' : 41.4076328155581, 
                'lon' : -73.26196805970572
            }},
            {'Danbury Ice' : {
                'lat' : 41.395522684003225, 
                'lon' : -73.45088991552578
            }},
            {'Brewster Ice' : {
                'lat' : 41.36578270632403,
                'lon' : -73.61497920268121
            }}

    ]  
}
st.title("Property Analysis App")

mls_id = st.text_input('Type the MLS Number of the property.')

if mls_id:
    ### LOAD PROPERTY ###
    results = get_property(mls_id=mls_id)

    ### COORDINATES ###
    # Structure coordinate data
    property_coordinates = results['data']['results'][0]['location']['address']['coordinate']

    property_coordinates_dict = {
    'property' : property_coordinates
    }

    # Add property coordinates to existing dict
    coordinates_dict['coordinates'].append(property_coordinates_dict)
    map_container = generate_raw_coordinates_dict(coordinates_dict)
    coordinates_df = pd.DataFrame(map_container)
    distance_list = get_driving_distance(coordinates_dict)


    
    col1, col2, col3 = st.columns([2,2,2])

    with col1:
        price = results['data']['results'][0]['list_price']

        st.header("Financials")
        Price = st.text_input(label="Price", value=dollarsformat.format(price))
        Percent_Down = st.slider("Percentage Down Payment (%)", min_value=0, max_value=100, value=20)
        DownPayment = st.text_input(label="Downpayment", value=dollarsformat.format(price*(Percent_Down/100)))
        LoanAmount = st.text_input(label="Loan Amount", value=dollarsformat.format(price*(1-(Percent_Down/100))))

    with col2:
        photo = results['data']['results'][0]['primary_photo']['href']

        st.header(f"Information")
        st.image(photo)
        
        for label, info in results['data']['results'][0]['description'].items():
            st.code(f"{label} : {info}")
        
    with col3:
        st.header(f"Distance")
        for item in distance_list:
            st.code(item)
    
    st.map(coordinates_df)

else:
    st.warning("Please enter an MLS ID")


