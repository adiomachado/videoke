import cv2

# Função para reproduzir o vídeo
def reproduzir_video(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Erro ao abrir o arquivo de vídeo")
        return

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Video', frame)

        # Pressione 'q' para sair
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Caminho do arquivo de vídeo
video_path = '\VIDEOKE\musicas\25362.mp4'
reproduzir_video(video_path)