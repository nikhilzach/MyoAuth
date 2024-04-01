        self.instructions_label4.place(relx=0.5, rely=0.35, anchor='center')

        self.user_label = ttk.Label(self.root, text="Before we start, enter Username", font=("Helvetica", 11), background="white")
        self.user_label.place(relx=0.5, rely=0.45, anchor='center')

        self.user_entry = ttk.Entry(self.root, justify="center", font=("Helvetica", 12),width=30)
        self.user_entry.place(relx=0.5, rely=0.52, anchor='center')

        # Create "Start Recording" button
        self.next_button = ttk.Button(self.root, text="Start Recording", command=self.step_counter)
        self.next_button.place(relx=0.5, rely=0.6, anchor='center')
