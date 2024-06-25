            feature_vectors.append({'Username': user_name, 'Features': features})

        feature_df = pd.DataFrame(feature_vectors)
        feature_df.to_csv(output_file, index=False)

        print(f"\nFeature vectors saved to {output_file}")

    def calculate_features(self, emg_values):
        # feature extraction
        features = []
        features.append(np.mean(np.abs(emg_values),axis=0)) #mean absolute value
        features.append(np.sum(np.abs(np.diff(emg_values)),axis=0)) #waveform length