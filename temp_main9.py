            current_volume -= step
            pygame.mixer.music.set_volume(max(0.1, current_volume))
            pygame.time.delay(int(step))

    def show_main_window(self):
        # Destroy the title label
        self.title_label.destroy()
        self.image_label.destroy()

        self.clear_window()

        # Create buttons for the main window