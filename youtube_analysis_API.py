import os
from dotenv import load_dotenv  
import pandas as pd
import requests
import streamlit as st
from pprint import pprint
load_dotenv()
api_key = os.environ["CHAVE_API_YOUTUBE_DATA_V3"]

#First get the channel ID from the channel name input by the user
def get_channel_id(channel_name, api_key=api_key):   
    url = 'https://www.googleapis.com/youtube/v3/search'
    params = {
        'part': 'snippet',
        'q': channel_name,
        'type': 'channel',
        'key': api_key
    }
    resposta = requests.get(url=url, params=params)
    try:
        resposta.raise_for_status()
    except requests.HTTPError as e:
        print(f"Erro no request: {e}")
        resultado = None
    else:
        print("ID encontrado!")
        resultado = resposta.json()
    if resultado and resultado['items']:
        return resultado['items'][0]['id']['channelId']
    else:
        print(f"Canal '{channel_name}' não encontrado.")
        return None


#Second, from the channel ID, get the channel information and statistics
def get_channel_info(channel_id, channel_name, api_key=api_key):

    params = {
        'part': 'snippet,statistics',
        'id': channel_id,
        'key': api_key
    }

    url = f'https://www.googleapis.com/youtube/v3/channels'

    resposta = requests.get(url=url, params=params)
    try:
        resposta.raise_for_status()
    except requests.HTTPError as e:
        print(f"Erro no request: {e}")
        resultado = None
    else:
        print("Canal encontrado!")
        resultado = resposta.json()
    if resultado and resultado['items']:
        return resultado['items'][0]    
    else:
        print(f"Informações do canal '{channel_name}' não encontradas.")
        return None


def main():

    st.title('Web App - Estatísticas de Canais do YouTube')
    st.write('Dados do YouTube Data API v3 (fonte: https://developers.google.com/youtube/v3)')
    st.write('Digite o nome do canal do YouTube para obter informações e estatísticas sobre ele.')

    #User Input for the channel name
    channel_name = st.text_input('Buscar Nome do Canal:')
    if not channel_name:
        st.stop()
        
    channel_id = get_channel_id(channel_name)
    if not channel_id:
        st.warning(f"Canal '{channel_name}' não encontrado. Por favor, tente outro nome.")
        st.stop()

    channel_info = get_channel_info(channel_id, channel_name)
    if not channel_info:
        st.warning(f"Informações do canal '{channel_name}' não encontradas.")
        st.stop()
    
    st.header(f"Informações do Canal: {channel_info['snippet']['title']}", divider=True)
    
    col1, col2 = st.columns([0.3,0.7])
    with col1: 
        st.image(channel_info['snippet']['thumbnails']['default']['url'], width=200, )
        st.write(f"link de acesso ao canal: https://www.youtube.com/channel/{channel_info['id']}")
    with col2:
        st.write(f"Descrição do Canal: {channel_info['snippet']['description']}")
       

    st.divider()

    col3, col4, col5 = st.columns(3)

    col3.metric(label="Inscritos", value=channel_info['statistics']['subscriberCount'])
    col4.metric(label="Visualizações", value=channel_info['statistics']['viewCount'])
    col5.metric(label="Vídeos", value=channel_info['statistics']['videoCount'])


    st.divider()

    st.write('Web App desenvolvido por: Josué Melo - https://www.linkedin.com/in/josu%C3%A9-suman-2b9351181/ ')

if __name__ == '__main__':
    main()

