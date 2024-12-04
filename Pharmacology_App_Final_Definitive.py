
import streamlit as st

# Configuração inicial do aplicativo
st.set_page_config(
    page_title="Pharmacology Insights",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo personalizado para design moderno
st.markdown(
    '''
    <style>
    body {
        font-family: "Arial", sans-serif;
        background-color: #f8f9fa;
    }
    .sidebar .sidebar-content {
        background-color: #343a40;
        color: white;
    }
    h1 {
        color: #007bff;
        font-size: 36px;
        font-weight: bold;
    }
    h2 {
        color: #0056b3;
        font-size: 28px;
    }
    .stButton button {
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton button:hover {
        background-color: #0056b3;
    }
    </style>
    ''',
    unsafe_allow_html=True
)

# Página inicial
def home_page():
    st.title("Pharmacology Insights")
    st.subheader("Bem-vindo ao mundo dos medicamentos")
    st.write("Explore o conhecimento farmacológico e descubra os benefícios das principais classes terapêuticas.")
    st.write("### Escolha um tópico para explorar:")
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
    "Anti-hipertensivos": '''
### Anti-hipertensivos
Medicamentos usados para controlar a pressão arterial elevada.

#### Principais Classes:
- **Inibidores da ECA:** Reduzem a produção de angiotensina II.
- **Bloqueadores de Receptores de Angiotensina II:** Relaxam os vasos sanguíneos.
- **Bloqueadores de Canais de Cálcio:** Diminuem a contração muscular nos vasos.
''',
    "Ansiolíticos": '''
### Ansiolíticos
Medicamentos que reduzem sintomas de ansiedade.

#### Principais Classes:
- **Benzodiazepínicos:** Potencializam o efeito do GABA.
- **Buspirona:** Um ansiolítico não sedativo.
''',
    "Antidepressivos": '''
### Antidepressivos
Utilizados para tratar transtornos depressivos.

#### Principais Classes:
- **Inibidores da Recaptação de Serotonina:** Aumentam os níveis de serotonina.
- **Tricíclicos:** Melhoram a regulação dos neurotransmissores.
''',
    "Antibióticos": '''
### Antibióticos
Combatem infecções bacterianas.

#### Principais Classes:
- **Penicilinas:** Inibem a síntese da parede celular bacteriana.
- **Macrolídeos:** Interferem na síntese de proteínas.
''',
    "Analgésicos": '''
### Analgésicos
Medicamentos para alívio da dor e febre.

#### Principais Classes:
- **AINEs:** Reduzem inflamações e dores.
- **Opioides:** Bloqueiam sinais de dor ao ligar-se a receptores específicos.
'''
}

# Função para exibir páginas de cada classe
def class_page(page):
    st.title(page)
    st.markdown(content[page])

# Navegação entre páginas
if "page" not in st.session_state:
    st.session_state["page"] = "Home"

if st.session_state["page"] == "Home":
    home_page()
else:
    class_page(st.session_state["page"])

# Menu lateral
st.sidebar.title("Menu")
if st.sidebar.button("Página Inicial"):
    st.session_state["page"] = "Home"
for page in content.keys():
    if st.sidebar.button(page):
        st.session_state["page"] = page
