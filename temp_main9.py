        image_path = 'myoauthicon.png'  # Replace with your image path
        original_image = Image.open(image_path)
        resized_image = original_image.resize((200, 200), Image.LANCZOS)
        self.image = ImageTk.PhotoImage(resized_image)
        self.image_label = tk.Label(self.root, image=self.image,background="white")
        self.image_label.place(relx=0.5, rely=0.4, anchor='center')

        # Create a label for the title
        self.title_label = ttk.Label(self.root, text="MyoAuth", font=("Calibri", 25), foreground='green',background="white")
        self.title_label.place(relx=0.5, rely=0.65, anchor='center')

        # Play audio when the title is shown