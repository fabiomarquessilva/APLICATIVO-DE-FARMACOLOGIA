
import streamlit as st

# Configuração inicial do aplicativo
st.set_page_config(
    page_title="Pharmacology Insights",
    layout="wide"
)

# Página inicial
def home_page():
    st.title("Pharmacology Insights")
    st.subheader("Desenvolvido por Prof. Dr. Fábio Marques")
    st.write("### Sobre o Autor:")
    st.write("- **Nome:** Prof. Dr. Fábio Marques")
    st.write("- **E-mail:** [ffabioms3@gmail.com](mailto:ffabioms3@gmail.com)")
    st.write("- **Especialidade:** Farmacologia e Ensino Superior")
    st.image("https://via.placeholder.com/600x300", caption="Bem-vindo ao mundo da farmacologia", use_column_width=True)
    st.write("Explore as principais classes de medicamentos e seus mecanismos de ação:")
    if st.button("Anti-hipertensivos"):
        st.session_state["page"] = "Anti-hipertensivos"
    if st.button("Ansiolíticos"):
        st.session_state["page"] = "Ansiolíticos"
    if st.button("Antidepressivos"):
        st.session_state["page"] = "Antidepressivos"
    if st.button("Antibióticos"):
        st.session_state["page"] = "Antibióticos"
    if st.button("Analgésicos"):
        st.session_state["page"] = "Analgésicos"

# Conteúdo para cada classe de medicamentos
content = {
    "Anti-hipertensivos": """
### Anti-hipertensivos
Medicamentos usados para controlar a pressão arterial elevada:
- **Inibidores da ECA:** Captopril, Enalapril
- **Bloqueadores de Receptores de Angiotensina II:** Losartana, Valsartana
- **Bloqueadores de Canais de Cálcio:** Amlodipino, Verapamil
""",
    "Ansiolíticos": """
### Ansiolíticos
Medicamentos que reduzem os sintomas de ansiedade:
- **Benzodiazepínicos:** Diazepam, Lorazepam
- **Buspirona:** Um ansiolítico não sedativo
""",
    "Antidepressivos": """
### Antidepressivos
Medicamentos utilizados para tratar transtornos depressivos:
- **Inibidores da Recaptação de Serotonina:** Fluoxetina, Sertralina
- **Tricíclicos:** Amitriptilina, Nortriptilina
""",
    "Antibióticos": """
### Antibióticos
Medicamentos que combatem infecções bacterianas:
- **Penicilinas:** Amoxicilina, Penicilina G
- **Macrolídeos:** Azitromicina, Claritromicina
""",
    "Analgésicos": """
### Analgésicos
Medicamentos para alívio da dor:
- **AINEs:** Ibuprofeno, Naproxeno
- **Opioides:** Morfina, Tramadol
"""
}

# Função para exibir páginas de conteúdo
def content_page(page):
    st.title(page)
    st.markdown(content[page])

# Navegação
if "page" not in st.session_state:
    st.session_state["page"] = "Home"

if st.session_state["page"] == "Home":
    home_page()
else:
    content_page(st.session_state["page"])

# Menu lateral
st.sidebar.title("Navegação")
if st.sidebar.button("Página Inicial"):
    st.session_state["page"] = "Home"
for key in content.keys():
    if st.sidebar.button(key):
        st.session_state["page"] = key
