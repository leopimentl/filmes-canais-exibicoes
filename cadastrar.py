import streamlit as st
import mysql.connector

def create_connection():
    # Substitua as informações abaixo pelas suas credenciais do banco de dados
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Programacoes_Filmes"
    )
    return cnx

def cadastrar():
    st.header("Operação de Cadastro")
    st.markdown("---")
    opcao = st.radio("Selecione a aba:", ("Filmes", "Canais", "Exibições"))

    cnx = create_connection()
    cursor = cnx.cursor()

    # Cadastrar Filmes
    if opcao == 'Filmes':
        st.subheader("Cadastrar Filmes")

        with st.form(key="include_filme"):
            input_titulo_original = st.text_input(label="Insira o Título Original do Filme", max_chars=100)
            input_titulo_brasil = st.text_input(label="Insira o Título no Brasil", max_chars=100)
            input_pais_origem = st.text_input(label="Insira o País de Origem", max_chars=50)
            input_categoria = st.text_input(label="Insira a Categoria do Filme", max_chars=50)
            input_duracao = st.number_input(label="Insira a Duração do Filme (em minutos)", min_value=0)

            submit_button = st.form_submit_button(label="Cadastrar Filme")

            if submit_button:
                cursor.execute(
                    "INSERT INTO Filme (titulo_original, titulo_brasil, pais_origem, categoria, duracao) VALUES (%s, %s, %s, %s, %s)",
                    (input_titulo_original, input_titulo_brasil, input_pais_origem, input_categoria, input_duracao)
                )
                cnx.commit()
                st.success("Filme cadastrado com sucesso!")

    # Cadastrar Canais
    elif opcao == 'Canais':
        st.subheader("Cadastrar Canais")

        with st.form(key="include_canal"):
            input_nome = st.text_input(label="Insira o Nome do Canal", max_chars=100)
            input_sigla = st.text_input(label="Insira a Sigla do Canal", max_chars=10)

            submit_button = st.form_submit_button(label="Cadastrar Canal")

            if submit_button:
                cursor.execute(
                    "INSERT INTO Canal (nome, sigla) VALUES (%s, %s)",
                    (input_nome, input_sigla)
                )
                cnx.commit()
                st.success("Canal cadastrado com sucesso!")

    # Cadastrar Exibições
    elif opcao == 'Exibições':
        st.subheader("Cadastrar Exibições")

        cursor.execute("SELECT num_filme, titulo_brasil FROM Filme")
        filmes = cursor.fetchall()
        valores_filmes = {str(row[0]): row[1] for row in filmes}

        cursor.execute("SELECT num_canal, nome FROM Canal")
        canais = cursor.fetchall()
        valores_canais = {str(row[0]): row[1] for row in canais}

        with st.form(key="include_exibicao"):
            input_num_filme = st.selectbox(label="Selecione o Filme", options=list(valores_filmes.keys()), format_func=lambda x: valores_filmes[x])
            input_num_canal = st.selectbox(label="Selecione o Canal", options=list(valores_canais.keys()), format_func=lambda x: valores_canais[x])
            input_data_exibicao = st.date_input(label="Selecione a Data de Exibição")
            input_hora_exibicao = st.time_input(label="Selecione a Hora de Exibição")

            submit_button = st.form_submit_button(label="Cadastrar Exibição")

            if submit_button:
                data_hora_exibicao = f"{input_data_exibicao} {input_hora_exibicao}"
                cursor.execute(
                    "INSERT INTO Exibicoes (num_filme, num_canal, data_exibicao) VALUES (%s, %s, %s)",
                    (input_num_filme, input_num_canal, data_hora_exibicao)
                )
                cnx.commit()
                st.success("Exibição cadastrada com sucesso!")

    cursor.close()
    cnx.close()