import streamlit as st
from supabase import create_client
url = "https://kjqncgasirjzilovibat.supabase.co"
key= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtqcW5jZ2FzaXJqemlsb3ZpYmF0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzI0NjkyNTgsImV4cCI6MjA4ODA0NTI1OH0.qDVawy4rq8QCO9fP5tJsTSVN8PrgZW5BKwFOWxX2ECI"
supabase = create_client(url, key)
st.title("Titolo del sito")
nome = st.text_input("Nome")
ruolo = st.selectbox("Chi sei?", ["produttore", "cantante", "entrambi"])
genere = st.selectbox("genere", ["uomo", "donna", "nessuno dei due", "preferisco non rispondere"])
response = supabase.table("utenti").select("*").execute()
if st.button("Salva il profilo"):
    supabase.table("utenti").insert({"nome": nome,"genere": genere,"ruolo": ruolo}).execute()

    st.success("Profilo salvato!")

response = supabase.table("utenti").select("*").execute

if response.data:
    current_user = response.data[-1]

    risultati = match(current_user, response.data)

    st.subheader("Collaboratori suggeriti")

    for u, score in risultati:
        if u["nome"] != current_user["nome"]:
            st.write(u["nome"], "→", score)

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
if response.data:
    current_user = response.data[-1]

    risultati = match(current_user, data.data)

    st.subheader("Collaboratori suggeriti")

    for u, score in risultati:
        if u["nome"] != current_user["nome"]:
            st.write(u["nome"], "-", score)


    if u["nome"] != current_user["nome"]:st.write(f"{u['nome']} compatibilità: {score}%")





















