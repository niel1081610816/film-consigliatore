
import streamlit as st
from supabase import create_client
url = "https://kjqncgasirjzilovibat.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtqcW5jZ2FzaXJqemlsb3ZpYmF0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzI0NjkyNTgsImV4cCI6MjA4ODA0NTI1OH0.qDVawy4rq8QCO9fP5tJsTSVN8PrgZW5BKwFOWxX2ECI"
supabase = create_client(url,key)
if st.button("Salva il profilo"):
    supabase.table("utenti").insert({
        "nome": nome,
        "genere": genere,
        "ruolo": ruolo
    })

    st.success("Profilo salvato!")


response = supabase.table("utenti").select("*")
data = response.data

if data and len(data) > 1:
    current_user = data[-1]

    risultati = match(current_user, data)

    st.subheader("Collaboratori suggeriti")

    for u, score in risultati:
        if u["nome"] != current_user["nome"]:
            st.write(f"{u['nome']} → compatibilità: {score}%")









