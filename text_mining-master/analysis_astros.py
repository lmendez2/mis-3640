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

def stop_words(hist):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(hist)

    filtered_tweets = [w for w in word_tokenize if not w in stop_words]
    hist_1 = []
    for w in word_tokens: 
        if w not in stop_words:
            hist_1.append(w)
    return hist_1

def most_common(hist_1):
    """Makes a list of word-freq pairs in descending order of frequency.
    hist: map from word to frequency
    returns: list of (frequency, word) pairs
    """
    t = []
    for key, value in hist.items():
        t.append((value, key))

    t.sort()
    t.reverse()
    return t    




def print_most_common(hist_1, num=20):
    """Prints the most commons words in a histgram and their frequencies.
    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[:num]:
        print(word, '\t', freq)

def main():
    data = process_data()
    hist = process_file(data)
    hist_1 = stop_words(hist)
    print(hist_1)

    t= most_common(hist_1)
    print("The Most Common words are:")
    for freq, word in t[0:20]:
        print(word, '\t', freq)


    sentence = "statuses"
    score = SentimentIntensityAnalyzer().polarity_scores(sentence)
    print(score)


if __name__ == '__main__':
    main()

