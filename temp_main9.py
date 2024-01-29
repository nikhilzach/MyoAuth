        pygame.init()
        pygame.mixer.music.load('myoauthintro.mp3')  # Replace with your audio file path
        pygame.mixer.music.play(0)  # Start playing
        self.fade_out_audio(1000, 0.1)  # Fade in over 3000 milliseconds (3 seconds) with a step of 0.5

        # Schedule the transition to the main window after 5000 milliseconds (5 seconds)
        self.root.after(2500, self.show_main_window)

    def fade_out_audio(self, duration, step):
        current_volume = 2.0
        # Gradually decrease the volume to simulate a fade-out effect
        for i in range(int(duration / step)):