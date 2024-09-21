from flask import Flask, render_template, request
import joblib
import numpy as np
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Load your trained model
model = joblib.load('ids_model.pkl')

def send_email(subject, body):
    sender_email = "ay5169680@gmail.com"
    receiver_email = "ak47ankii@gmail.com"
    password = "bqck vdpq mnjr vojg"  # Replace with your actual email password

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # Replace 'smtp.example.com' with your actual email provider's SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(request.form[f'feature{i}']) for i in range(1, 119)]
        final_features = [np.array(features)]
        prediction = model.predict(final_features)
        output = prediction[0]

        chart_data = features  # Pass feature data to chart

        if output == 1:
            prediction_text = 'Intrusion Prediction: Malicious'
            send_email(
                subject="Alert: Malicious Activity Detected",
                body=f"A malicious activity has been detected with features: {features}"
            )
        else:
            prediction_text = 'Intrusion Prediction: Normal'

    except Exception as e:
        prediction_text = f"An error occurred: {str(e)}"
        chart_data = []  # Empty data for the chart in case of error

    return render_template('index.html', prediction_text=prediction_text, chart_data=chart_data)

@app.route('/feedback', methods=['POST'])
def feedback():
    feedback_text = request.form['feedback']
    
    # Send feedback via email
    send_email(
        subject="New Feedback Received",
        body=f"Feedback received: {feedback_text}"
    )
    
    return render_template('index.html', feedback_text="Thank you for your feedback!")

if __name__ == "__main__":
    app.run(debug=True)
