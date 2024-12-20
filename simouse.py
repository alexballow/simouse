import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import threading
import pyautogui
import time
import os
import sys

# Variable pour gérer l'état de la simulation
is_running = False

def resource_path(relative_path):
    """Obtenir le chemin absolu pour le fichier dans un exécutable PyInstaller."""
    if hasattr(sys, '_MEIPASS'):
        # Lorsque l'exécutable est créé, PyInstaller extrait les fichiers dans _MEIPASS
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Fonction pour simuler l'activité utilisateur
def simulate_activity(x_start, y_start, x_end, y_end, speed):
    global is_running
    x, y = x_start, y_start
    direction = 1  # Sens du mouvement

    while is_running:
        # Déplacer la souris
        pyautogui.moveTo(x, y, duration=speed)
        x += 10 * direction
        y += 10 * direction

        # Revenir au point de départ si les limites sont atteintes
        if x >= x_end or y >= y_end:
            direction = -1
        if x <= x_start or y <= y_start:
            direction = 1

        # Simuler un clic de souris
        pyautogui.click()

        # Simuler une frappe clavier (touche Shift)
        pyautogui.press("shift")

        time.sleep(5)  # Pause entre les cycles

# Fonction pour démarrer la simulation
def start_simulation():
    global is_running

    # Récupérer les valeurs saisies et valider
    try:
        x_start = int(entry_x_start.get())
        y_start = int(entry_y_start.get())
        x_end = int(entry_x_end.get())
        y_end = int(entry_y_end.get())
        speed = float(entry_speed.get())

        if not is_running:
            is_running = True
            threading.Thread(
                target=simulate_activity,
                args=(x_start, y_start, x_end, y_end, speed),
                daemon=True,
            ).start()
            messagebox.showinfo("Info", "Simulation démarrée !")
    except ValueError:
        messagebox.showerror(
            "Erreur", "Veuillez entrer des valeurs valides pour les coordonnées et la vitesse."
        )

# Fonction pour arrêter la simulation
def stop_simulation():
    global is_running
    is_running = False
    messagebox.showinfo("Info", "Simulation arrêtée !")

# Fonction pour arrêter avec la touche Échap
def stop_with_escape(event):
    stop_simulation()

# Réinitialiser les champs
def reset_fields():
    entry_x_start.delete(0, tk.END)
    entry_y_start.delete(0, tk.END)
    entry_x_end.delete(0, tk.END)
    entry_y_end.delete(0, tk.END)
    entry_speed.delete(0, tk.END)

    entry_x_start.insert(0, "100")
    entry_y_start.insert(0, "100")
    entry_x_end.insert(0, "400")
    entry_y_end.insert(0, "400")
    entry_speed.insert(0, "0.5")

# Interface graphique avec Tkinter
def create_gui():
    window = tk.Tk()
    window.title("SiMouse")
    window.geometry("350x220")
    window.resizable(False, False)

    # Ajouter une icône dans la barre de titre
    icon_path = resource_path("simouse.ico")
    window.iconbitmap(icon_path)

    # Associer la touche Échap pour arrêter la simulation
    window.bind("<Escape>", stop_with_escape)

    # Style moderne avec ttk
    style = ttk.Style()
    style.configure("TButton", font=("Arial", 10), padding=6)
    style.map("TButton",
              foreground=[("active", "#ffffff")],
              background=[("active", "#5c85d6")])

    # Titre
    label_title = tk.Label(window, text="SiMouse", font=("Arial", 14, "bold"))
    label_title.pack(pady=10)

    # Entrée pour les coordonnées de départ
    frame_start = tk.Frame(window)
    frame_start.pack(pady=5)
    tk.Label(frame_start, text="Coordonnées de départ (X, Y) :", font=("Arial", 10)).grid(row=0, column=0, padx=5)
    global entry_x_start, entry_y_start
    entry_x_start = ttk.Entry(frame_start, width=8)
    entry_y_start = ttk.Entry(frame_start, width=8)
    entry_x_start.grid(row=0, column=1, padx=5)
    entry_y_start.grid(row=0, column=2, padx=5)

    # Entrée pour les coordonnées de fin
    frame_end = tk.Frame(window)
    frame_end.pack(pady=5)
    tk.Label(frame_end, text="Coordonnées de fin (X, Y) :", font=("Arial", 10)).grid(row=0, column=0, padx=5)
    global entry_x_end, entry_y_end
    entry_x_end = ttk.Entry(frame_end, width=8)
    entry_y_end = ttk.Entry(frame_end, width=8)
    entry_x_end.grid(row=0, column=1, padx=5)
    entry_y_end.grid(row=0, column=2, padx=5)

    # Entrée pour la vitesse
    frame_speed = tk.Frame(window)
    frame_speed.pack(pady=5)
    tk.Label(frame_speed, text="Vitesse (en secondes) :", font=("Arial", 10)).grid(row=0, column=0, padx=5)
    global entry_speed
    entry_speed = ttk.Entry(frame_speed, width=8)
    entry_speed.grid(row=0, column=1, padx=5)

    # Boutons Start, Stop, et Reset
    frame_buttons = tk.Frame(window)
    frame_buttons.pack(pady=20)
    start_button = ttk.Button(frame_buttons, text="Start", command=start_simulation)
    start_button.grid(row=0, column=0, padx=10)
    stop_button = ttk.Button(frame_buttons, text="Stop", command=stop_simulation)
    stop_button.grid(row=0, column=1, padx=10)
    reset_button = ttk.Button(frame_buttons, text="Reset", command=reset_fields)
    reset_button.grid(row=0, column=2, padx=10)

    # Initialiser les champs avec des valeurs par défaut
    reset_fields()

    window.mainloop()

if __name__ == "__main__":
    create_gui()
