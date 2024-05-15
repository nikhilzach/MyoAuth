    def animate_gif(self, index, duration):
        # Display the current frame of the animated GIF
        self.gif_label.config(image=self.gif_photos[index])

        # Schedule the next frame to be shown after a delay
        if index < len(self.gif_photos) - 1:
            self.root.after(int(duration * 1000 / len(self.gif_photos)), self.animate_gif, index + 1, duration)
        elif self.initial_option=="register":
            # Schedule the static image to be shown after the animated GIF
            self.root.after(int(duration * 160), self.show_static_image, 'tick2.png')
        else:
            pass