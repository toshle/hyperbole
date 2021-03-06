import nltk

tweets = [
    (['love', 'this', 'car'], 'hyperbole'),
    (['this', 'view', 'amazing'], 'hyperbole'),
    (['feel', 'great', 'this', 'morning'], 'hyperbole'),
    (['excited', 'about', 'the', 'concert'], 'hyperbole'),
    (['best', 'friend'], 'hyperbole'),
    (['not', 'like', 'this', 'car'], 'normal'),
    (['this', 'view', 'horrible'], 'normal'),
    (['feel', 'tired', 'this', 'morning'], 'normal'),
    (['not', 'looking', 'forward', 'the', 'concert'], 'normal'),
    (['enemy'], 'normal')]

test_tweets = [
    (['feel', 'happy', 'this', 'morning'], 'hyperbole'),
    (['larry', 'friend'], 'hyperbole'),
    (['not', 'like', 'that', 'man'], 'normal'),
    (['house', 'not', 'great'], 'normal'),
    (['your', 'song', 'annoying'], 'normal')]

pos_tweets = [('I am so hungry I could eat a horse', 'hyperbole'),
              ('I have a million things to do', 'hyperbole'),
              ('I had to walk 15 miles to school in the snow, uphill', 'hyperbole'),
              ('She is as heavy as an elephant', 'hyperbole'),
              ('He is as fat as a whale', 'hyperbole'),
              ('Like a god', 'hyperbole'),
              ('They ran like greased lightning', 'hyperbole'),
              ('My grandmother is as old as the hills', 'hyperbole'),
              ('I am dying of shame', 'hyperbole'),
              ('I had a ton of homework', 'hyperbole'),
              ('If I can’t buy that new game I will die', 'hyperbole')]

neg_tweets = [('I do not like this car', 'normal'),
              ('I like this car', 'normal'),
              ('This view is horrible', 'normal'),
              ('I feel tired this morning', 'normal'),
              ('I am not looking forward to the concert', 'normal'),
              ('The door is black', 'normal'),
              ('I love you', 'normal'),
              ('He is my enemy', 'normal')]

tweets = pos_tweets + neg_tweets

def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

def comparative_features(features):
    features['contains(as a)'] = 1.0
    features['contains(is as)'] = 1.0
    features['contains(like a)'] = 1.0
    features['contains(is so)'] = 1.0
    return features

def extract_features(document):
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

def training_features(document):
    return comparative_features(extract_features(document))

#base = names + adjectives + nouns

# word_features = get_word_features(get_words_in_tweets(tweets))

training_set = nltk.classify.apply_features(training_features, tweets)

#print(training_set)

classifier = nltk.NaiveBayesClassifier.train(training_set)

print(classifier.show_most_informative_features(32))

# tweet = "He is as fast as a cheetah"
# print(grams_features(tweet))
# # nltk.download()
# print(classifier.classify(extract_features(tweet)))

tweet2 = "Wash the dishes"
print(extract_features(tweet2))
# nltk.download()
print(classifier.classify(extract_features(tweet2)))
#print(nltk.pos_tag(tweet.split()))


# hw_token = nltk.word_tokenize(tweet)
# print(hw_token)


# S   sentence                    the man walked
# NP  noun phrase                 a dog
# VP  verb phrase                 saw a park
# PP  prepositional phrase        with a telescope
# Det determiner                  the
# N   noun                        dog
# V   verb                        walked
# P   preposition                 in

# grammar1 = nltk.CFG.fromstring("""
#   S -> NP VP
#   VP -> V NP | V NP PP
#   PP -> P NP
#   V -> "saw" | "ate" | "walked"
#   NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
#   Det -> "a" | "an" | "the" | "my"
#   N -> "man" | "dog" | "cat" | "telescope" | "park"
#   P -> "in" | "on" | "by" | "with"
#   """)

# sent = "Mary saw Bob".split()
# rd_parser = nltk.RecursiveDescentParser(grammar1)
# for tree in rd_parser.parse(sent):
#     print(tree)