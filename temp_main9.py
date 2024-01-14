from ttkthemes import ThemedStyle
from tkinter import font


class EMGRecorderApp:
    def __init__(self, root, serial_port):
        self.root = root
        self.root.title("MyoAuth")
        self.root.geometry("700x500")  # Set window size
        self.root.iconbitmap(default='myoauthicon.ico')
        self.root.configure(bg='white')
