
    def show_static_image(self, image_path):
        static_image = Image.open(image_path)
        resized_image = static_image.resize((100, 100), Image.LANCZOS)
        static_photo = ImageTk.PhotoImage(resized_image)

        # Replace the GIF label with a static image label
        self.gif_label.config(image=static_photo)
        self.gif_label.image = static_photo

        # Play audio
        pygame.init()