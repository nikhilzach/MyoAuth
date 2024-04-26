        step_label.config(text=f"Step {self.step} / 5")

        countdown_label = tk.Label(self.root, text="", font=("Helvetica", 12), background="white")
        countdown_label.place(relx=0.5, rely=0.2, anchor='center')

        # Start the countdown in a separate thread
        countdown_thread = threading.Thread(target=self.start_countdown, args=(2, countdown_label))
        countdown_thread.start()
    
    def start_countdown(self, seconds, countdown_label):

        gif_path = 'wave2.gif'  # Replace with your GIF path