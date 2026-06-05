import streamlit as st

st.title("Empans")
st.write("Lire chaque suite de chiffre au rythme de un par seconde.")

tab1, tab2, tab3, tab4= st.tabs(["➡️ Empan endroit", "⬅️ Empan inverse", "📊 Scores", "📄 Rapport"])

with tab1:
    st.write("Empan de chiffres endroit")

    resultat = st.segmented_control("*9 - 7*", ["Vrai", "Faux"])

with tab2:
    st.write("Empan de chiffres inverse")

with tab3:
    st.write("📊 Scores")

with tab4:
    st.write("📄 Rapport")
