import streamlit as st
import requests

API_URL = "https://v6.exchangerate-api.com/v6/91387a635b191f938a9b557b/latest/USD"

@st.cache_data
def get_rates():
    data = requests.get(API_URL).json()
    st.write("RAW API RESPONSE:", data)

    if data.get("result") != "success":
        raise ValueError(
            f"API error: {data.get('error-type') or data.get('message') or 'Unknown error'}"
        )

    return data["conversion_rates"]


def convert_currency(amount, from_currency, to_currency, rates):
    return amount * (rates[to_currency] / rates[from_currency])

st.title("Currency Converter")

rates = get_rates()
currency_list = sorted(rates.keys())

amount = st.number_input("Amount:", value=1.0)

from_currency = st.selectbox(
    "From currency",
    currency_list,
    index=currency_list.index("NZD") if "NZD" in currency_list else 0
)

to_currency = st.selectbox(
    "To currency",
    currency_list,
    index=currency_list.index("EUR") if "EUR" in currency_list else 0
)

if st.button("Convert"):
    try:
        result = convert_currency(amount, from_currency, to_currency, rates)
        st.success(f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}")
    except Exception as e:
        st.error(f"Error: {e}")
