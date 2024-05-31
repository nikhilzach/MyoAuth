    def record_emg(self, user_name):
        print(user_name)
        with serial.Serial(self.serial_port, 115200, timeout=1) as ser:
            ser.reset_input_buffer()

            start_time = time.time()
            while time.time() - start_time < 2:
                try:
                    line = ser.readline().decode().strip()
                    if line:
                        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
                        emg_value = float(line)