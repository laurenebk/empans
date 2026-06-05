import streamlit as st

st.title("Empans")
st.write("Lire chaque suite de chiffre au rythme de un par seconde.")

tab1, tab2, tab3, tab4= st.tabs(["➡️ Empan endroit", "⬅️ Empan inverse", "📊 Scores", "📄 Rapport"])

with tab1:

    sequences_endroit = {
        2: ("9 - 7", "6 - 3"),
        3: ("5 - 8 - 2", "6 - 9 - 4"),
        4: ("7 - 2 - 8 - 6","6 - 4 - 3 - 9"),
        5: ("4 - 2 - 7 - 3 - 1","7 - 5 - 8 - 3 - 6"),
        6: ("3 - 9 - 2 - 4 - 8 - 7","6 - 1 - 9 - 4 - 7 - 3"),
        7: ("4 - 1 - 7 - 9 - 3 - 8 - 6","6 - 9 - 1 - 7 - 4 - 2 - 8"),
        8: ("3 - 8 - 2 - 9 - 6 - 1 - 7 - 4","5 - 8 - 1 - 3 - 2 - 6 - 4 - 7"),
        9: ("2 - 7 - 5 - 8 - 6 - 3 - 1 - 9 - 4","7 - 1 - 3 - 9 - 4 - 2 - 5 - 6 - 8")
    }

    for empan, (essai1, essai2) in sequences_endroit.items():
        col1, col2, col3, col4, col5 = st.columns([1, 3, 2, 3, 2])
        with col1:
            st.write(f"**{empan}**")
        with col2:
            st.write(f"{essai1}")
        with col3:
            st.segmented_control(".", ["Vrai", "Faux"], key=f"endroit_e1_{empan}", label_visibility="collapsed")
        with col4:
            st.write(f"{essai2}")
        with col5:
            st.segmented_control(".", ["Vrai", "Faux"], key=f"endroit_e2_{empan}", label_visibility="collapsed")

with tab2:
    st.write("Empan de chiffres inverse")

with tab3:
    st.write("📊 Scores")

with tab4:
    st.write("📄 Rapport")
