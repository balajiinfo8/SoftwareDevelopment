import tkinter as tk
import keyboard
import winsound
import threading

class SoundApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Keyboard Sound Toggle")
        self.root.geometry("300x200")

        self.sound_enabled = False  # Initially disabled

        # Toggle Button
        self.toggle_button = tk.Button(root, text="Enable Sound", command=self.toggle_sound, font=("Arial", 12))
        self.toggle_button.pack(pady=20)

        # Label
        self.status_label = tk.Label(root, text="Sound: Disabled", font=("Arial", 12))
        self.status_label.pack(pady=20)

        # Start Keyboard Listener
        threading.Thread(target=self.listen_keys, daemon=True).start()

    def toggle_sound(self):
        self.sound_enabled = not self.sound_enabled
        self.toggle_button.config(text="Disable Sound" if self.sound_enabled else "Enable Sound")
        self.status_label.config(text=f"Sound: {'Enabled' if self.sound_enabled else 'Disabled'}")

    def play_sound(self):
        if self.sound_enabled:
            winsound.Beep(1000, 200)  # Beep sound for 200ms

    def listen_keys(self):
        while True:
            key = keyboard.read_event().name  # Detect keypress
            if self.sound_enabled and key.isalpha():  # Plays sound for letter keys
                self.play_sound()

# Run GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = SoundApp(root)
    root.mainloop()
