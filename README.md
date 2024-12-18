# Sentiment Analysis on Hotel Reviews

## Overview

This project focuses on sentiment analysis of hotel reviews. By leveraging machine learning algorithms, the goal was to classify customer reviews into sentiments such as positive, negative, or neutral. The project includes data preprocessing, feature extraction, model training, evaluation, and deployment of a real-time sentiment analysis web application using Streamlit.

## Project Structure

- **data/**: Contains the dataset used for the analysis.
- **notebooks/**: Jupyter notebooks detailing the data preprocessing, feature extraction, model training, and evaluation processes.
- **models/**: Saved models.
- **app/**: Streamlit application files for deploying the real-time sentiment analysis web app.
- **requirements.txt**: List of required Python packages.
- **README.md**: Project documentation.

## Key Features

### Data Preprocessing

- **Cleaning:** Removing HTML tags, special characters, and stopwords.
- **Tokenization:** Breaking down text into individual words or tokens.
- **Lemmatization:** Reducing words to their base or root form.

### Feature Extraction

- **Bag of Words (BoW):** Converting text data into numerical vectors.
- **TF-IDF:** Term Frequency-Inverse Document Frequency to evaluate the importance of a word in a document relative to a collection of documents.
- **Word2Vec:** Capturing semantic meaning of words by representing them as vectors.

### Model Training and Evaluation

- **Algorithms Used:**
  - Naive Bayes
  - Logistic Regression
  - XGBoost

- **Evaluation Metrics:**
  - Accuracy
  - Precision
  - Recall
  - F1-Score

### Deployment

- **Streamlit App:** A user-friendly web application for real-time sentiment analysis.
- **Deployment Instructions:** Steps to deploy the app locally or on a cloud platform.

## Installation

To run this project, follow these steps:

1. Clone the repository:
   ```
   git clone [https://github.com/yourusername/sentiment-analysis-hotel-reviews](https://github.com/MadasuLaxman/Hackathon_Sentimental_Analysis/).git
 2. Navigate to the project directory: 
  ```
cd sentiment-analysis-hotel-reviews
```
3. Install the required packages:
```
pip install -r requirements.txt
```
# Usage

Running the Streamlit App
To start the Streamlit app, use the following command: 
```
streamlit run app/app.py
```
# Predicting Sentiment
1. Open the web application.
2. Enter a hotel review in the input box.
3. The app will display the predicted sentiment (positive, negative, or neutral).
# Results and Insights
This project provided valuable insights into customer sentiments affecting satisfaction. By analyzing the reviews, we could identify common themes and issues that influence customer experiences positively or negatively.

# Contact
For any inquiries or feedback, please contact me at:

Email: madasulaxman028@gmail.com

LinkedIn: https://www.linkedin.com/in/laxmanmadasu/
