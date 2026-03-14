# 📊 YouTube Channel Statistics Web App

Este projeto é um **aplicativo web em Python com Streamlit** que consulta a **YouTube Data API v3** para buscar informações públicas de canais do YouTube a partir do nome do canal informado pelo usuário.  

This project is a **Python web application built with Streamlit** that uses the **YouTube Data API v3** to fetch public information about YouTube channels based on the channel name entered by the user.

---

## 🚀 Funcionalidades | Features

### Português
- Buscar canal pelo nome
- Consultar o **ID do canal** pela API
- Exibir:
  - Nome do canal
  - Descrição
  - Foto do canal
  - Link de acesso
  - Número de inscritos
  - Número de visualizações
  - Quantidade de vídeos
- Interface web simples com **Streamlit**

### English
- Search for a channel by name
- Retrieve the **channel ID** through the API
- Display:
  - Channel name
  - Description
  - Channel image
  - Channel link
  - Number of subscribers
  - Number of views
  - Total videos
- Simple web interface built with **Streamlit**

---

## 🛠️ Tecnologias utilizadas | Technologies Used

- **Python**
- **Streamlit**
- **Requests**
- **python-dotenv**
- **Pandas**
- **YouTube Data API v3**
- 
---

## ⚙️ Como o projeto funciona | How the Project Works

### Português
O fluxo da aplicação funciona assim:

1. O usuário digita o **nome de um canal** no campo de busca.
2. A função `get_channel_id()` faz uma requisição para encontrar o canal.
3. O sistema obtém o **ID do canal**.
4. Depois, a função `get_channel_info()` usa esse ID para buscar os dados do canal.
5. As informações são exibidas na interface com Streamlit.

### English
The application flow works like this:

1. The user enters the **channel name** in the search field.
2. The function `get_channel_id()` sends a request to find the channel.
3. The system gets the **channel ID**.
4. Then, the function `get_channel_info()` uses that ID to fetch channel data.
5. The information is displayed in the Streamlit interface.

---

## 🧩 Estrutura do código | Code Structure

### `get_channel_id(channel_name, api_key)`

**Português:**  
Responsável por buscar o **ID do canal** com base no nome digitado pelo usuário.

- Endpoint usado: `search`
- Parâmetros principais:
  - `part=snippet`
  - `q=channel_name`
  - `type=channel`

Se houver resultado, retorna o `channelId`.

**English:**  
Responsible for searching the **channel ID** based on the name entered by the user.

- Endpoint used: `search`
- Main parameters:
  - `part=snippet`
  - `q=channel_name`
  - `type=channel`

If a result is found, it returns the `channelId`.

---

### `get_channel_info(channel_id, channel_name, api_key)`

**Português:**  
Responsável por buscar as **informações e estatísticas** do canal a partir do ID encontrado.

- Endpoint usado: `channels`
- Parâmetros principais:
  - `part=snippet,statistics`
  - `id=channel_id`

Retorna dados como:
- título do canal
- descrição
- thumbnail
- inscritos
- visualizações
- quantidade de vídeos

**English:**  
Responsible for fetching the **channel information and statistics** using the channel ID.

- Endpoint used: `channels`
- Main parameters:
  - `part=snippet,statistics`
  - `id=channel_id`

Returns data such as:
- channel title
- description
- thumbnail
- subscribers
- views
- number of videos

---

### `main()`

**Português:**  
É a função principal da aplicação. Ela monta a interface, recebe o nome do canal, chama as funções de busca, trata erros e exibe os dados na tela.

**English:**  
This is the main function of the application. It builds the interface, gets the channel name, calls the search functions, handles errors, and displays the data on screen.

---

## 📋 Pré-requisitos | Requirements

### Português
Antes de executar o projeto, você precisa ter:
- Python instalado
- Uma chave válida da **YouTube Data API v3**
- As bibliotecas do projeto instaladas

### English
Before running the project, you need:
- Python installed
- A valid **YouTube Data API v3** key
- The project libraries installed

---

## 📦 Instalação | Installation

Clone o repositório | Clone the repository:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

## ⚠️ Tratamento de erros | Error Handling

### Português

O projeto possui tratamento básico para:

- erro na requisição HTTP
- canal não encontrado
- informações do canal não encontradas

### English

The project includes basic handling for:

- HTTP request errors
- channel not found
- channel information not found

---

## 🔮 Melhorias futuras | Future Improvements

### Português

Algumas melhorias que podem ser implementadas:

- Buscar vídeos do canal
- Exibir playlists
- Mostrar a lista de vídeos com suas informações, para análises mais profundas
- Permitir exportação dos dados em CSV
- Melhorar a validação de entrada
- Criar uma interface mais elaborada

### English

Some possible future improvements:

- Fetch channel videos
- Display playlists
- Show de list of videos with their information, for deeper analysis
- Allow CSV export
- Improve input validation
- Create a more advanced interface

---

## 📚 Aprendizados com o projeto | What I Learned from This Project

### Português

Este projeto é uma boa prática para aprender:

- consumo de APIs REST
- uso de variáveis de ambiente
- manipulação de JSON
- criação de interfaces com Streamlit
- organização de funções em Python

### English

This project is a great way to practice:

- consuming REST APIs
- using environment variables
- handling JSON data
- building interfaces with Streamlit
- organizing functions in Python
