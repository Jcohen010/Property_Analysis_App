import streamlit as st


@st.cache_data()
def get_property(mls_id):
    
    import requests

    url = "https://us-real-estate.p.rapidapi.com/property-by-mls-id"

    querystring = {"mls_id": mls_id}

    headers = {
        "X-RapidAPI-Key": "fe7ae48289msh7c3517a0cacdcbbp143430jsnd4c11f1d33e7",
        "X-RapidAPI-Host": "us-real-estate.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    results = response.json()

    return results