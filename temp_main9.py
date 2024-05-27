        pygame.mixer.music.load('myoauthintro.mp3')  # Replace with your audio file path
        pygame.mixer.music.play(0,0,1)  # Start playing
        
        # Create "Next" button
        if(self.step<5):
            self.next_button = ttk.Button(self.root, text="Next Step", command=self.step_counter)
            self.next_button.place(relx=0.5, rely=0.6, anchor='center')
        else:
            self.next_button = ttk.Button(self.root, text="Finish", command=self.step_counter)
            self.next_button.place(relx=0.5, rely=0.6, anchor='center')

