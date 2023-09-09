# csv-bulk-files-downloader

## Download de Imagens em Lote com Tratamento de Exceção

Este é um script Python que permite baixar imagens em lote a partir de links fornecidos em um arquivo CSV, com tratamento de exceção para tentar novamente em caso de falha.

## Pré-requisitos

- Python 3.x
- Biblioteca pandas
- Biblioteca requests
- Ambiente virtual (venv)

### Configurando um Ambiente Virtual (venv)

É altamente recomendável criar um ambiente virtual para isolar as dependências do projeto. Siga estas etapas para configurar um ambiente virtual:

1. Abra um terminal e navegue até o diretório do projeto.

2. Crie um ambiente virtual usando o comando `venv` (ou `virtualenv`, dependendo da versão do Python):

   ```
   python -m venv venv
   ```

   Isso criará um diretório chamado `venv` no seu diretório de projeto.

3. Ative o ambiente virtual:

   - No Windows:

     ```
     venv\Scripts\activate
     ```

   - No macOS e Linux:

     ```
     source venv/bin/activate
     ```

4. Agora, você está dentro do ambiente virtual e pode instalar as dependências sem afetar o sistema global.

5. Instale as bibliotecas necessárias usando o pip:

   ```
   pip install pandas requests
   ```

6. Continue com as instruções de uso abaixo.

Lembre-se de ativar o ambiente virtual sempre que for trabalhar no projeto.

## Como Usar

1. Clone este repositório em sua máquina local.

```
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

2. Certifique-se de que o arquivo CSV com os links das imagens esteja no mesmo diretório que o script e tenha uma coluna chamada "imagens" com os URLs das imagens.

3. Execute o script Python:

```
python download_imagens.py
```

O script baixará as imagens para uma pasta de destino (por padrão, "imagens") e registrará o progresso em um arquivo CSV chamado "registro.csv".

## Tratamento de Exceção

O script utiliza um loop `while` para tentar novamente as solicitações em caso de falha. Ele tentará até atingir o número máximo de tentativas especificado.

## Personalização

Você pode personalizar o número máximo de tentativas, a pasta de destino e o nome do arquivo de registro modificando as variáveis no código.

```python
max_attempts = 3  # Número máximo de tentativas
pasta_destino = 'imagens'  # Pasta de destino para as imagens
registro_arquivo = 'registro.csv'  # Nome do arquivo de registro
```
