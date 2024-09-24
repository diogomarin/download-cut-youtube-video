from pytube.innertube import _default_clients
from pytube import cipher
import re
from pytube import YouTube
from moviepy.editor import VideoFileClip
import os

# Ajuste das versões dos clientes do YouTube
_default_clients["ANDROID"]["context"]["client"]["clientVersion"] = "19.08.35"
_default_clients["IOS"]["context"]["client"]["clientVersion"] = "19.08.35"
_default_clients["ANDROID_EMBED"]["context"]["client"]["clientVersion"] = "19.08.35"
_default_clients["IOS_EMBED"]["context"]["client"]["clientVersion"] = "19.08.35"
_default_clients["IOS_MUSIC"]["context"]["client"]["clientVersion"] = "6.41"
_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]

# Substituição da função que obtém o nome da função de throttling
def get_throttling_function_name(js: str) -> str:
    """Extract the name of the function that computes the throttling parameter.

    :param str js:
        The contents of the base.js asset file.
    :rtype: str
    :returns:
        The name of the function used to compute the throttling parameter.
    """
    function_patterns = [
        r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&\s*'
        r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])?\([a-z]\)',
        r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])\([a-z]\)',
    ]
    for pattern in function_patterns:
        regex = re.compile(pattern)
        function_match = regex.search(js)
        if function_match:
            if len(function_match.groups()) == 1:
                return function_match.group(1)
            idx = function_match.group(2)
            if idx:
                idx = idx.strip("[]")
                array = re.search(
                    r'var {nfunc}\s*=\s*(\[.+?\]);'.format(
                        nfunc=re.escape(function_match.group(1))),
                    js
                )
                if array:
                    array = array.group(1).strip("[]").split(",")
                    array = [x.strip() for x in array]
                    return array[int(idx)]

    raise ValueError("Throttling function name not found in the JavaScript.")

cipher.get_throttling_function_name = get_throttling_function_name


# Função de download e corte de vídeo
def download_video():
    try:
        # Solicitando a URL do vídeo do YouTube
        url = input("Digite a URL do vídeo do YouTube: ").split('&')[0]  # Remove parâmetros extras da URL

        # Solicitando se o usuário deseja cortar o vídeo ou não
        cut = input("Você deseja cortar o vídeo? (s/n): ").lower() == 's'
        
        # Definindo o tempo de início e fim do corte, se necessário
        t_start, t_end = None, None
        if cut:
            t_start = int(input("Digite o tempo inicial do corte em segundos: "))
            t_end = int(input("Digite o tempo final do corte em segundos: "))

        print("Downloading video ...")
        yt = YouTube(url)

        # Seleciona o primeiro stream MP4 com resolução progressiva
        video_stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()

        # Definindo o caminho para salvar o vídeo
        output_path = "downloaded-videos"
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        video_file_path = video_stream.download(output_path)
        print(f"Download concluído! Vídeo salvo em: {video_file_path}")

        if cut:
            cut_output_path = "cut-videos"
            if not os.path.exists(cut_output_path):
                os.makedirs(cut_output_path)

            # Corrigindo o problema de escape de caminho
            clip = VideoFileClip(video_file_path).subclip(t_start, t_end)
            cut_file_path = os.path.join(cut_output_path, video_stream.default_filename)

            clip.write_videofile(cut_file_path)
            print(f"Download and cut concluído! Vídeo cortado salvo em: {cut_file_path}")

    except Exception as e:
        print("Ocorreu um erro durante o download:", e)


# Executar a função
download_video()
