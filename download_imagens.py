import requests
import pandas as pd
import os
import time

# Ler o arquivo CSV com os links das imagens
df = pd.read_csv('imagens.csv')

# Pasta de destino para as imagens
pasta_destino = 'imagens'

# Verificar se a pasta de destino existe, se não, criar
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

# Verificar se o arquivo de registro existe, se não, criar um novo
registro_arquivo = 'registro.csv'
if not os.path.exists(registro_arquivo):
    df['baixado'] = False
    df.to_csv(registro_arquivo, index=False)

# Ler o arquivo de registro
registro_df = pd.read_csv(registro_arquivo)

# Loop através das linhas do DataFrame
for index, row in df.iterrows():
    if not registro_df.at[index, 'baixado']:
        link_imagem = row['image']
        nome_arquivo = os.path.basename(link_imagem)
        success = False
        max_attempts = 5  # Número máximo de tentativas
        attempts = 0

        while not success and attempts < max_attempts:
            try:
                response = requests.get(link_imagem)
                if response.status_code == 200:
                    with open(os.path.join(pasta_destino, nome_arquivo), 'wb') as file:
                        file.write(response.content)
                    print(f'Imagem {nome_arquivo} baixada com sucesso!')
                    registro_df.at[index, 'baixado'] = True
                    registro_df.to_csv(registro_arquivo, index=False)
                    success = True
                else:
                    print(f'Falha ao baixar a imagem {nome_arquivo}, tentando novamente...')
            except Exception as e:
                print(f'Erro ao baixar a imagem {nome_arquivo}: {str(e)}, tentando novamente...')
            attempts += 1

        if not success:
            print(f'Não foi possível baixar a imagem {nome_arquivo} após {max_attempts} tentativas.')

        time.sleep(1)  # Aguardar 1 segundo entre as tentativas para evitar sobrecarregar o servidor