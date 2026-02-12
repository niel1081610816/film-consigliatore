import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="sk-or-v1-37c...9a8", base_url="httpsw://openrouter.ai/api/v1")

st.title("Consigliatore Film/Serie")

titolo = st.text_input("Scrivi un film o una serie che ti è piaciuto")

if st.button("Trova qualcosa di simile"):
    if titolo:
        risposta = client.chat.completions.create(model="opena/gpt-4o-mini",messages=[{"role": "system", "content": "sei un assistente che consiglia film o seriesimili a quello indicato, basandotisullo stesso mood e genere."},
                                                                                      {"role": "user", "content": titolo}])
testo = risposta.choices[0].message["content"]
st.write(testo)



