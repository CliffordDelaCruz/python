import streamlit as st

def convert_km_to_miles(km):
    # Convert kilometers to miles
    return km * 0.621371

def convert_miles_to_km(miles):
    # Convert miles to kilometers
    return miles / 0.621371

# Streamlit app layout
st.title('Kilometers ⇄ Miles Converter')

# User selection for conversion direction
conversion_direction = st.radio("Choose the conversion direction:", ("Kilometers to Miles", "Miles to Kilometers"))

# User input for the value to convert
if conversion_direction == "Kilometers to Miles":
    km = st.number_input("Enter the distance in kilometers:", min_value=0.0, format="%.2f")
    if st.button('Convert'):
        miles = convert_km_to_miles(km)
        st.success(f"{km} kilometers is equal to {miles:.2f} miles.")
else:
    miles = st.number_input("Enter the distance in miles:", min_value=0.0, format="%.2f")
    if st.button('Convert'):
        km = convert_miles_to_km(miles)
        st.success(f"{miles} miles is equal to {km:.2f} kilometers.")