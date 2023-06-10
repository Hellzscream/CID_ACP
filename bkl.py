import tkinter as tk
from PIL import Image, ImageTk
import pygame

def play_audio():
    pygame.mixer.init()
    sound = pygame.mixer.Sound('data/lib/pkg/renamed.mp3')
    sound.play()

    audio_length = sound.get_length() * 1000  # Convert to milliseconds
    root.after(int(audio_length), root.destroy)  # Schedule program to close after audio length

def open_popup():
    popup = tk.Toplevel()
    popup.title("Popup Dialog")
    popup.geometry("400x400")
    popup.wm_attributes('-topmost', 1)  # Bring the window to the top

    image_path = 'data/lib/pkg/ACP.png'  # Path to your image file
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(popup, image=photo)
    label.image = photo  # Keep a reference to the image object
    label.pack(pady=20)

root = tk.Tk()

# Open the popup and play the sound automatically when the program starts
open_popup()
play_audio()

root.mainloop()