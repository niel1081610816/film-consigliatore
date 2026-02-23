import streamlit as st
from openai import OpenAI

client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
)

st.title("Consigliatore Film/Serie")

film = st.text_input("Scrivi un film o serie che ti è piaciuto:")

if st.button("Trova qualcosa con lo stesso mood"):
    if film:
        risposta = client.responses.create(
            model="openchat/openchat-3.5-0106:free",
            input=f"Elenca tre film/serie con lo stesso mood di: {film}")
        st.write(risposta.output_text)
    else:
        st.warning("Scrivi prima un film o una serie.")


