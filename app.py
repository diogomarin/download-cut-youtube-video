from pytube import YouTube
from moviepy.editor import VideoFileClip


def download_video(url, output_path=None, cut=False, t_start=None, t_end=None):
    try:
        print("Downloading video ...")
        yt = YouTube(url)

        video_stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()

        output_path = "downloaded-videos"

        if cut is False:

            video_stream.download(output_path)
            print("Download concluído!")
            
        else:
            video_stream.download(output_path)
            
            clip = VideoFileClip(f'{output_path}\{video_stream.default_filename}').subclip(t_start, t_end)

            clip.write_videofile(f'cut-videos\{video_stream.default_filename}')
            
            print("Download and cut concluído!")


    except Exception as e:
        print("Ocorreu um erro durante o download", e)
        





if __name__ == "__main__":

    goal = int(input("Funções: \nDigite 1 para apenas realizar o download completo do video \nDigite 2 para relizar o corte do video, além do download completo do video: \n"))

    if goal == 1 or goal == 2:

        if goal == 1:
            video_url = input("Digite a URL do vídeo do YouTube: ")

            download_video(video_url)

        elif goal == 2:
            video_url = input("Digite a URL do vídeo do YouTube: ")
            t_start = int(input("Digite o tempo incial do corte, em segundos: "))
            t_end = int(input("Digite o tempo final do corte, em segundos: "))
            
            download_video(video_url, cut=True, t_start=t_start, t_end=t_end)

    else:
        print("Revise sua escolha, por favor reinicie o aplicativo!")




