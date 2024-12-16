import os
import tkinter as tk
from tkinter import messagebox
import pygame
from pygame.locals import *

class AudioPlayer(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Настройки окна
        self.title("Audio Player")
        self.geometry("400x200")  # Начальный размер окна
        self.resizable(True, True)
        
        # Инициализация pygame
        pygame.init()
        pygame.mixer.init()
        
        # Переменная для хранения пути к файлу
        self.file_path = None
        
        # Автоматически находим аудиофайл в текущей папке
        current_dir = os.path.dirname(os.path.abspath(__file__))
        audio_files = [f for f in os.listdir(current_dir) if f.endswith('.mp3') or f.endswith('.wav')]
        
        if len(audio_files) > 0:
            self.file_path = os.path.join(current_dir, audio_files[0])  # Берем первый найденный аудиофайл
            pygame.mixer.music.load(self.file_path)
            pygame.mixer.music.play()  # Начинаем автоматическое воспроизведение
            messagebox.showinfo("Success", f"Loaded {self.file_path}")
        else:
            messagebox.showwarning("Warning", "No audio files found in the same directory.")
        
        # Создаем элементы интерфейса
        self.create_controls()
    
    def play_pause(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
    
    def stop(self):
        pygame.mixer.music.stop()
    
    def set_volume(self, value):
        volume = float(value) / 100
        pygame.mixer.music.set_volume(volume)
    
    def create_controls(self):
        control_frame = tk.Frame(self)
        control_frame.pack(pady=20)
        
        play_button = tk.Button(control_frame, text="Play/Pause", command=self.play_pause)
        play_button.grid(row=0, column=0, padx=10)
        
        stop_button = tk.Button(control_frame, text="Stop", command=self.stop)
        stop_button.grid(row=0, column=1, padx=10)
        
        volume_label = tk.Label(self, text="Volume:")
        volume_label.pack(pady=(30, 0))
        
        volume_scale = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL, length=300, command=self.set_volume)
        volume_scale.pack(pady=10)
        volume_scale.set(20)  # Установим начальную громкость 20%

if __name__ == "__main__":
    app = AudioPlayer()
    app.mainloop()