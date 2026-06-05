import streamlit as st

st.title("Empans")
st.write("Lire chaque suite de chiffre au rythme de un par seconde.")

tab1, tab2, tab3 = st.tabs(["🎯 Épreuve", "📊 Scores", "📄 Rapport"])

with tab1:
    st.subheader("🎯 Épreuve")

with tab2:
    st.subheader("📊 Scores")

with tab3:
    st.subheader("📄 Rapport)
