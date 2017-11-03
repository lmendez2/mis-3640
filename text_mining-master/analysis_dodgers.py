from twython import Twython
import random 
import string
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Replace the following strings with your own keys and secrets
TOKEN = '926141030096875520-cPeB28AALjsDqXlrgZFfBP9UmmVJQsl'
TOKEN_SECRET = 'v5d6uTaXnNYPHNjhgVJBeZ4A77NznKmHwl7qRh9zzvHmw'
CONSUMER_KEY = '59CIo2eOMd7m8fjXVMHLBLjCY'
CONSUMER_SECRET = '5tvo8vOrQqX4MYMOaMuiCbj5eBhVv06hIHKJtRMVK8iza77mCM'


"""t = Twython(CONSUMER_KEY, CONSUMER_SECRET,
   TOKEN, TOKEN_SECRET)

data = t.search(q="Astros", count=50)


for status in data['statuses']:
 print(status['text'])"""

def process_file(data):
    """Makes a histogram that contains the words from a file.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    hist = {}

    for line in data:
        line = line.replace("-", " ")
        strippables = string.punctuation + string.whitespace
        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()
            hist[word] = hist.get(word, 0) + 1 
    return hist

def most_common(hist):
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


def print_most_common(hist, num=20):
    """Prints the most commons words in a histgram and their frequencies.
    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[:num]:
        print(word, '\t', freq)

def main():
    t = Twython(CONSUMER_KEY , CONSUMER_SECRET , TOKEN , TOKEN_SECRET)
    data = t.search(q="Dodgers", count=50)
    
    tweet_list = []
    for status in data['statuses']:
        tweet_list.append(status['text'])

    hist = process_file(tweet_list)
    print(hist)

    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[0:20]:
        print(word, '\t', freq)

    words = process_file('text')

    sentence = "statuses"
    score = SentimentIntensityAnalyzer().polarity_scores(sentence)
    print(score)

if __name__ == '__main__':
    main()