        self.gif_label.place(relx=0.5, rely=0.4, anchor='center')

        # Load the animated GIF
        gif = imageio.mimread(gif_path)
        gif_images = [Image.fromarray(img) for img in gif]

        # Convert the PIL Images to Tkinter-compatible format
        self.gif_photos = [ImageTk.PhotoImage(img) for img in gif_images]

        # Display the animated GIF
        self.animate_gif(0, duration)
