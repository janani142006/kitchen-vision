import streamlit as st
from PIL import Image

st.title("Kitchen Vision")

uploaded_file = st.file_uploader("Upload Pantry Image", type=["jpg","png","jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image")

    if st.button("Analyze Pantry"):
        st.write("Detected Items:")
        st.write(["Rice","Tomato","Egg","Milk"])