            user_data = df[df['Username'] == user].sample(1)  # Select one random row for each user
            testing_data.append(user_data)

        testing_df = pd.concat(testing_data)
        training_df = df.drop(testing_df.index)

        # Extract features and labels from training and testing datasets
        X_train = np.vstack(training_df['Features'])
        y_train = training_df['Username']
        X_test = np.vstack(testing_df['Features'])
        y_test = testing_df['Username']
