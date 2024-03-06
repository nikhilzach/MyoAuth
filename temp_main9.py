        self.clear_window()

        self.initial_option = "register"

        register_label = tk.Label(self.root, text="New User Registration", background="white", font=("Helvetica", 15, "bold"), fg="green")
        register_label.place(relx=0.5, rely=0.1, anchor='center')
        
        self.step = 0
        
        # Create "Record EMG Signals," "Extract Features," and "Train" buttons
        self.record_button = ttk.Button(self.root, text="Record EMG Signals", command=self.start_recording_instructions)
        self.record_button.place(relx=0.5, rely=0.3, anchor='center', width=200, height=40)