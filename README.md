# API de Carros

Esta é uma API simples desenvolvida com Flask para gerenciar uma lista de carros. A API permite consultas (GET) e a criação de novos carros (POST).

## Funcionalidades

- **GET /carros**: Retorna uma lista de carros com uma mensagem.
- **POST /carros**: Cria um novo carro a partir dos dados fornecidos.

## Estrutura do Projeto

.

├── app.py # Código principal da API

├── bd.py # Simulação do banco de dados (lista de carros)

└── README.md # Este documento


## Uso

### Requisição GET

Para obter a lista de carros, você pode fazer uma requisição GET para o endpoint `/carros`.

#### Exemplo de Resposta

[Consulta GET](imagens/get-carros.jpg)

### Requisição POST

Para criar um novo carro, envie uma requisição POST para o endpoint `/carros` com um corpo JSON.

### Exemplo de Requisição

- **URL**: `http://127.0.0.1:5000/carros`
- **Método**: POST
- **Corpo da Requisição**:
  
```json
{
    "id": 6,
    "marca": "Fiat",
    "modelo": "Elba",
    "ano": 1997
}
```
[Exemplo de Resposta da Requisição POST](imagens/post-carros.jpg)

## Instalação

Clone este repositório para sua máquina local:

git clone https://github.com/seu_usuario/seu_repositorio.git

cd seu_repositorio

### Instale as dependências necessárias:

pip install Flask

### Execute a aplicação:
python app.py

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou correções. Faça um fork deste repositório, faça suas alterações e envie um pull request.
