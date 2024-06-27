# LoM/MushroomGUI.py
import tkinter as tk
from tkinter import scrolledtext
from LoM.MushroomBot import start_bot_handler, stop_bot_handler
from loguru import logger
from LoM.MushroomMessages import LEGENDS_CLOSED, LEGENDS_TERMINATED

class MushroomGUI:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f0f0")
        self.root.resizable(False, False)
        self.center_window()
        self.root.overrideredirect(True)

        self.font = ("Helvetica", 10)

        self.title_bar = tk.Frame(self.root, bg="#e0e0e0", relief='raised', bd=0)
        self.title_bar.pack(expand=0, fill=tk.X)

        self.title_label = tk.Label(self.title_bar, text="🍄 Legends of Mushroom", bg="#e0e0e0", fg="#333333", font=("Helvetica", 12))
        self.title_label.pack(side=tk.LEFT, padx=5)

        self.close_button = tk.Button(self.title_bar, text="X", command=self.close_app, bg="#e0e0e0", fg="#333333", bd=0, padx=5, pady=2, font=self.font)
        self.close_button.pack(side=tk.RIGHT)

        self.title_bar.bind("<B1-Motion>", self.move_app)
        self.title_bar.bind("<Button-1>", self.get_pos)

        self.buttons_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.buttons_frame.pack(pady=10)

        self.start_button = tk.Button(self.buttons_frame, text="Start Bot", command=start_bot_handler, bg="#008CBA", fg="white", font=self.font, bd=0, padx=20, pady=10)
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = tk.Button(self.buttons_frame, text="Stop Bot", command=stop_bot_handler, bg="#008CBA", fg="white", font=self.font, bd=0, padx=20, pady=10)
        self.stop_button.pack(side=tk.LEFT, padx=5)

        self.start_button.bind("<Enter>", lambda e: self.on_enter(e, self.start_button))
        self.start_button.bind("<Leave>", lambda e: self.on_leave(e, self.start_button))
        self.stop_button.bind("<Enter>", lambda e: self.on_enter(e, self.stop_button))
        self.stop_button.bind("<Leave>", lambda e: self.on_leave(e, self.stop_button))

        self.log_box = scrolledtext.ScrolledText(self.root, width=60, height=15, state='disabled', bg="#ffffff", fg="#333333", font=self.font, bd=0, padx=10, pady=10, relief="flat")
        self.log_box.pack(pady=10, padx=10)

        logger.remove()
        logger.add(self.log, level="INFO", format="{time} | {level} | {message}")
        logger.add(lambda msg: print(msg, end=""), level="DEBUG", format="{time} | {level} | {message}")

    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def get_pos(self, event):
        self.xwin = event.x
        self.ywin = event.y

    def move_app(self, event):
        x = event.x_root - self.xwin
        y = event.y_root - self.ywin
        self.root.geometry(f'+{x}+{y}')

    def log(self, message):
        self.log_box.config(state='normal')
        self.log_box.insert(tk.END, message + '\n')
        self.log_box.config(state='disabled')
        self.log_box.yview(tk.END)

    def close_app(self):
        logger.info(LEGENDS_CLOSED)
        self.root.destroy()

    def on_enter(self, event, button):
        button['background'] = '#005f73'

    def on_leave(self, event, button):
        button['background'] = '#008CBA'

def launch_app():
    root = tk.Tk()
    app = MushroomGUI(root)
    try:
        root.mainloop()
    except KeyboardInterrupt:
        logger.info(LEGENDS_TERMINATED)