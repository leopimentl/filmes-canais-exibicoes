CREATE DATABASE Programacoes_Filmes;

USE Programacoes_Filmes;

CREATE TABLE Canal (
    num_canal INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50),
    sigla VARCHAR(25)
);

CREATE TABLE Filme (
    num_filme INT PRIMARY KEY AUTO_INCREMENT,
    titulo_original VARCHAR(80) NOT NULL,
    titulo_brasil VARCHAR(255),
    pais_origem VARCHAR(30),
    categoria VARCHAR(25),
    duracao INT NOT NULL
);

CREATE TABLE Exibicoes (
    num_filme INT,
    num_canal INT,
    data_exibicao DATETIME,
    PRIMARY KEY(num_filme, num_canal, data_exibicao),
    FOREIGN KEY(num_filme) REFERENCES Filme(num_filme) ON DELETE CASCADE,
    FOREIGN KEY(num_canal) REFERENCES Canal(num_canal) ON DELETE CASCADE
);

DELIMITER //

CREATE TRIGGER before_insert_filme
BEFORE INSERT ON Filme
FOR EACH ROW
BEGIN
    IF NEW.duracao <= 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'A duração do filme deve ser maior que 0';
    END IF;
END //

DELIMITER ;