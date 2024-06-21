            return

        self.extract_features(input_file, output_file)

    def extract_features(self, input_file, output_file):
        df = pd.read_csv(input_file)

        feature_vectors = []
        for user_name, user_data in df.groupby('Username'):
            emg_values = user_data['emgvalues'].tolist()
            features = self.calculate_features(emg_values)
            user_name = ''.join(char for char in user_name if not char.isdigit())