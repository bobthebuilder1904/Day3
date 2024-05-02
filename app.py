import streamlit as st

st.title("Car MPG Calculator")

st.write("Car MPG Calculator is an app that calculates the miles based on the amount of gallons and MPG.")

st.image("https://pictures.dealer.com/c/chevroletofwes26922wesleychapelblvd/1251/461dacf21ca92b5295a1d6ce1a0a5deex.jpg?impolicy=resize&w=1024")

# Create input fields for MPG highway and MPG city
mpg_highway = st.number_input("Enter MPG for highway driving", min_value=1, step=1, value=32)
mpg_city = st.number_input("Enter MPG for city driving", min_value=1, step=1, value=25)

# Create a slider ranging from 1 through 10 for gallons
gallons = st.slider("Select the amount of gallons (1-10)", 1, 10)

# Create a button to perform the calculation for both highway and city driving
if st.button("Calculate Miles left"):
    # Calculate highway MPG
    highway_miles = gallons * mpg_highway
    # Calculate city MPG
    city_miles = gallons * mpg_city
    # Display the results
    st.write("Highway Miles:", highway_miles)
    st.write("City Miles:", city_miles)
