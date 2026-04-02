CREATE DATABASE Users_Sistema
GO
USE Users_Sistema

CREATE TABLE Usuario(
    ID_Usuario int PRIMARY KEY IDENTITY(1,1) NOT NULL,
    Username varchar(20) NOT NULL,
    Senha VARCHAR(20) NOT NULL
);

INSERT INTO Usuario(Username, Senha) VALUES
('NpcTeste1', '1234abcd'), -- só pra testar a integração msm
('NpcTeste2', '4321dcba'); -- só pra testar a integração msm
select * from Usuario