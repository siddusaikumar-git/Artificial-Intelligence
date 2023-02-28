# -*- coding: utf-8 -*-
"""N_Grams_Language_Model_Reuters.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mgB0Pl27KHhzLWYNMzwfGL07p9T-xhkK

# N-gram Language Model

Here's what you will learn in this project:

 - 3-gram language model on news documents (Reuters corpus)
 - Predict the next word in a sentence
 - Generate a random news text
 - Find probability of a sentence

## Loading required libraries and corpuses
"""

import nltk
from nltk.corpus import reuters

# loading corpus
nltk.download('reuters')
nltk.download('punkt')

"""## About the Dataset

Reuters corpus is a collection of 10,788 news documents totaling 1.3 million words. 
"""

reuters.categories()

"""Let's have a look at first 10 documents:"""

# print 10 sentences of the reuters corpus
for i, sent in enumerate(reuters.sents()[:10]):
  print("sent ", i, ":", " ".join(sent))

"""## Model building


"""

from nltk import bigrams, trigrams

# trigrams
[x for x in trigrams("the price of petrol has dropped".split())]

from nltk.corpus import reuters
from collections import Counter, defaultdict

# Create a placeholder for model
model = defaultdict(lambda: defaultdict(lambda: 0))

# Count frequency of co-occurance  
for sentence in reuters.sents():
    for w1, w2, w3 in trigrams(sentence, pad_right=True, pad_left=True):
        model[(w1, w2)][w3] += 1

"""**Let's see this in action...here is how our model would like:**"""

model

# predict the next word
dict(model["world", "markets"])

# find the overall frequency of words in the corpus
counts = Counter(reuters.words())
total_count = len(reuters.words())
 
# relative frequencies
for word in counts:
    counts[word] /= float(total_count)
    
# Let's transform the counts to probabilities
for w1_w2 in model:
    total_count = float(sum(model[w1_w2].values()))
    for w3 in model[w1_w2]:
        model[w1_w2][w3] /= total_count

# predict the next word
dict(model["world", "markets"])

"""## Inference - Text generation"""

# predict the next word
sorted(dict(model["today", "the"]).items(), key=lambda x: x[1], reverse=True)

sorted(dict(model["the", "price"]).items(), key=lambda x: x[1], reverse=True)

import random

def gen_text():

  # starting words
  text = ["today", "the"]
  sentence_finished = False
  
  while not sentence_finished:
    # select a random probability threshold  
    r = random.random()
    accumulator = .0

    for word in model[tuple(text[-2:])].keys():
        accumulator += model[tuple(text[-2:])][word]

        # select words that are above the probability threshold
        if accumulator >= r:
            text.append(word)
            break

    if text[-2:] == [None, None]:
        sentence_finished = True
  
  print (' '.join([t for t in text if t]))

for i in range(5):
  gen_text()

"""### 3. Sentence probability"""

# find probability of a sentence

def sent_prob(sent):
  probs = []
  trigram_seq = [x for x in trigrams(sent.split())]
  for w1, w2, w3 in trigram_seq:
      probs.append(model[w1, w2][w3])
  return probs

model["the", "price"]["of"]

sent_prob("the price of oil has dropped")
# [x for x in trigrams("the price of oil has dropped".split())],sent_prob("the price of oil has dropped")

sent_prob("the price of all has dropped")

sent_prob("oil and natural gas")

sent_prob("owl and natural gas")

sent_prob("large price of stock")

sent_prob("high price of stock")
