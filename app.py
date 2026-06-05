import streamlit as st

st.title("Empans")
st.write("Lire chaque suite de chiffre au rythme de un par seconde.")

tab1, tab2, tab3, tab4= st.tabs(["➡️ Empan endroit", "⬅️ Empan inverse", "📊 Scores", "📄 Rapport"])

with tab1:
    st.write("Empan de chiffres endroit")

    for empan in range(2, 10):
        col1, col2, col3 = st.columns([1, 2, 2])  # ← indenté
        with col1:
            st.write(f"**{empan} chiffres**")
        with col2:
            st.segmented_control(".", ["✅", "❌"], key=f"endroit_e1_{empan}", label_visibility="collapsed")
        with col3:
            st.segmented_control(".", ["✅", "❌"], key=f"endroit_e2_{empan}", label_visibility="collapsed")
with tab2:
    st.write("Empan de chiffres inverse")

with tab3:
    st.write("📊 Scores")

with tab4:
    st.write("📄 Rapport")
