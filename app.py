
# SALVA
if st.button("Salva il profilo"):
    supabase.table("utenti").insert({
        "nome": nome,
        "genere": genere,
        "ruolo": ruolo
    })

    st.success("Profilo salvato!")

# LEGGI
response = supabase.table("utenti").select("*")
data = response.data

if data and len(data) > 1:
    current_user = data[-1]

    risultati = match(current_user, data)

    st.subheader("Collaboratori suggeriti")

    for u, score in risultati:
        if u["nome"] != current_user["nome"]:
            st.write(f"{u['nome']} → compatibilità: {score}%")




