import pandas as pd
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

def consultar():
    st.header("Consulta de Dados")
    st.markdown("---")
    tab_selected = st.selectbox("Selecione a tabela para consultar:", ["Canais", "Filmes", "Exibições", "Consultas Avançadas"])

    cnx = create_connection()

    if tab_selected == "Canais":
        # Consultar e exibir os dados da tabela "canais"
        st.subheader("Tabela Canais")
        query_canais = "SELECT * FROM Canal"
        df_canais = pd.read_sql_query(query_canais, cnx)
        st.dataframe(df_canais)

    elif tab_selected == "Filmes":
        # Consultar e exibir os dados da tabela "filmes"
        st.subheader("Tabela Filmes")
        query_filmes = "SELECT * FROM Filme"
        df_filmes = pd.read_sql_query(query_filmes, cnx)
        st.dataframe(df_filmes)

    elif tab_selected == "Exibições":
        # Consultar e exibir os dados da tabela "exibições" com detalhes adicionais
        st.subheader("Tabela Exibições")
        query_exibicoes = """
        SELECT e.num_filme, f.titulo_brasil AS nome_filme, e.num_canal, c.nome AS nome_canal, e.data_exibicao
        FROM Exibicoes e
        JOIN Filme f ON e.num_filme = f.num_filme
        JOIN Canal c ON e.num_canal = c.num_canal
        """
        df_exibicoes = pd.read_sql_query(query_exibicoes, cnx)
        st.dataframe(df_exibicoes)

    elif tab_selected == "Consultas Avançadas":
        consultas_avancadas(cnx)

    # Fechar a conexão com o banco de dados
    cnx.close()

def consultas_avancadas(cnx):
    st.subheader("Consultas Avançadas")

    # Consulta 1: Número de Exibições por Canal
    st.markdown("### Número de Exibições por Canal")
    query1 = """
    SELECT c.nome AS nome_canal, COUNT(e.num_filme) AS total_exibicoes
    FROM Exibicoes e
    JOIN Canal c ON e.num_canal = c.num_canal
    GROUP BY c.nome;
    """
    df_query1 = pd.read_sql_query(query1, cnx)
    st.dataframe(df_query1)

    # Consulta 2: Duração Média dos Filmes por Categoria
    st.markdown("### Duração Média dos Filmes por Categoria")
    query2 = """
    SELECT f.categoria, AVG(f.duracao) AS duracao_media
    FROM Filme f
    GROUP BY f.categoria;
    """
    df_query2 = pd.read_sql_query(query2, cnx)
    st.dataframe(df_query2)

    # Consulta 3: Exibições por Filme e Canal
    st.markdown("### Exibições por Filme e Canal")
    query3 = """
    SELECT f.titulo_brasil AS nome_filme, c.nome AS nome_canal, COUNT(e.data_exibicao) AS total_exibicoes
    FROM Exibicoes e
    JOIN Filme f ON e.num_filme = f.num_filme
    JOIN Canal c ON e.num_canal = c.num_canal
    GROUP BY f.titulo_brasil, c.nome;
    """
    df_query3 = pd.read_sql_query(query3, cnx)
    st.dataframe(df_query3)