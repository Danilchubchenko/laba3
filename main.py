import tkinter as tk
from tkinter import filedialog, messagebox
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
        
        # Создаем элементы интерфейса
        self.create_menu()
        self.create_controls()
    
    def create_menu(self):
        menu_bar = tk.Menu(self)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open File...", command=self.open_file)
        menu_bar.add_cascade(label="File", menu=file_menu)
        self.config(menu=menu_bar)
    
    def open_file(self):
        try:
            self.file_path = filedialog.askopenfilename(filetypes=[('Audio files', '*.mp3 *.wav')])
            if self.file_path:
                pygame.mixer.music.load(self.file_path)
                messagebox.showinfo("Success", f"Loaded {self.file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong: {e}")
    
    def play_pause(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
    
    def stop(self):
        pygame.mixer.music.stop()
    
    def next_track(self):
        pass  # Добавить логику переключения треков
    
    def previous_track(self):
        pass  # Добавить логику переключения треков
    
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
        
        next_button = tk.Button(control_frame, text="Next", command=self.next_track)
        next_button.grid(row=0, column=2, padx=10)
        
        prev_button = tk.Button(control_frame, text="Previous", command=self.previous_track)
        prev_button.grid(row=0, column=3, padx=10)
        
        volume_label = tk.Label(self, text="Volume:")
        volume_label.pack(pady=(30, 0))
        
        volume_scale = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL, length=300, command=self.set_volume)
        volume_scale.pack(pady=10)
        volume_scale.set(50)  # Установим начальную громкость 50%

if __name__ == "__main__":
    app = AudioPlayer()
    app.mainloop()