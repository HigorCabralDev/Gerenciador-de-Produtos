# Gerenciador de Produtos

Sistema CRUD desenvolvido em Python para gerenciamento de produtos, utilizando Tkinter para a interface gráfica e PostgreSQL para armazenamento dos dados.

## Funcionalidades

O sistema permite:

- Cadastrar produtos
- Listar produtos
- Atualizar produtos
- Excluir produtos
- Selecionar registros na tabela
- Limpar os campos do formulário
- Armazenar os dados no PostgreSQL

## Tecnologias utilizadas

- Python
- Tkinter
- PostgreSQL
- Psycopg2

## Banco de Dados

O projeto utiliza PostgreSQL como banco de dados.

A tabela principal utilizada é:

```sql
CREATE TABLE PRODUTO (
    CODIGO SERIAL PRIMARY KEY,
    NOME VARCHAR(100) NOT NULL,
    PRECO NUMERIC(10, 2) NOT NULL
);
