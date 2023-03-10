import streamlit as st
import pandas as pd
import numpy_financial as npf
from streamlit_folium import st_folium, folium_static
from functions.get_property_property import get_property
from functions.generate_raw_coordinates_dict import generate_raw_coordinates_dict
from functions.get_driving_distance import get_driving_distance
from functions.generate_folium_map import generate_folium_map


### VARIABLES ###
dollarsformat = "${:,.2f}"

income_dict = {
    "Justin" : 5400,
    "Syd" : 4800
}

expenses_dict = {
    "Justin" : 2394,
    "Syd" : 1775
}

if 'coordinates_dict' in st.session_state:
    coordinates_dict = st.session_state.coordinates_dict

# coordinates_dict = {
#         'coordinates' : {
#             'home' : [
#             {'Justin' : {
#                 'lat' : 41.33115142971489,
#                 'lon' : -73.18608590196374
#                         }},
#             {'Syd' : {
#                 'lat' : 41.331497982773655,
#                 'lon' : -73.44446180227342
#             }}],
#             'work' : [
#             {'Curtis Packaging' : {
#                 'lat' : 41.4076328155581, 
#                 'lon' : -73.26196805970572
#             }},
#             {'Danbury Ice' : {
#                 'lat' : 41.395522684003225, 
#                 'lon' : -73.45088991552578
#             }},
#             {'Brewster Ice' : {
#                 'lat' : 41.36578270632403,
#                 'lon' : -73.61497920268121
#             }}
#     ]}
# }
st.title("Property Analysis App")

mls_id = st.text_input('Type the MLS Number of the property.')

if mls_id:
    ### LOAD PROPERTY ###
    results = get_property(mls_id=mls_id)

    ### COORDINATES ###
    # Structure coordinate data
    property_coordinates = results['data']['results'][0]['location']['address']['coordinate']

    property_coordinates_dict = [{
    'property' : property_coordinates
    }]

    # Add property coordinates to existing dict
    coordinates_dict['coordinates']['property'] = property_coordinates_dict
    map_container = generate_raw_coordinates_dict(coordinates_dict)
    coordinates_df = pd.DataFrame(map_container)
    distance_list = get_driving_distance(coordinates_dict)

    
    map = generate_folium_map(coordinates_df=coordinates_df, coordinates_dict=coordinates_dict)

    st_folium(map, width=700, height=800)
    
    col1, col2, col3 = st.columns([2,2,2])

    with col1:
        price = results['data']['results'][0]['list_price']

        st.header("Financials")
        Price = st.text_input(label="Price", value=dollarsformat.format(price), help="This field may be changed; all other 'Financials' fields will update to reflect the change in purchase price.")
        price_input = float(Price.replace("$","").replace(",","").replace(".",""))/100
        PercentDown = st.slider("Percentage Down Payment (%)", min_value=0, max_value=100, value=20)
        DownPayment = st.text_input(label="Downpayment", value=dollarsformat.format(price_input*(PercentDown/100)))
        st.markdown("#")
        st.markdown("#### Mortgage Info")
        loanamount = price_input*(1-(PercentDown/100))
        LoanAmount = st.text_input(label="Loan Amount", value=dollarsformat.format(price_input*(1-(PercentDown/100))))
        LoanTerm = st.slider("Loan Term (Years)", min_value=5, max_value=30, value=30, step=5)
        InterestRate = st.slider("Interest Rate (%)", min_value=float(0.000), max_value=float(10), value=6.0, step=float(.1))
        monthlypayment = -1*npf.pmt(float(InterestRate/100)/12, LoanTerm*12, loanamount)
        st.markdown("###### Monthly Payment")
        MonthlyPayment = st.code(dollarsformat.format(monthlypayment), language="html")
        st.markdown("#")
        st.markdown("#### Percentage of Income")
        for person, income in income_dict.items():
            percentage_of_income = 100*(monthlypayment / income)
            st.code(f"{int(percentage_of_income)}% of {person}'s Income" )



    with col2:
        photo = results['data']['results'][0]['primary_photo']['href']

        st.header(f"Information")
        st.image(photo)
        
        for label, info in sorted(results['data']['results'][0]['description'].items()):
            if info != None:
                st.code(f"{label} : {info}")
        
    with col3:
        st.header(f"Distance")
        for item in distance_list:
            st.code(item)
    

else:
    st.warning("Please enter an MLS ID")



