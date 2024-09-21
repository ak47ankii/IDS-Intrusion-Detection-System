import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
import joblib
import argparse
import logging

# Load the dataset
def load_data():
    column_names = ["duration","protocol_type","service","flag","src_bytes","dst_bytes","land","wrong_fragment","urgent",
                    "hot","num_failed_logins","logged_in","num_compromised","root_shell","su_attempted","num_root",
                    "num_file_creations","num_shells","num_access_files","num_outbound_cmds","is_host_login","is_guest_login",
                    "count","srv_count","serror_rate","srv_serror_rate","rerror_rate","srv_rerror_rate","same_srv_rate",
                    "diff_srv_rate","srv_diff_host_rate","dst_host_count","dst_host_srv_count","dst_host_same_srv_rate",
                    "dst_host_diff_srv_rate","dst_host_same_src_port_rate","dst_host_srv_diff_host_rate","dst_host_serror_rate",
                    "dst_host_srv_serror_rate","dst_host_rerror_rate","dst_host_srv_rerror_rate","label"]
    data = pd.read_csv('kddcup.data_10_percent.gz', names=column_names, header=None)
    return data

# Preprocess the dataset
def preprocess_data(data):
    data['label'] = data['label'].apply(lambda x: 0 if x == 'normal.' else 1)
    X = data.drop('label', axis=1)
    y = data['label']
    X = pd.get_dummies(X, columns=["protocol_type", "service", "flag"])
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    return X, y

# Train the model
def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print(classification_report(y_test, predictions))
    return model

# Save the model
def save_model(model, filename):
    joblib.dump(model, filename)

# Load the model
def load_model(filename):
    return joblib.load(filename)

# Predict using the model
def predict(model, features):
    return model.predict([features])

# Setup logging
logging.basicConfig(filename='intrusions.log', level=logging.INFO)

# Log intrusions
def log_intrusion(prediction, features):
    if prediction == 1:  # Assuming 1 indicates an intrusion
        logging.info(f'Intrusion detected: {features}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Intrusion Detection System CLI')
    parser.add_argument('model_path', type=str, help='Path to the trained model')
    parser.add_argument('features', type=float, nargs='+', help='Features for prediction')
    args = parser.parse_args()
    
    model = load_model(args.model_path)
    prediction = predict(model, args.features)
    print(f'Prediction: {prediction[0]}')
    log_intrusion(prediction, args.features)
