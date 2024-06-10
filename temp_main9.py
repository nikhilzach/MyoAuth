
        with open(filename, 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)

            # Write header only if the file doesn't exist
            if not file_exists:
                csv_writer.writerow(["Username", "timestamps", "emgvalues"])

            for user_name, data in self.emg_data.items():
                print(user_name)
                for timestamp, emg_value in data:
                    csv_writer.writerow([user_name, timestamp, emg_value])