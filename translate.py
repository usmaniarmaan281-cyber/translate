!pip install googletrans
 !pip install streamlit
 import streamlit as st
from googletrans import Translator

st.title("Translator (English ↔ Hindi)")

text = st.text_input("Enter text")
translator = Translator()

if st.button("Translate"):
    translated = translator.translate(text, dest="hi")
    st.success(translated.text)

