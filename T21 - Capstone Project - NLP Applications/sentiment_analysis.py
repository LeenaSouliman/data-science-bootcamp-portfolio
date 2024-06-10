# Import dataset and packages.
# Load the english language model. 
# Import the csv file, rename it to dataframe.
# Executes tokenisation.
# Specifiy and idtity  the name of colunm to be analysed, reviews.text.

import spacy
import pandas as pd
from textblob import TextBlob

nlp = spacy.load('en_core_web_sm')
df = pd.read_csv('amazon_product_reviews.csv')

# Data Cleaning.
# Use 'dropna' function to remove missing values in the column.
clean_df = df.dropna(subset=['reviews.text'])

# Funtion to process data: remove stop word, lowercase and remove white space.
def preprocess_data(text):
    doc = nlp(text)
    filtered_tokens = [token.text for token in doc if not token.is_stop]
    filtered_text = ' '.join(filtered_tokens)
    filtered_column = filtered_text.lower().strip()
    return filtered_column

# Function to analyse polarity.
def analyse_polarity(text):
    blob_text = TextBlob(text)
    polarity = blob_text.polarity
    return polarity

# Function to assign sentiment.
def determine_sentiment(polarity_score):
    if polarity_score > 0:
        return 'Positive'
    elif polarity_score < 0:
        return 'Negative'
    else:
        return 'Neutral'

# Select two reviews for sentiment analysis.
# '.sample' selects random rows from the column.
sample_df = clean_df.sample(n = 2)

# Apply function to clean data and create polarity and sentiment variables.
# Random rows selected from cleaned_sample.
cleaned_sample = sample_df['reviews.text'].apply(preprocess_data)

# Sentiment and polarity score.
sample_polarity_scores = cleaned_sample.apply(analyse_polarity)
sample_sentiments = sample_polarity_scores.apply(determine_sentiment)

# Create a user-friendly table to display the results.

# Create a variable with empty 2D dataframe which will hold the reviews text selected randomly by panda.
# Create a column called text to store cleaned sample.
# Create another column called polarity score to store polarity results.
# Create another column called sentiment to store the sentiment results. 
sample_table = pd.DataFrame()
sample_table['text'] = cleaned_sample
sample_table['polarity_score'] = sample_polarity_scores
sample_table['sentiment'] = sample_sentiments

print(sample_table)

# Compare similarity of two review products.
text_1 = nlp(cleaned_sample.iloc[0])
text_2 = nlp(cleaned_sample.iloc[1])

similarity_score = text_1.similarity(text_2)

print(f"Similarity between the two reviews: {similarity_score}")