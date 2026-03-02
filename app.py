import streamlit as st
from supabase import create_client
url = "https://jnaujwpfuhynogktbfua.supabase.co"
key= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpuYXVqd3BmdWh5bm9na3RiZnVhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzI0NjkyOTksImV4cCI6MjA4ODA0NTI5OX0.X_PFJHONaGMYqAJG-5Br7iE4_xsv-umiFcLyl-JiMuw"
supabase = create_client(url, key)
st.title("Titolo del sito")
nome = st.text_input("Nome")
ruolo = st.selectbox("Chi sei?", ["produttore", "cantante", "entrambi"])
genere = st.selectbox("genere", ["uomo", "donna", "nessuno dei due", "preferisco non rispondere"])
if st.button("Salva il profilo"):
    st.success("Profilo salvato")

def match(user, others):
    risultati = []
    for u in others:
        score = 0
        if user["genere"] == u["genere"]:
            score += 50
        if abs(user["bpm"] - u["bpm"]) < 10:
            score += 30
        if user["ruolo"] != u["ruolo"]:
            score += 20
        risultati.append((u, score))
    return sorted(risultati, key=lambda x: x[1], reverse=True)

if data.data:
    current_user = data.data[-1]  # ultimo inserito

    risultati = match(current_user, data.data)

    st.subheader("Collaboratori suggeriti")

    for u, score in risultati:
        if u["nome"] != current_user["nome"]:
            st.write(u["nome"], "-", score)

current_user = data.data[-1]
risultati = match(current_user, data.data)

st.subheader("Collaboratori suggeriti")
for u, score in risultati:
    if u["nome"] != current_user["nome"]:st.write(f"{u['nome']} ➝‬ compatibilità: {score}%")
