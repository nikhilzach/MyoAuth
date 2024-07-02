            return

        print("Loading feature vectors...")
        df = pd.read_csv(input_file)
        df['Features'] = df['Features'].apply(lambda x: eval(x))  # Convert string to list

        # Assuming 'Username' is the column containing user names
        unique_users = df['Username'].unique()

        # Create testing dataset with one feature vector per user
        testing_data = []
        for user in unique_users: