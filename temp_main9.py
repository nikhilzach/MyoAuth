
        print(f"EMG data saved to {filename}")

    def feature_extract_data(self):
        input_file = filedialog.askopenfilename(title="Select CSV file", filetypes=[("CSV files", "*.csv")])

        if not input_file:
            return

        output_file = filedialog.asksaveasfilename(title="Save Feature data as", defaultextension=".csv", filetypes=[("CSV files", "*.csv")])

        if not output_file: