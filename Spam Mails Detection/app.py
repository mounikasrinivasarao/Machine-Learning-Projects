from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('Index.html', input_mail="")

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Load the dataset
        raw_mail_data = pd.read_csv('spam_mail_data.csv')
        # Convert 'spam' and 'ham' labels to 0 and 1
        raw_mail_data['Category'] = raw_mail_data['Category'].map({'spam': 0, 'ham': 1})
        
        # Extract features and labels
        X = raw_mail_data['Message']
        Y = raw_mail_data['Category']
        
        # Create a TF-IDF vectorizer
        feature_extraction = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)
        
        # Transform text data into numerical features
        X_features = feature_extraction.fit_transform(X)
        
        # Create and train the SVM model
        model = SVC()
        model.fit(X_features, Y)
        
        # Get user input from the form
        input_mail = request.form['input_mail']
        
        # Transform the user input into numerical features
        input_data_features = feature_extraction.transform([input_mail])
        
        # Make a prediction
        prediction = model.predict(input_data_features)
        
        # Determine if it's spam or ham
        if prediction[0] == 1:
            k = 'Ham mail'
        else:
            k = 'Spam mail'
    
    return render_template("Index.html", k=k, input_mail=input_mail)

if __name__ == "main":
    app.run(debug=True)
