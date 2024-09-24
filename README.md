# YouTube Video Downloader and Cutter

Este projeto é uma aplicação Python para download de vídeos do YouTube e corte de trechos específicos. Ele utiliza as bibliotecas `pytube` e `moviepy` para realizar o download e manipulação de vídeos.

## Funcionalidades

- Download de vídeos completos do YouTube.
- Opção para cortar e salvar um trecho específico do vídeo baixado.

## Como Usar

### Instalação

1. Clone este repositório:

    git clone https://github.com/diogomarin/download-cut-youtube-video.git

2. Navegue até o diretório do projeto

3. Crie e ative o ambiente virtual:

    virtualenv venv (comando para criar um ambiente)

    .\.venv\Scripts\activate (comando para ativar no windows)

    source .venv/bin/activate (comando para ativar no macOS/Linux)

4. Instale as dependências do projeto:

    pip install -r requirements.txt


### Uso

1. Execute o script principal

    python app.py

2. Insira a URL do vídeo do YouTube que deseja baixar.

3. Escolha se deseja realizar o corte do vídeo e, se sim, insira o tempo inicial e final em segundos.

    Por exemplo:
    Digite a URL do vídeo do YouTube: "Passo 2"
    Você deseja cortar o vídeo? (s/n): s
    Digite o tempo inicial do corte em segundos: 30
    Digite o tempo final do corte em segundos: 60


### Solução de Erro 400 no Pytube

Essa aplicação enfrentava o problema de "HTTP Error 400: Bad Request" ao tentar baixar vídeos do YouTube. Esse erro foi causado por mudanças nas estruturas internas do YouTube, que afetaram a forma como a biblioteca pytube processava as solicitações de download.

A solução descrita no `comentário da issue #1973` (https://github.com/pytube/pytube/issues/1973#issuecomment-2264722197) no GitHub corrigiu o problema. A correção foi aplicada ao projeto e está funcionando corretamente com o commit atual, permitindo o download de vídeos sem o erro 400.