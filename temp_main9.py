        # Create instructions label
        self.instructions_label = ttk.Label(self.root, text="Follow these instructions", font=("Helvetica", 14,"bold"), background="white",foreground="green")
        self.instructions_label.place(relx=0.5, rely=0.1, anchor='center')
        

        self.instructions_label2 = ttk.Label(self.root, text="You will be guided through a series of five steps.", font=("Helvetica", 12), background="white")
        self.instructions_label2.place(relx=0.5, rely=0.2, anchor='center')

        self.instructions_label3 = ttk.Label(self.root, text="During each step, execute a hand gesture for a duration of 2 seconds.", font=("Helvetica", 12), background="white")
        self.instructions_label3.place(relx=0.5, rely=0.3, anchor='center')

        self.instructions_label4 = ttk.Label(self.root, text="It is necessary to maintain uniformity by consistently performing the same gesture at each step.", font=("Helvetica", 12), background="white")