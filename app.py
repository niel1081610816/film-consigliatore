import streamlit as st
from openai import OpenAI

client = OpenAI(
    api_key="sk-or-v1-37c...9a8",
    base_url="https://openrouter.ai/api/v1")

st.title("Consigliatore Film/Serie 🎬")

film = st.text_input("Scrivi un film o serie che ti è piaciuto:")

if st.button("Trova qualcosa con lo stesso mood"):
    if film:
        risposta = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": "Consiglia un film o serie con lo stesso mood."},{"role": "user", "content": film}])

        testo = risposta.choices[0].message["content"]
        st.write(testo)

    else:
        st.warning("Scrivi prima un film o serie.")


