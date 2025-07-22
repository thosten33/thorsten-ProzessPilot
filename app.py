
import streamlit as st

st.set_page_config(page_title="ProzessPilot", layout="centered")

st.title("📄 ProzessPilot")
st.write("Lade eine PDF hoch oder beschreibe dein Anliegen, und erhalte passende KI-Tools, Lösungen und Anleitungen.")

uploaded_file = st.file_uploader("PDF hochladen", type="pdf")

if uploaded_file:
    st.success("PDF empfangen (Demo-Modus).")
    st.write("Hier würde die Analyse starten …")

prompt = st.text_area("Oder beschreibe dein Anliegen (z. B. 'Ich will ein Review schreiben')")

if st.button("Loslegen"):
    st.write("Hier würde die KI dir eine PDF-Anleitung mit Tools und Tipps erstellen.")
