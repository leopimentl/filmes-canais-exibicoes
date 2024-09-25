-- Consultas Extras
-- Consulta 1: Número de Exibições por Canal
SELECT c.nome AS nome_canal, COUNT(e.num_filme) AS total_exibicoes
FROM Exibicoes e
JOIN Canal c ON e.num_canal = c.num_canal
GROUP BY c.nome;

-- Consulta 2: Duração Média dos Filmes por Categoria
SELECT f.categoria, AVG(f.duracao) AS duracao_media
FROM Filme f
GROUP BY f.categoria;

-- Consulta 3: Exibições por Filme e Canal
SELECT f.titulo_brasil AS nome_filme, c.nome AS nome_canal, COUNT(e.data_exibicao) AS total_exibicoes
FROM Exibicoes e
JOIN Filme f ON e.num_filme = f.num_filme
JOIN Canal c ON e.num_canal = c.num_canal
GROUP BY f.titulo_brasil, c.nome;