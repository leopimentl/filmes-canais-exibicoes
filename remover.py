import streamlit as st
import mysql.connector

def create_connection():
    
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Programacoes_Filmes"
    )
    return cnx

def remover():
    st.header("Operação de Remoção")
    st.markdown("---")
    opcao = st.radio("Selecione a aba:", ("Filmes", "Canais", "Exibições"))

    cnx = create_connection()
    cursor = cnx.cursor()

    # Remover Filmes
    if opcao == 'Filmes':
        st.subheader("Remover Filmes")

        cursor.execute("SELECT num_filme, titulo_brasil FROM Filme")
        filmes = cursor.fetchall()
        valores_filmes = {str(row[0]): row[1] for row in filmes}

        with st.form(key="remove_filme"):
            input_num_filme = st.selectbox(label="Selecione o Filme", options=list(valores_filmes.keys()), format_func=lambda x: valores_filmes[x])
            submit_button = st.form_submit_button(label="Remover Filme")

            if submit_button:
                cursor.execute("DELETE FROM Filme WHERE num_filme=%s", (input_num_filme,))
                cnx.commit()
                st.success("Filme removido com sucesso!")

    # Remover Canais
    elif opcao == 'Canais':
        st.subheader("Remover Canais")

        cursor.execute("SELECT num_canal, nome FROM Canal")
        canais = cursor.fetchall()
        valores_canais = {str(row[0]): row[1] for row in canais}

        with st.form(key="remove_canal"):
            input_num_canal = st.selectbox(label="Selecione o Canal", options=list(valores_canais.keys()), format_func=lambda x: valores_canais[x])
            submit_button = st.form_submit_button(label="Remover Canal")

            if submit_button:
                cursor.execute("DELETE FROM Canal WHERE num_canal=%s", (input_num_canal,))
                cnx.commit()
                st.success("Canal removido com sucesso!")

    # Remover Exibições
    elif opcao == 'Exibições':
        st.subheader("Remover Exibições")

        cursor.execute("SELECT e.num_filme, e.num_canal, e.data_exibicao, f.titulo_brasil, c.nome FROM Exibicoes e JOIN Filme f ON e.num_filme = f.num_filme JOIN Canal c ON e.num_canal = c.num_canal")
        exibicoes = cursor.fetchall()
        valores_exibicoes = {f"{row[3]} no {row[4]} em {row[2]}": (row[0], row[1], row[2]) for row in exibicoes}

        with st.form(key="remove_exibicao"):
            input_exibicao = st.selectbox(label="Selecione a Exibição", options=list(valores_exibicoes.keys()))
            num_filme, num_canal, data_exibicao = valores_exibicoes[input_exibicao]
            submit_button = st.form_submit_button(label="Remover Exibição")

            if submit_button:
                cursor.execute("DELETE FROM Exibicoes WHERE num_filme=%s AND num_canal=%s AND data_exibicao=%s", (num_filme, num_canal, data_exibicao))
                cnx.commit()
                st.success("Exibição removida com sucesso!")

    cursor.close()
    cnx.close()