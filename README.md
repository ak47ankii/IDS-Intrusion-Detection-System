# IDS-Intrusion-Detection-System
# Intrusion Detection System (IDS) Dashboard

This project is an Intrusion Detection System (IDS) that uses a machine learning model to predict whether network activity is malicious or normal. It includes a web-based dashboard developed using Flask, where users can input feature values for network traffic and view predictions. The system sends an email alert if malicious activity is detected. Additionally, feature data is visualized using graphs.

## Features

- **Machine Learning Model**: A trained model that predicts malicious activity based on network features.
- **Flask Web App**: A user-friendly interface for inputting network features and receiving predictions.
- **Email Alerts**: Sends an email notification if the model predicts malicious activity.
- **Feature Visualization**: Displays feature values as bar or line charts.
- **Real-time Alerts**: Alerts the user if malicious activity is detected based on feature input.

## Requirements

### Python Packages

- Flask
- Joblib
- Numpy
- Smtplib
- Matplotlib
- io
- base64

### Installation

To run this project locally, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone 
    cd your-repo-name
    ```

2. **Install dependencies**:

    Make sure you have Python installed. You can install the necessary dependencies by running:

    ```bash
    pip install flask joblib numpy matplotlib
    ```

3. **Prepare your trained model**:

    - Place your pre-trained model file (`ids_model.pkl`) in the root directory of the project.

4. **Email Setup**:

    Update the `send_email` function in `app.py` with your email credentials. You'll need to:
    - Replace `sender_email`, `receiver_email`, and `password` with your own values.
    - Ensure your email account allows access to third-party apps. For Gmail, you may need to enable "Less Secure Apps" or generate an App Password.

5. **Run the Flask app**:

    In the project directory, run the Flask application:

    ```bash
    python app.py
    ```

6. **Access the Web App**:

    Open your web browser and go to:

    ```
    http://127.0.0.1:5000
    ```

    You'll see the IDS dashboard where you can input network feature values.

## Usage

1. Enter the values for the 118 features in the form.
2. Click on the "Predict" button to get the prediction result.
3. If the prediction is "Malicious", an email alert will be sent to the specified email address.
4. View the graph of feature values below the prediction result.



### Dashboard

![IDS Dashboard](screenshots/dashboard.png)


## Files

- `app.py`: The main Flask application file containing the routes, model loading, and email notification logic.
- `index.html`: The HTML template for the dashboard, including the form and feature visualization.
- `ids_model.pkl`: The trained machine learning model (this needs to be added manually).
- `README.md`: Documentation for the project.



made with love by Ankit
