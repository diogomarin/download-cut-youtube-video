# YouTube Video Downloader and Cutter

Este projeto é uma aplicação Python para o download de vídeos do YouTube e corte de trechos específicos, utilizando as bibliotecas `pytube` e `moviepy`.

## Funcionalidades

- Download de vídeos completos do YouTube.
- Opção para cortar e salvar trechos específicos dos vídeos baixados.

## Como Usar

### Instalação

1. Clone este repositório:

    ```bash
    git clone https://github.com/diogomarin/download-cut-youtube-video.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd download-cut-youtube-video
    ```

3. Crie e ative o ambiente virtual:

    - Para criar um ambiente virtual:

    ```bash
    virtualenv venv
    ```

    - Para ativar no Windows:

    ```bash
    .\.venv\Scripts\activate
    ```

    - Para ativar no macOS/Linux:

    ```bash
    source .venv/bin/activate
    ```

4. Instale as dependências do projeto:

    ```bash
    pip install -r requirements.txt
    ```

### Uso

1. Execute o script principal:

    ```bash
    python app.py
    ```

2. Insira a URL do vídeo do YouTube que deseja baixar.

3. Escolha se deseja cortar o vídeo. Se sim, forneça o tempo inicial e final do trecho em segundos.

    Exemplo:
    
    - Digite a URL do vídeo do YouTube: `https://youtube.com/xyz`
    - Deseja cortar o vídeo? (s/n): `s`
    - Digite o tempo inicial do corte em segundos: `30`
    - Digite o tempo final do corte em segundos: `60`

### Solução para o Erro 400 no Pytube

Esta aplicação enfrentava o erro "HTTP Error 400: Bad Request" ao tentar baixar vídeos do YouTube. Esse erro foi causado por mudanças nas estruturas internas do YouTube, afetando o funcionamento da biblioteca `pytube`.

A solução, descrita no [comentário da issue #1973](https://github.com/pytube/pytube/issues/1973#issuecomment-2264722197), corrigiu o problema. O projeto já inclui essa correção, permitindo o download de vídeos sem o erro 400.

---