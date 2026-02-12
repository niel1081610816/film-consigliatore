import streamlit as st
from openai import OpenAI

client = OpenAI(
    api_key="sk-or-v1-37c...9a8",
    base_url="https://openrouter.ai/api/v1")

st.title("Consigliatore Film/Serie 🎬")

film = st.text_input("Scrivi un film o serie che ti è piaciuto:")

if st.button("Trova qualcosa con lo stesso mood"):
    if film:
        risposta = client.responses.create(
            model="gpt-4o-mini",
            input=f"consigliaun film o serie con lo stesso mood di: {film}")

        st.write(risposta.output_text)

    else:
        st.warning("Scrivi prima un film o serie.")




