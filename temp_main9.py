
        self.preprocess_button = ttk.Button(self.root, text="Extract Features", command=self.feature_extract_data)
        self.preprocess_button.place(relx=0.5, rely=0.4, anchor='center', width=200, height=40)

        self.train_button = ttk.Button(self.root, text="Train", command=self.train_classifier)
        self.train_button.place(relx=0.5, rely=0.5, anchor='center', width=150, height=35)

        self.back_button = ttk.Button(self.root, text="Back", command=self.show_main_window)
        self.back_button.place(relx=0.5, rely=0.6, anchor='center', width=150, height=35)

    def step_counter(self):
        # Add your logic for the step counter here