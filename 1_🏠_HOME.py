import streamlit as st
import base64
import pandas as pd
from PIL import Image
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="CRYPTO WEB-APP",page_icon="🪙")

def load_animation(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


#Useing local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# loading img form pc
main_p= Image.open("images/m.png")

animation_logo=load_animation("https://assets8.lottiefiles.com/packages/lf20_pxiupds9.json")

# logo display
st.write("---")
with st.container():
    left_column, right_column = st.columns((2,10))
    with left_column:
        st_lottie(animation_logo, height=100, key="coding")
          
    with right_column:
        st.markdown('<b class="big-font">CRYPTO PREDICTION</b>', unsafe_allow_html=True)
        
st.write("---")


with st.container():
    text_column, image_column = st.columns((3, 3))
    with text_column:
        st.markdown("LOOK")
        st.markdown("LEARN")
        st.markdown("PREDICT")
    with image_column:
        st.image(main_p)
    
#bg img func
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('images/hetgabdu.jpg')   


st.write("---")

st.markdown('''# **TO THE TOP**
*PRICES OF SOME CRYPTO*
''')

st.write("---")


# Binance API yaha se coming
df = pd.read_json('https://api.binance.com/api/v3/ticker/24hr')


# Crypto round value
def round_value(input_value):
    if input_value.empty:
        return None  # Handle missing data
    if input_value.values > 1:
        return float(round(input_value, 2))
    else:
        return float(round(input_value, 8))


col1, col2, col3 = st.columns(3)

# Display horaha
col1_Crypto ='BTCBUSD'
col2_Crypto ='ETHBUSD' 
col3_Crypto ='BNBBUSD' 
col4_Crypto ='XRPBUSD' 
col5_Crypto ='ADABUSD' 
col6_Crypto ='DOGEBUSD'
col7_Crypto ='SHIBBUSD'
col8_Crypto ='DOTBUSD' 
col9_Crypto ='MATICBUSD'


# DataFrame of selected Cryptocurrency
col1_df = df[df.symbol == col1_Crypto]
col2_df = df[df.symbol == col2_Crypto]
col3_df = df[df.symbol == col3_Crypto]
col4_df = df[df.symbol == col4_Crypto]
col5_df = df[df.symbol == col5_Crypto]
col6_df = df[df.symbol == col6_Crypto]
col7_df = df[df.symbol == col7_Crypto]
col8_df = df[df.symbol == col8_Crypto]
col9_df = df[df.symbol == col9_Crypto]

# Apply a custom function to conditionally round values
col1_price = round_value(col1_df.weightedAvgPrice)
col2_price = round_value(col2_df.weightedAvgPrice)
col3_price = round_value(col3_df.weightedAvgPrice)
col4_price = round_value(col4_df.weightedAvgPrice)
col5_price = round_value(col5_df.weightedAvgPrice)
col6_price = round_value(col6_df.weightedAvgPrice)
col7_price = round_value(col7_df.weightedAvgPrice)
col8_price = round_value(col8_df.weightedAvgPrice)
col9_price = round_value(col9_df.weightedAvgPrice)

# Select the priceChangePercent column
col1_percent = f"{col1_df['priceChangePercent'].values[0]}%" if not col1_df.empty else 'N/A'
col2_percent = f"{col2_df['priceChangePercent'].values[0]}%" if not col2_df.empty else 'N/A'
col3_percent = f"{col3_df['priceChangePercent'].values[0]}%" if not col3_df.empty else 'N/A'
col4_percent = f"{col4_df['priceChangePercent'].values[0]}%" if not col4_df.empty else 'N/A'
col5_percent = f"{col5_df['priceChangePercent'].values[0]}%" if not col5_df.empty else 'N/A'
col6_percent = f"{col6_df['priceChangePercent'].values[0]}%" if not col6_df.empty else 'N/A'
col7_percent = f"{col7_df['priceChangePercent'].values[0]}%" if not col7_df.empty else 'N/A'
col8_percent = f"{col8_df['priceChangePercent'].values[0]}%" if not col8_df.empty else 'N/A'
col9_percent = f"{col9_df['priceChangePercent'].values[0]}%" if not col9_df.empty else 'N/A'

# Create a metrics price box
col1.metric(col1_Crypto, col1_price, col1_percent)
col2.metric(col2_Crypto, col2_price, col2_percent)
col3.metric(col3_Crypto, col3_price, col3_percent)
col1.metric(col4_Crypto, col4_price, col4_percent)
col2.metric(col5_Crypto, col5_price, col5_percent)
col3.metric(col6_Crypto, col6_price, col6_percent)
col1.metric(col7_Crypto, col7_price, col7_percent)
col2.metric(col8_Crypto, col8_price, col8_percent)
col3.metric(col9_Crypto, col9_price, col9_percent)