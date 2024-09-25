-- Populando a tabela Canal
INSERT INTO Canal (num_canal, nome, sigla) VALUES
(1, 'Canal de Filmes', 'CF'),
(2, 'Cinema 24h', 'C24'),
(3, 'Filmes Clássicos', 'FC');

-- Populando a tabela Filme
INSERT INTO Filme (num_filme, titulo_original, titulo_brasil, pais_origem, categoria, duracao) VALUES
(1, 'The Shawshank Redemption', 'Um Sonho de Liberdade', 'EUA', 'Drama', 142),
(2, 'The Godfather', 'O Poderoso Chefão', 'EUA', 'Crime', 175),
(3, 'The Dark Knight', 'Batman: O Cavaleiro das Trevas', 'EUA', 'Ação', 152);

-- Populando a tabela Exibicoes
INSERT INTO Exibicoes (num_filme, num_canal, data_exibicao) VALUES
(1, 1, '2024-09-16 20:00:00'),
(2, 2, '2024-09-17 22:00:00'),
(3, 3, '2024-09-18 21:00:00'),
(1, 2, '2024-09-19 19:00:00'),
(2, 3, '2024-09-20 23:00:00');

-- Trigger em execução
-- INSERT INTO Filme (num_filme, titulo_original, titulo_brasil, pais_origem, categoria, duracao) VALUES(8, 'The Shawshank Redemption', 'Um Sonho de Liberdade', 'EUA', 'Drama', 0);
