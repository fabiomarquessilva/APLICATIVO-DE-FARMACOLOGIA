
import streamlit as st

# Configuração inicial do aplicativo
st.set_page_config(
    page_title="Curso de Farmacologia",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Função para exibir páginas das classes de medicamentos
def class_page(title, content):
    st.title(title)
    st.write(content)

# Página inicial com botões de navegação
def home_page():
    st.title("Bem-vindo ao Curso de Farmacologia")
    st.write(
        "Olá! Eu sou o **Prof. Dr. Fábio Marques**. Este aplicativo foi desenvolvido "
        "para guiar você pelos fundamentos da farmacologia, incluindo tópicos como "
        "farmacocinética, farmacodinâmica, classes de fármacos e muito mais."
    )
    st.write("### Explore as Classes de Medicamentos:")
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
    "Anti-hipertensivos": (
        "### Anti-hipertensivos

"
        "Medicamentos usados para tratar hipertensão arterial. Exemplos:
"
        "- **Inibidores da ECA:** Captopril, Enalapril.
"
        "- **Bloqueadores de Receptores de Angiotensina II:** Losartana, Valsartana.
"
        "- **Bloqueadores de Canais de Cálcio:** Amlodipino, Verapamil."
    ),
    "Ansiolíticos": (
        "### Ansiolíticos

"
        "Medicamentos ansiolíticos ajudam a aliviar sintomas de ansiedade. Exemplos:
"
        "- **Benzodiazepínicos:** Diazepam, Lorazepam.
"
        "- **Buspirona:** Um ansiolítico não sedativo."
    ),
    "Antidepressivos": (
        "### Antidepressivos

"
        "Utilizados para tratar transtornos depressivos. Exemplos:
"
        "- **Inibidores da Recaptação de Serotonina:** Fluoxetina, Sertralina.
"
        "- **Tricíclicos:** Amitriptilina, Nortriptilina."
    ),
    "Antibióticos": (
        "### Antibióticos

"
        "Utilizados para tratar infecções bacterianas. Exemplos:
"
        "- **Penicilinas:** Amoxicilina, Penicilina G.
"
        "- **Macrolídeos:** Azitromicina, Claritromicina."
    ),
    "Analgésicos": (
        "### Analgésicos

"
        "Medicamentos para alívio da dor e redução da febre. Exemplos:
"
        "- **AINEs:** Ibuprofeno, Naproxeno.
"
        "- **Opioides:** Morfina, Tramadol."
    ),
}

# Configuração inicial da navegação
if "page" not in st.session_state:
    st.session_state["page"] = "Home"

# Controle de navegação
if st.session_state["page"] == "Home":
    home_page()
else:
    class_page(st.session_state["page"], content[st.session_state["page"]])

# Menu lateral para navegação rápida
st.sidebar.title("Menu")
if st.sidebar.button("Página Inicial"):
    st.session_state["page"] = "Home"
for page in content.keys():
    if st.sidebar.button(page):
        st.session_state["page"] = page
