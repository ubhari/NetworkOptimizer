from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
from datetime import datetime

app = Flask(__name__)

# Load the trained CatBoost model
catboost_model = joblib.load('trained_catboost_model.joblib')

# Serve the HTML page containing the form
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# API endpoint to accept custom inputs and return predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get custom input data from the request
    data = request.form.to_dict()

    # print(data)

    # Set default values for non-existing checkbox keys
    checkbox_keys = ['Application_Type_Video_Call',
                     'Application_Type_Web_Browsing',
                     'Application_Type_Background_Download',
                     'Application_Type_Emergency_Service',
                     'Application_Type_File_Download',
                     'Application_Type_IoT_Temperature',
                     'Application_Type_Online_Gaming',
                     'Application_Type_Streaming',
                     'Application_Type_Video_Streaming',
                     'Application_Type_VoIP_Call',
                     'Application_Type_Voice_Call',
                     ]  # Add other checkbox keys as needed
    for key in checkbox_keys:
        if key in data:
            data[key] = 1
        if key not in data:
            data[key] = 0

    # Convert non-checkbox items to appropriate types
    for key in ['Signal_Strength', 'Latency', 'Bandwidth_Utilization_Ratio']:
        if key in data:
            data[key] = float(data[key])

    # Add Timestamp with current time
    # data['Timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Convert data to DataFrame
    input_data = pd.DataFrame([data])

    # print(input_data.columns)

    # print(input_data)

    # Make predictions using the loaded model
    prediction = catboost_model.predict(input_data)

    # Return the prediction as the API response
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=False)
