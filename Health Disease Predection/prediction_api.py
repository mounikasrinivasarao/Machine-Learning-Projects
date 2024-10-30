from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the preprocessed data and model
with open('preprocessed_data.pkl', 'rb') as f:
    X_train, X_test, y_train, y_test = pickle.load(f)
with open('knn_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define feature names
feature_names = X_train.columns

@app.route('/')
def index():
    return render_template('index.html', feature_names=feature_names)

@app.route('/predict', methods=['POST'])
def predict():
    # Get user input from the form
    user_input = request.form

    # Preprocess user input (ensure same preprocessing as training data)
    user_input_list = [float(user_input[feature]) for feature in feature_names]
    user_input_array = np.array([user_input_list])  # Reshape into a 2D array

    # Make prediction using the model
    prediction = model.predict(user_input_array)
    predicted_class = prediction[0]  # Get the predicted class (0 or 1)

    # Map predicted class to heart disease prediction
    prediction_text = 'Heart Disease Present' if predicted_class == 1 else 'Heart Disease Not Present'

    return render_template('result.html', prediction=prediction_text)

if __name__ == '__main__':
    app.run(debug=True)
