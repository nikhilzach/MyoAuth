        print(X_train)
        print(y_train)

        # Standardize the feature values
        print("Standardizing feature values...")
        self.scaler = StandardScaler()
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)

        # Create and train the KNN classifier
        print("Training KNN classifier...")
        self.knn_classifier = KNeighborsClassifier(n_neighbors=1, metric='manhattan')