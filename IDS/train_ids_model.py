from ids import load_data, preprocess_data, train_model, save_model

# Load the dataset
data = load_data()

# Preprocess the data
X, y = preprocess_data(data)

# Train the model
model = train_model(X, y)

# Save the trained model to a file
save_model(model, 'ids_model.pkl')
