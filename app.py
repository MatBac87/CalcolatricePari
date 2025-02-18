import streamlit as st

st.set_page_config(page_title="Calcolatrice Pari 🔢", page_icon="🧮")

# Stile CSS personalizzato
st.markdown("""
<style>
div[data-testid="stTextInput"] input {
    font-size: 20px !important;
    text-align: right !important;
}
button {
    background-color: #4CAF50 !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

def controlla_pari(num):
    try:
        return int(num) % 2 == 0
    except:
        return False

# Interfaccia
st.title("Calcolatrice per Numeri Pari 🧮")
st.write("Inserisci **solo numeri pari**!")

col1, col2 = st.columns(2)

with col1:
    num1 = st.text_input("Primo numero", placeholder="Es: 4")
with col2:
    num2 = st.text_input("Secondo numero", placeholder="Es: 6")

operazione = st.selectbox("Operazione", ["+", "-", "×", "÷"])

# Logica di calcolo
if st.button("Calcola 🔍"):
    errori = []
    
    if not num1 or not num2:
        errori.append("⚠️ Inserisci entrambi i numeri!")
    else:
        if not controlla_pari(num1):
            errori.append(f"❌ {num1} non è pari!")
        if not controlla_pari(num2):
            errori.append(f"❌ {num2} non è pari!")
    
    if errori:
        for errore in errori:
            st.error(errore)
    else:
        try:
            n1 = int(num1)
            n2 = int(num2)
            
            if operazione == "+":
                risultato = n1 + n2
            elif operazione == "-":
                risultato = n1 - n2
            elif operazione == "×":
                risultato = n1 * n2
            elif operazione == "÷":
                if n2 == 0:
                    raise ZeroDivisionError
                risultato = n1 / n2
            
            st.success(f"**Risultato:** {risultato}")
            
        except ZeroDivisionError:
            st.error("Non puoi dividere per zero! 🚫")
        except Exception as e:
            st.error(f"Errore: {str(e)}")
