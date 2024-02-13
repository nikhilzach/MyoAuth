        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat", background="#ccc")

        welcome_label = tk.Label(self.root, text="Welcome to MyoAuth", background="white", font=("Helvetica", 15, "bold"), fg="green")
        welcome_label.place(relx=0.5, rely=0.1, anchor='center')

        existing_user_label = tk.Label(self.root, text="Existing User?",background="white", font=("Helvetica", 10))
        existing_user_label.place(relx=0.5, rely=0.3, anchor='center')

        # Create "Login" and "Register" buttons
        self.login_button = ttk.Button(self.root, text="Login", command=self.show_login_window)
        self.login_button.place(relx=0.5, rely=0.37, anchor='center', width=150, height=40)