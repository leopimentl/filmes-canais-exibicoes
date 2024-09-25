import mysql.connector
import streamlit as st
from datetime import datetime

def create_connection():
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Programacoes_Filmes"
    )
    return cnx

def atualizar():
    st.header("Operação de Atualização")
    st.markdown("---")
    opcao = st.radio("Selecione a aba:", ("Filmes", "Canais", "Exibições"))

    cnx = create_connection()
    cursor = cnx.cursor()

    # Atualizar Filmes
    if opcao == 'Filmes':
        st.subheader("Atualizar Filmes")

        cursor.execute("SELECT num_filme, titulo_brasil FROM Filme")
        filmes = cursor.fetchall()
        valores_filmes = {row[1]: row[0] for row in filmes}

        with st.form(key="update_filme"):
            input_titulo_brasil = st.selectbox(label="Selecione o Filme", options=list(valores_filmes.keys()))
            input_titulo_original = st.text_input(label="Insira o Novo Título Original do Filme", max_chars=100)
            input_pais_origem = st.text_input(label="Insira o Novo País de Origem", max_chars=50)
            input_categoria = st.text_input(label="Insira a Nova Categoria do Filme", max_chars=50)
            input_duracao = st.number_input(label="Insira a Nova Duração do Filme (em minutos)", min_value=0)

            submit_button = st.form_submit_button(label="Atualizar Filme")

            if submit_button:
                num_filme = valores_filmes[input_titulo_brasil]
                cursor.execute(
                    "UPDATE Filme SET titulo_original=%s, titulo_brasil=%s, pais_origem=%s, categoria=%s, duracao=%s WHERE num_filme=%s",
                    (input_titulo_original, input_titulo_brasil, input_pais_origem, input_categoria, input_duracao, num_filme)
                )
                cnx.commit()
                st.success("Filme atualizado com sucesso!")

    # Atualizar Canais
    elif opcao == 'Canais':
        st.subheader("Atualizar Canais")

        cursor.execute("SELECT num_canal, nome FROM Canal")
        canais = cursor.fetchall()
        valores_canais = {row[1]: row[0] for row in canais}

        with st.form(key="update_canal"):
            input_nome = st.selectbox(label="Selecione o Canal", options=list(valores_canais.keys()))
            input_sigla = st.text_input(label="Insira a Nova Sigla do Canal", max_chars=10)

            submit_button = st.form_submit_button(label="Atualizar Canal")

            if submit_button:
                num_canal = valores_canais[input_nome]
                cursor.execute(
                    "UPDATE Canal SET nome=%s, sigla=%s WHERE num_canal=%s",
                    (input_nome, input_sigla, num_canal)
                )
                cnx.commit()
                st.success("Canal atualizado com sucesso!")

        # Atualizar Exibições
    elif opcao == 'Exibições':
        st.subheader("Atualizar Exibições")
    
        cursor.execute("SELECT e.num_filme, e.num_canal, e.data_exibicao, f.titulo_brasil, c.nome FROM Exibicoes e JOIN Filme f ON e.num_filme = f.num_filme JOIN Canal c ON e.num_canal = c.num_canal")
        exibicoes = cursor.fetchall()
        valores_exibicoes = {f"{row[3]} no {row[4]} em {row[2]}": (row[0], row[1], row[2]) for row in exibicoes}
    
        cursor.execute("SELECT num_filme, titulo_brasil FROM Filme")
        filmes = cursor.fetchall()
        valores_filmes = {row[1]: row[0] for row in filmes}
    
        cursor.execute("SELECT num_canal, nome FROM Canal")
        canais = cursor.fetchall()
        valores_canais = {row[1]: row[0] for row in canais}
    
        with st.form(key="update_exibicao"):
            input_exibicao = st.selectbox("Selecione a Exibição para Atualizar", options=list(valores_exibicoes.keys()))
            input_num_filme = st.selectbox("Selecione o Novo Filme", options=list(valores_filmes.keys()), format_func=lambda x: x)
            input_num_canal = st.selectbox("Selecione o Novo Canal", options=list(valores_canais.keys()), format_func=lambda x: x)
            input_data_exibicao = st.date_input("Selecione a Nova Data de Exibição")
            input_hora_exibicao = st.time_input("Selecione a Nova Hora de Exibição")
    
            submit_button = st.form_submit_button(label="Atualizar Exibição")
    
            if submit_button:
                num_filme, num_canal, data_exibicao = valores_exibicoes[input_exibicao]
                novo_num_filme = valores_filmes[input_num_filme]
                novo_num_canal = valores_canais[input_num_canal]
                nova_data_hora_exibicao = f"{input_data_exibicao} {input_hora_exibicao}"
    
                cursor.execute(
                    "UPDATE Exibicoes SET num_filme = %s, num_canal = %s, data_exibicao = %s WHERE num_filme = %s AND num_canal = %s AND data_exibicao = %s",
                    (novo_num_filme, novo_num_canal, nova_data_hora_exibicao, num_filme, num_canal, data_exibicao)
                )
                cnx.commit()
                st.success("Exibição atualizada com sucesso!")

    cursor.close()
    cnx.close()