import cv2
import numpy as np
from PIL import Image

# Define o conjunto de caracteres que representam os diferentes níveis de brilho
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# Função para converter a imagem em escala de cinza para ASCII
def pixel_to_ascii(gray_value):
    return ASCII_CHARS[int(gray_value / 25)]  # Mapeia a intensidade de brilho para o caractere correspondente

# Função para converter uma imagem em ASCII
def image_to_ascii(image, new_width=100):
    # Obtenha as dimensões da imagem
    width, height = image.size
    aspect_ratio = height / float(width)
    new_height = int(aspect_ratio * new_width)

    # Redimensiona a imagem
    image = image.resize((new_width, new_height))
    image = image.convert("L")  # Converte para escala de cinza

    pixels = np.array(image)
    ascii_str = ""

    for row in pixels:
        for pixel in row:
            ascii_str += pixel_to_ascii(pixel)
        ascii_str += "\n"

    return ascii_str

# Função para exibir o vídeo como ASCII no terminal
def play_video_as_ascii(video_path, width=100):
    # Abre o vídeo
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Converte o quadro para uma imagem PIL
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(frame_rgb)

        # Converte o quadro para ASCII
        ascii_frame = image_to_ascii(pil_image, new_width=width)

        # Limpa a tela (isso pode ser diferente dependendo do terminal)
        print("\033c", end="")  # Em alguns terminais, isso limpa a tela
        print(ascii_frame)

    cap.release()

if __name__ == "__main__":
    video_path = "seu_video.mp4"  # Caminho do seu arquivo de vídeo
    play_video_as_ascii(video_path)
