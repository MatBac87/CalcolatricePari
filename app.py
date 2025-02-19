import streamlit as st
from operator import add, sub, mul, truediv

st.set_page_config(page_title="Calcolatrice Pari 🧮", page_icon="➗")

# Stile CSS personalizzato
st.markdown("""
<style>
div[data-testid="stVerticalBlock"] > div:first-child {
    background-color: #2d2d2c;
    padding: 10px;
    border-radius: 5px;
}

div[data-testid="stVerticalBlock"] > div:first-child input {
    color: white !important;
    font-size: 24px !important;
    text-align: right !important;
    background-color: #2d2d2d !important;
    border: none !important;
}

button[kind="secondary"] {
    width: 100% !important;
    height: 50px !important;
    font-size: 18px !important;
    border-radius: 5px !important;
    margin: 2px !important;
}

button.number {
    background-color: #4a4a4a !important;
    color: white !important;
}

button.operator {
    background-color: #ff9500 !important;
    color: white !important;
}

button.special {
    background-color: #a6a6a6 !important;
    color: black !important;
}
</style>
""", unsafe_allow_html=True)

if "display" not in st.session_state:
    st.session_state.display = ""
if "first_num" not in st.session_state:
    st.session_state.first_num = None
if "operation" not in st.session_state:
    st.session_state.operation = None

def controlla_pari(num):
    try:
        return int(num) % 2 == 0
    except:
        return False

def update_display(value):
    st.session_state.display += value

def set_operation(op):
    if st.session_state.display:
        st.session_state.first_num = int(st.session_state.display)
        st.session_state.operation = op
        st.session_state.display = ""

def calculate():
    if st.session_state.first_num is not None and st.session_state.display:
        try:
            num2 = int(st.session_state.display)
            
            if not controlla_pari(st.session_state.first_num) or not controlla_pari(num2):
                st.error("Entrambi i numeri devono essere pari!")
                reset()
                return
                
            ops = {
                "+": add, "-": sub, 
                "×": mul, "÷": truediv
            }
            
            result = ops[st.session_state.operation](
                st.session_state.first_num, num2
            )
            
            st.session_state.display = str(result)
            st.session_state.first_num = None
            st.session_state.operation = None
            
        except ZeroDivisionError:
            st.error("Divisione per zero non permessa!")
            reset()

def reset():
    st.session_state.display = ""
    st.session_state.first_num = None
    st.session_state.operation = None

# Interfaccia
st.title("Calcolatrice Pari 🧮")
display = st.text_input("", value=st.session_state.display, key="calc_display", disabled=True)

# Griglia pulsanti
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button("7", on_click=update_display, args=("7",), key="7", kwargs={"class": "number"})
    st.button("4", on_click=update_display, args=("4",), key="4", kwargs={"class": "number"})
    st.button("1", on_click=update_display, args=("1",), key="1", kwargs={"class": "number"})
    st.button("0", on_click=update_display, args=("0",), key="0", kwargs={"class": "number"})

with col2:
    st.button("8", on_click=update_display, args=("8",), key="8", kwargs={"class": "number"})
    st.button("5", on_click=update_display, args=("5",), key="5", kwargs={"class": "number"})
    st.button("2", on_click=update_display, args=("2",), key="2", kwargs={"class": "number"})
    st.button("C", on_click=reset, key="clear", kwargs={"class": "special"})

with col3:
    st.button("9", on_click=update_display, args=("9",), key="9", kwargs={"class": "number"})
    st.button("6", on_click=update_display, args=("6",), key="6", kwargs={"class": "number"})
    st.button("3", on_click=update_display, args=("3",), key="3", kwargs={"class": "number"})
    st.button("=", on_click=calculate, key="equals", kwargs={"class": "operator"})

with col4:
    st.button("÷", on_click=set_operation, args=("÷",), key="divide", kwargs={"class": "operator"})
    st.button("×", on_click=set_operation, args=("×",), key="multiply", kwargs={"class": "operator"})
    st.button("-", on_click=set_operation, args=("-",), key="subtract", kwargs={"class": "operator"})
    st.button("+", on_click=set_operation, args=("+",), key="add", kwargs={"class": "operator"})

st.write("⚠️ Solo numeri pari! I risultati possono essere pari o dispari")

# Gestione errori automatica
if st.session_state.display and not st.session_state.display[-1].isdigit():
    st.session_state.display = st.session_state.display[:-1]
