Sentiment Analysis using Scikit-learn

Overview:
This project focuses on Sentiment Analysis, a Natural Language Processing (NLP) task that analyzes textual data to determine whether the sentiment expressed is positive, negative, or neutral. The analysis is performed using the Scikit-learn library, along with VADER (Valence Aware Dictionary and sEntiment Reasoner) for sentiment scoring.

Features:
1. Text Preprocessing: The input text undergoes several preprocessing steps such as lowercasing, removal of numbers, stopwords, and special characters.
2. TF-IDF Vectorization: The text data is converted into numerical form using the TfidfVectorizer from Scikit-learn.
3. Cosine Similarity: Measures similarity between text documents.
4. Sentiment Analysis: Sentiment scores are computed using VADER for positive, negative, neutral, and compound sentiments.

Libraries Used:
   - Flask: For building the web interface.
   - Scikit-learn: For vectorizing text and measuring similarity.
   - VADER Sentiment: For sentiment scoring.
   - NLTK: For stopword removal.
   - Python: The project is written in Python.

Installation:
1. Clone this repository:
    - git clone [https://github.com/your-username/sentiment-analysis.git](https://github.com/mounikasrinivasarao/Sentimental_Analysis-ML-)
2. Navigate to the project directory:
    - cd sentiment-analysis
3. Install the required dependencies:
    - pip install -r requirements.txt

Download NLTK stopwords:
   - python -m nltk.downloader stopwords

Project Structure
├── app.py                    # Flask application
├── templates
│   └── form.html             # HTML form for text input
├── requirements.txt          # Required libraries for the project
└── README.md                 # Project documentation (this file)

How It Works:
1. The user inputs a text through a web form.
2. The text is preprocessed by:
    - Converting to lowercase.
    - Removing numbers.
    - Eliminating stopwords.
3. The preprocessed text is passed through VADER sentiment analysis to compute:
    - Positive, negative, neutral, and compound scores.
4. The results are displayed on the web page showing sentiment scores.
   
Running the Project:
1. Start the Flask server:
   - python app.py
2. Open your browser and go to http://127.0.0.1:5002/.
3. Enter the text you want to analyze in the form, and submit.

Dependencies:
1. Flask
2. Scikit-learn
3. NLTK
4. VanderSentiment
5. Python 3.x

You can install the dependencies by running:
   - pip install -r requirements.txt

Future Enhancements:
   - Implement more advanced NLP techniques such as word embeddings.
   - Improve the user interface for better user experience.
   - Incorporate multiple models to compare sentiment scores.
     
Conclusion:
     This project showcases how sentiment analysis can be implemented using Python libraries such as Scikit-learn and VADER. It's a simple yet effective way to analyze text and gain insights from user feedback or social media posts.
