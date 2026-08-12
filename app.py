import streamlit as st
from func import bows
from PIL import Image

st.title("Bows detection")
file = st.file_uploader(
    "Upload an Image",
    type=['jpg','png','jpeg'],
    accept_multiple_files= False
    
)

if file:
    with open("image.png",'wb') as f:
        f.write(file.getbuffer())
        
    result = bows("image.png")
    
    print(result)