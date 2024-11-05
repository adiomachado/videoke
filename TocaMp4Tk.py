import tkinter as tk
from tkVideoPlayer import TkinterVideo

# Função para reproduzir o vídeo
def reproduzir_video(video_path):
    root = tk.Tk()
    root.title("Reprodutor de Vídeo")

    videoplayer = TkinterVideo(master=root, scaled=True)
    videoplayer.load(video_path)
    videoplayer.pack(expand=True, fill="both")
    videoplayer.play()

    
    root.mainloop()

# Caminho do arquivo de vídeo
video_path = '\VIDEOKE\musicas\25362.mp4'
reproduzir_video(video_path)