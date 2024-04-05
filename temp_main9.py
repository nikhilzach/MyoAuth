        self.back_button = ttk.Button(self.root, text="Back", command=self.show_register_window)
        self.back_button.place(relx=0.5, rely=0.7, anchor='center')

    def clear_window(self):
        # Destroy all widgets in the window
        for widget in self.root.winfo_children():
            widget.destroy()

    def start_recording(self):
        if(self.step==1):
            user_name = self.user_entry.get()
            self.user_name = user_name