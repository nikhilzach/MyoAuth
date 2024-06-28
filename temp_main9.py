        features.append(np.sum(np.diff(np.sign(emg_values),axis=0)!=0,axis=0)/(len(emg_values)-1))
        features.append(skew(emg_values,axis=0))
        features.append(kurtosis(emg_values,axis=0))
        features.append(np.sqrt(np.mean(np.array(emg_values)**2,axis=0))) #root mean sqaure
        features.append(np.sum(np.array(emg_values)**2,axis=0)) #simple square integral
        return features
    
    def train_classifier(self):
        # Load feature vectors from the CSV file
        input_file = filedialog.askopenfilename(title="Select Feature Vectors CSV file", filetypes=[("CSV files", "*.csv")])

        if not input_file: