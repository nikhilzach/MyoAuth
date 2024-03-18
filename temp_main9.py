        # This function will be called when the "Next" button is clicked
        self.step = self.step + 1
        if(self.step<=5):
            self.start_recording()
        else:
            self.show_register_window()

    def start_recording_instructions(self):
        
        self.clear_window()
        self.step=0
