        if user_name not in self.emg_data:
            self.emg_data[user_name] = []  # Create an empty list for the user if not present

        self.emg_data.clear()
        self.emg_data[user_name] = []
        self.clear_window()

        self.data_thread = threading.Thread(target=self.record_emg, args=(user_name,))
        self.data_thread.start()

        step_label = tk.Label(self.root, text="", font=("Helvetica", 15,"bold"), background="white",foreground="green")
        step_label.place(relx=0.5, rely=0.1, anchor='center')