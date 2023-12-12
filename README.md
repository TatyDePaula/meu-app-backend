# Gerenciamento de Convidados - Aplicação MVP

## Descrição do Projeto

Este projeto é um MVP desenvolvido como parte da disciplina de Desenvolvimento Full Stack na PUC-RIO. A aplicação visa solucionar desafios relacionados ao gerenciamento de convidados em uma lista, servindo como base para futuras aplicações mais aprimoradas.


## Funcionalidades Atuais

A aplicação foi construída usando Flask em Python, com um banco de dados SQLite, e possui documentação disponível no Swagger. Até o momento, a API oferece três operações principais:

### 1. Cadastrar Convidado (POST)

- Rota: `/convidado`
- Descrição: Adiciona um novo convidado à lista.
- Parâmetros:
  - `nome`: Nome do convidado.
  - `numero_convidado`: Número associado ao convidado.
  - `numero_telefone`: Número de telefone do convidado.

## Como executar 

> É importante criar um ambiente virtual seguro.
```
python -m venv env
```

> Ativar o ambiente Virtual.
```
.\env\scripts\activate
```
> Instalar as libs que estão no arquivo requirements.txt.
```
(env)$ pip install -r requirements.txt
```
> Após a Instalação para executar a API:
```
(env)$ flask run --host 0.0.0.0 --port 5000
```
> É só abrir o local host no Browser para ver e testar a aplicação!

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
