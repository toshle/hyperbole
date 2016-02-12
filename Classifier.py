import nltk

class Classifier:
    def __init__(self):
        pass

    def get_words_in_tweets(self, tweets):
      all_words = []
      for (words, sentiment) in tweets:
        all_words.extend(words)
      return all_words

    def get_word_features(self, wordlist):
        wordlist = nltk.FreqDist(wordlist)
        word_features = wordlist.keys()
        return word_features

    def comparative_features(self, features):
        features['contains(as a)'] = 1.0
        features['contains(is as)'] = 1.0
        features['contains(like a)'] = 1.0
        features['contains(is so)'] = 1.0
        return features

    def extract_features(self, document):
        features = {}
        #porter = nltk.PorterStemmer()
        tokens = nltk.word_tokenize(document)
        tokens = [t.lower() for t in tokens] 
        bigrams = nltk.bigrams(tokens)
        bigrams = [tup[0]+' ' +tup[1] for tup in bigrams]
        grams = tokens + bigrams
        for t in grams:
            if(len(t) > 2):
                features['contains(%s)' % t] = 1.0
        return features

    def training_features(self, document):
        return self.comparative_features(self.extract_features(document))

    def train(self, tweets):
        training_set = nltk.classify.apply_features(self.training_features, tweets)
        self.classifier = nltk.NaiveBayesClassifier.train(training_set)

    def classify(self, tweet):
        return self.classifier.classify(self.extract_features(tweet))