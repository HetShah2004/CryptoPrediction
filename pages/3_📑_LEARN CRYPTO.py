
import streamlit as st
from PIL import Image
import base64


st.set_page_config(page_title="CRYPTO WEB-APP",page_icon="🪙")

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
add_bg_from_local('images/dd.jpg') 



# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

#imgs loading form local

img_learn_1 = Image.open("images/what.png")
img_learn_2 = Image.open("images/how.png")
img_learn_3 = Image.open("images/f.png")
img_learn_4 = Image.open("images/n.png")


    
st.header("LEARN WITH US")
st.write("---")

# ---- PROJECTS ----
with st.container():
    
    image_column, text_column = st.columns((1, 2))

    with image_column:
        st.image(img_learn_1)
    with text_column:
        st.subheader("Cryptocurrency In 5 Minutes | What Is Cryptocurrency? | Simplilearn")
        
        st.markdown("[Watch Video...](https://youtu.be/1YyAzVmP9xQ)")

        
st.write("---")
with st.container():

    image_column, text_column = st.columns((1, 2))

    with image_column:
        st.image(img_learn_2)
    with text_column:
        st.subheader("How Cryptocurrency ACTUALLY works.")
        
        st.markdown("[Watch Video...](https://youtu.be/rYQgy8QDEBI)")

st.write("---")

with st.container():

    image_column, text_column = st.columns((1, 2))

    with image_column:
        st.image(img_learn_3)
    with text_column:
        st.subheader("How to invest in Crypto Currency !")
        
        st.markdown("[Watch Video...](https://youtu.be/jV68yMnH01o)")

st.write("---")

with st.container():

    image_column, text_column = st.columns((1, 2))

    with image_column:
        st.image(img_learn_4)
    with text_column:
        st.subheader("How To Invest In Crypto Full Beginners Guide in 2023")
        
        st.markdown("[Watch Video...](https://youtu.be/Yb6825iv0Vk)")

st.write("---")