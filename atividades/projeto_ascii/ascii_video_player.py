import cv2
import numpy as np
from PIL import Image
import os
import time

ASCII_CHARS = ["@", "#", "8", "&", "o", "=", "+", ";", ":", ",", ".", " ", "?", "%", "$", "S", "W", "B", "M", "H", "U"]

def pixel_to_ascii(gray_value):
    return ASCII_CHARS[min(int(gray_value / 10), len(ASCII_CHARS) - 1)]

def image_to_ascii(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / float(width)
    new_height = int(aspect_ratio * new_width * 0.5)
    image = image.resize((new_width, new_height))
    image = image.convert("L")
    pixels = np.array(image)
    ascii_str = ""
    for row in pixels:
        for pixel in row:
            ascii_str += pixel_to_ascii(pixel)
        ascii_str += "\n"
    return ascii_str

def play_video_as_ascii(video_path, width=100, speed_factor=0.01):
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(frame_rgb)
        ascii_frame = image_to_ascii(pil_image, new_width=width)
        os.system("cls" if os.name == "nt" else "clear")
        print(ascii_frame)
        time.sleep(speed_factor)
    cap.release()

if __name__ == "__main__":
    video_path = "video/calabreso.mp4"
    play_video_as_ascii(video_path, width=100, speed_factor=0.01)
