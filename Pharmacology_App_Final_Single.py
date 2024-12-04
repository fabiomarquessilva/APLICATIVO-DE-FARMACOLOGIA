
import streamlit as st

# Configuração inicial do aplicativo
st.set_page_config(page_title="Anti-hipertensivos", layout="wide")

# Página única: Anti-hipertensivos
def anti_hypertensive_page():
    st.title("Anti-hipertensivos")
    st.write("Anti-hipertensivos são medicamentos usados para tratar a hipertensão arterial (pressão alta).")
    st.write("### Principais Classes:")
    st.write("- **Inibidores da ECA:** Captopril, Enalapril.")
    st.write("- **Bloqueadores de Receptores de Angiotensina II:** Losartana, Valsartana.")
    st.write("- **Bloqueadores de Canais de Cálcio:** Amlodipino, Verapamil.")
    st.write("### Como Funcionam:")
    st.write("- Relaxam os vasos sanguíneos.")
    st.write("- Diminuem a frequência cardíaca.")
    st.write("- Reduzem a resistência dos vasos.")
    st.write("### Benefícios:")
    st.write("- Reduzem o risco de ataques cardíacos e AVC.")
    st.write("- Protegem contra danos renais em pacientes com diabetes.")

# Exibindo a página diretamente
anti_hypertensive_page()
