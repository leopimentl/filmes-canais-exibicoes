import streamlit as st
from consultar import *
from cadastrar import *
from atualizar import *
from remover import *

st.set_page_config(
    page_title="Operações CRUD",
    page_icon="📄",
    layout= 'centered'
)

def main():
    st.sidebar.title('Operações CRUD')
    st.sidebar.markdown("---")
    
    tabs = ["Consultar", "Cadastrar", "Atualizar", "Remover"]
    selected_tab = st.sidebar.radio("Selecione a operação que deseja realizar", tabs)

    if selected_tab == "Consultar":
        consultar()
    elif selected_tab == "Cadastrar":
        cadastrar()
    elif selected_tab == "Remover":
        remover()
    elif selected_tab == "Atualizar":
        atualizar()

if __name__ == "__main__":
    main()
