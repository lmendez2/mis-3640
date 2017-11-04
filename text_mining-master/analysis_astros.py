from twython import Twython
import random 
import string
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def process_data():
    # Replace the following strings with your own keys and secrets
    TOKEN = '926141030096875520-cPeB28AALjsDqXlrgZFfBP9UmmVJQsl'
    TOKEN_SECRET = 'v5d6uTaXnNYPHNjhgVJBeZ4A77NznKmHwl7qRh9zzvHmw'
    CONSUMER_KEY = '59CIo2eOMd7m8fjXVMHLBLjCY'
    CONSUMER_SECRET = '5tvo8vOrQqX4MYMOaMuiCbj5eBhVv06hIHKJtRMVK8iza77mCM'

    t = Twython(CONSUMER_KEY, CONSUMER_SECRET,
    TOKEN, TOKEN_SECRET)

    data = t.search(q="Astros", count=50)
    return data


def process_file(data):
    """Makes a histogram that contains the words from a file.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    hist = {}

    for status in data['statuses']:
        line = status['text'].replace("-", " ")
        strippables = string.punctuation + string.whitespace 
        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()
            hist[word] = hist.get(word, 0) + 1 
    return hist

def main():
    data = process_data()
    hist = process_file(data)
    print(hist)

if __name__ == '__main__':
    main()

