import pygame  # type: ignore # Importa a biblioteca pygame
import time    # Para aguardar o áudio terminar

# Inicializa o mixer do pygame
pygame.mixer.init()

# Carrega o arquivo MP3
arquivo_mp3 = "caminho/do/seu/arquivo.mp3"  # Substitua pelo caminho do arquivo
pygame.mixer.music.load(arquivo_mp3)

# Reproduz o arquivo de áudio
pygame.mixer.music.play()

# Aguarda enquanto o áudio está tocando
print("Reproduzindo áudio...")
while pygame.mixer.music.get_busy():  # Verifica se o áudio ainda está tocando
    time.sleep(1)

print("Reprodução finalizada.")
