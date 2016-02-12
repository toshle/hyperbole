# -*- coding: utf-8 -*-
from Fetcher import Fetcher
from Classifier import Classifier

hyp_tweets = [('I am so hungry I could eat a horse', 'hyperbole'),
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

nor_tweets = [('I do not like this car', 'normal'),
              ('I like this car', 'normal'),
              ('This view is horrible', 'normal'),
              ('I feel tired this morning', 'normal'),
              ('I am not looking forward to the concert', 'normal'),
              ('The door is black', 'normal'),
              ('I love you', 'normal'),
              ('He is my enemy', 'normal')]

tweets = hyp_tweets + nor_tweets

classifier = Classifier()

classifier.train(tweets)
for tweet in Fetcher.fetch("hyperbole", 10):
  print(classifier.classify(tweet))