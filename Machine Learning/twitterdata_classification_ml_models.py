# -*- coding: utf-8 -*-
"""TwitterData_classification_ML_models.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ohmqvI7basCRQ5ETA5RtUNRzm6hshObU

#Machine Learning Models
1. Naive Bayes
2. Support Vector Machines
3. Logistic Regression
4. Random Forest
5. Ada Boost
6. XG Boost
"""

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

from sklearn import model_selection, naive_bayes, svm, metrics, preprocessing, linear_model
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn import decomposition, ensemble

from keras.preprocessing.sequence import pad_sequences


df = pd.read_csv('/content/drive/My Drive/ML_Data/Sentiment.csv')
df.drop(['id', 'relevant_yn', 'relevant_yn_confidence', 'candidate', 'candidate_confidence', 'sentiment_confidence', 'subject_matter', 'subject_matter_confidence', 'candidate_gold', 'name','relevant_yn_gold','retweet_count', 'sentiment_gold',	'subject_matter_gold', 'tweet_coord', 'tweet_created', 'tweet_id',	'tweet_location',	'user_timezone'], axis=1, inplace=True)



def clean_data(sentence):
  sentence = [w for w in sentence.split(" ") if "RT" not in w]
  sentence = [w for w in sentence if ":" not in w]
  sentence = [w for w in sentence if "#" not in w]
  sentence = [w for w in sentence if "@" not in w]
  sentence = " ".join(sentence)
  return sentence

df["text"] = df["text"].apply(lambda x: clean_data(x))

x = df.text
y = df.sentiment

label = preprocessing.LabelEncoder()

y = label.fit_transform(y)

# Encoding the input text

count_label = CountVectorizer(analyzer='word', token_pattern=r'\w{1,}')

x_count = count_label.fit_transform(x)


tfidf_word_label = TfidfVectorizer(analyzer='word', token_pattern=r'\w{1,}', max_features=5000)

x_tfidf_word = tfidf_word_label.fit_transform(x)


tfidf_ngram_word_label = TfidfVectorizer(analyzer='word', ngram_range=(2, 3), token_pattern=r'\w{1,}', max_features=5000)

x_ngram_tfidf_word = tfidf_ngram_word_label.fit_transform(x)


tfidf_char_label = TfidfVectorizer(analyzer='char', token_pattern=r'\w{1,}', max_features=5000)

x_tfidf_char = tfidf_char_label.fit_transform(x)


tfidf_ngram_char_label = TfidfVectorizer(analyzer='char', ngram_range=(2, 3), token_pattern=r'\w{1,}', max_features=5000)

x_ngram_tfidf_char = tfidf_ngram_char_label.fit_transform(x)

x_train_count, x_test_count, y_train, y_test = train_test_split(x_count, y, test_size=0.2, random_state=42)
x_train_tfidf_word, x_test_tfidf_word, y_train, y_test = train_test_split(x_tfidf_word, y, test_size=0.2, random_state=42)
x_train_ngram_tfidf_word, x_test_ngram_tfidf_word, y_train, y_test = train_test_split(x_ngram_tfidf_word, y, test_size=0.2, random_state=42)
x_train_tfidf_char,  x_test_tfidf_char, y_train, y_test = train_test_split(x_tfidf_char, y, test_size=0.2, random_state=42)
x_train_ngram_tfidf_char,  x_test_ngram_tfidf_char, y_train, y_test = train_test_split(x_ngram_tfidf_char, y, test_size=0.2, random_state=42)

def model_training(model, x_train, y_train, x_test, y_test):

  model.fit(x_train, y_train)
  y_pred = model.predict(x_test)
  accuracy = metrics.accuracy_score(y_pred, y_test)

  return accuracy

accuracyAnalysis = {}
accuracy = model_training(naive_bayes.MultinomialNB(), x_train_count, y_train, x_test_count, y_test)
print("NB countVectorizer: ", accuracy)
accuracyAnalysis["NB countVectorizer"] = accuracy

accuracy = model_training(naive_bayes.MultinomialNB(), x_train_tfidf_word, y_train, x_test_tfidf_word, y_test)
print("NB Tfidf word: ", accuracy)
accuracyAnalysis["NB Tfidf word"] = accuracy

accuracy = model_training(naive_bayes.MultinomialNB(), x_train_ngram_tfidf_word, y_train, x_test_ngram_tfidf_word, y_test)
print("NB ngram countVectorizer: ", accuracy)
accuracyAnalysis["NB ngram countVectorizer"] = accuracy

accuracy = model_training(naive_bayes.MultinomialNB(), x_train_tfidf_char, y_train, x_test_tfidf_char, y_test)
print("NB Tfidf char: ", accuracy)
accuracyAnalysis["NB Tfidf char"] = accuracy

accuracy = model_training(naive_bayes.MultinomialNB(), x_train_ngram_tfidf_char, y_train, x_test_ngram_tfidf_char, y_test)
print("NB ngram Tfidf char: ", accuracy)
accuracyAnalysis["NB ngram Tfidf char"] = accuracy

accuracy = model_training(svm.SVC(), x_train_count, y_train, x_test_count, y_test)
print("SVM countVectorizer: ", accuracy)
accuracyAnalysis["SVM countVectorizer"] = accuracy

accuracy = model_training(svm.SVC(), x_train_tfidf_word, y_train, x_test_tfidf_word, y_test)
print("SVM Tfidf word: ", accuracy)
accuracyAnalysis["SVM Tfidf word"] = accuracy

accuracy = model_training(svm.SVC(), x_train_ngram_tfidf_word, y_train, x_test_ngram_tfidf_word, y_test)
print("SVM ngram countVectorizer: ", accuracy)
accuracyAnalysis["SVM ngram countVectorizer"] = accuracy

accuracy = model_training(svm.SVC(), x_train_tfidf_char, y_train, x_test_tfidf_char, y_test)
print("SVM Tfidf char: ", accuracy)
accuracyAnalysis["SVM Tfidf char"] = accuracy

accuracy = model_training(svm.SVC(), x_train_ngram_tfidf_char, y_train, x_test_ngram_tfidf_char, y_test)
print("SVM ngram Tfidf char: ", accuracy)
accuracyAnalysis["SVM ngram Tfidf char"] = accuracy

accuracy = model_training(linear_model.LogisticRegression(), x_train_count, y_train, x_test_count, y_test)
print("LR countVectorizer: ", accuracy)
accuracyAnalysis["LR countVectorizer"] = accuracy

accuracy = model_training(linear_model.LogisticRegression(), x_train_tfidf_word, y_train, x_test_tfidf_word, y_test)
print("LR Tfidf word: ", accuracy)
accuracyAnalysis["LR Tfidf word"] = accuracy

accuracy = model_training(linear_model.LogisticRegression(), x_train_ngram_tfidf_word, y_train, x_test_ngram_tfidf_word, y_test)
print("LR ngram countVectorizer: ", accuracy)
accuracyAnalysis["LR ngram countVectorizer"] = accuracy

accuracy = model_training(linear_model.LogisticRegression(), x_train_tfidf_char, y_train, x_test_tfidf_char, y_test)
print("LR Tfidf char: ", accuracy)
accuracyAnalysis["LR Tfidf char"] = accuracy

accuracy = model_training(linear_model.LogisticRegression(), x_train_ngram_tfidf_char, y_train, x_test_ngram_tfidf_char, y_test)
print("LR ngram Tfidf char: ", accuracy)
accuracyAnalysis["LR ngram Tfidf char"] = accuracy

accuracy = model_training(ensemble.RandomForestClassifier(), x_train_count, y_train, x_test_count, y_test)
print("RF countVectorizer: ", accuracy)
accuracyAnalysis["RF countVectorizer"] = accuracy

accuracy = model_training(ensemble.RandomForestClassifier(), x_train_tfidf_word, y_train, x_test_tfidf_word, y_test)
print("RF Tfidf word: ", accuracy)
accuracyAnalysis["RF Tfidf word"] = accuracy

accuracy = model_training(ensemble.RandomForestClassifier(), x_train_ngram_tfidf_word, y_train, x_test_ngram_tfidf_word, y_test)
print("RF ngram countVectorizer: ", accuracy)
accuracyAnalysis["RF ngram countVectorizer"] = accuracy

accuracy = model_training(ensemble.RandomForestClassifier(), x_train_tfidf_char, y_train, x_test_tfidf_char, y_test)
print("RF Tfidf char: ", accuracy)
accuracyAnalysis["RF Tfidf char"] = accuracy

accuracy = model_training(ensemble.RandomForestClassifier(), x_train_ngram_tfidf_char, y_train, x_test_ngram_tfidf_char, y_test)
print("RF ngram Tfidf char: ", accuracy)
accuracyAnalysis["RF ngram Tfidf char"] = accuracy

accuracy = model_training(ensemble.AdaBoostClassifier(), x_train_count, y_train, x_test_count, y_test)
print("AB countVectorizer: ", accuracy)
accuracyAnalysis["AB countVectorizer"] = accuracy

accuracy = model_training(ensemble.AdaBoostClassifier(), x_train_tfidf_word, y_train, x_test_tfidf_word, y_test)
print("AB Tfidf word: ", accuracy)
accuracyAnalysis["AB Tfidf word"] = accuracy

accuracy = model_training(ensemble.AdaBoostClassifier(), x_train_ngram_tfidf_word, y_train, x_test_ngram_tfidf_word, y_test)
print("AB ngram countVectorizer: ", accuracy)
accuracyAnalysis["AB ngram countVectorizer"] = accuracy

accuracy = model_training(ensemble.AdaBoostClassifier(), x_train_tfidf_char, y_train, x_test_tfidf_char, y_test)
print("AB Tfidf char: ", accuracy)
accuracyAnalysis["AB Tfidf char"] = accuracy

accuracy = model_training(ensemble.AdaBoostClassifier(), x_train_ngram_tfidf_char, y_train, x_test_ngram_tfidf_char, y_test)
print("AB ngram Tfidf char: ", accuracy)
accuracyAnalysis["AB ngram Tfidf char"] = accuracy

accuracy = model_training(xgboost.XGBClassifier(), x_train_count, y_train, x_test_count, y_test)
print("XGB countVectorizer: ", accuracy)
accuracyAnalysis["XGB countVectorizer"] = accuracy

accuracy = model_training(xgboost.XGBClassifier(), x_train_tfidf_word, y_train, x_test_tfidf_word, y_test)
print("XGB Tfidf word: ", accuracy)
accuracyAnalysis["XGB Tfidf word"] = accuracy

accuracy = model_training(xgboost.XGBClassifier(), x_train_ngram_tfidf_word, y_train, x_test_ngram_tfidf_word, y_test)
print("XGB ngram countVectorizer: ", accuracy)
accuracyAnalysis["XGB ngram countVectorizer"] = accuracy

accuracy = model_training(xgboost.XGBClassifier(), x_train_tfidf_char, y_train, x_test_tfidf_char, y_test)
print("XGB Tfidf char: ", accuracy)
accuracyAnalysis["XGB Tfidf char"] = accuracy

accuracy = model_training(xgboost.XGBClassifier(), x_train_ngram_tfidf_char, y_train, x_test_ngram_tfidf_char, y_test)
print("XGB ngram Tfidf char: ", accuracy)
accuracyAnalysis["XGB ngram Tfidf char"] = accuracy

metrics = sorted(accuracyAnalysis.items(), key=lambda x: x[1], reverse=True)
metrics

import matplotlib.pyplot as plt
!matplotlib inline

x_metrics = []
y_metrics = []

for i in metrics:
  x_metrics.append(i[0])
  y_metrics.append(i[1])


plt.xlabel("Classification Models for text Data")
plt.ylabel("Accuracy Score")
# plt.plot(x_metrics, y_metrics)
plt.bar(x_metrics, y_metrics)
plt.xticks(x_metrics, rotation='vertical')
plt.show()

"""#Lemmatiztion added to Machine Learning Models"""

import pandas as pd
import numpy as np
import warnings
import nltk
warnings.filterwarnings("ignore")

from sklearn import model_selection, naive_bayes, svm, metrics, preprocessing, linear_model
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn import decomposition, ensemble

from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('wordnet')

lemma = WordNetLemmatizer()
from keras.preprocessing.sequence import pad_sequences


df = pd.read_csv('/content/drive/My Drive/ML_Data/Sentiment.csv')
df.drop(['id', 'relevant_yn', 'relevant_yn_confidence', 'candidate', 'candidate_confidence', 'sentiment_confidence', 'subject_matter', 'subject_matter_confidence', 'candidate_gold', 'name','relevant_yn_gold','retweet_count', 'sentiment_gold',	'subject_matter_gold', 'tweet_coord', 'tweet_created', 'tweet_id',	'tweet_location',	'user_timezone'], axis=1, inplace=True)


def clean_data(sentence):
  sentence = [w for w in sentence.split(" ") if "RT" not in w]
  sentence = [w for w in sentence if ":" not in w]
  sentence = [w for w in sentence if "#" not in w]
  sentence = [w for w in sentence if "@" not in w]
  sentence = [lemma.lemmatize(w) for w in sentence if w not in stopwords.words('english')]
  sentence = " ".join(sentence)
  return sentence

df["text"] = df["text"].apply(lambda x: clean_data(x))

x = df.text
y = df.sentiment

label = preprocessing.LabelEncoder()

y = label.fit_transform(y)

# Encoding the input text

count_label = CountVectorizer(analyzer='word', token_pattern=r'\w{1,}')

x_count = count_label.fit_transform(x)


tfidf_word_label = TfidfVectorizer(analyzer='word', token_pattern=r'\w{1,}', max_features=5000)

x_tfidf_word = tfidf_word_label.fit_transform(x)


tfidf_ngram_word_label = TfidfVectorizer(analyzer='word', ngram_range=(2, 3), token_pattern=r'\w{1,}', max_features=5000)

x_ngram_tfidf_word = tfidf_ngram_word_label.fit_transform(x)


tfidf_char_label = TfidfVectorizer(analyzer='char', token_pattern=r'\w{1,}', max_features=5000)

x_tfidf_char = tfidf_char_label.fit_transform(x)


tfidf_ngram_char_label = TfidfVectorizer(analyzer='char', ngram_range=(2, 3), token_pattern=r'\w{1,}', max_features=5000)

x_ngram_tfidf_char = tfidf_ngram_char_label.fit_transform(x)

x_train_count, x_test_count, y_train, y_test = train_test_split(x_count, y, test_size=0.2, random_state=42)
x_train_tfidf_word, x_test_tfidf_word, y_train, y_test = train_test_split(x_tfidf_word, y, test_size=0.2, random_state=42)
x_train_ngram_tfidf_word, x_test_ngram_tfidf_word, y_train, y_test = train_test_split(x_ngram_tfidf_word, y, test_size=0.2, random_state=42)
x_train_tfidf_char,  x_test_tfidf_char, y_train, y_test = train_test_split(x_tfidf_char, y, test_size=0.2, random_state=42)
x_train_ngram_tfidf_char,  x_test_ngram_tfidf_char, y_train, y_test = train_test_split(x_ngram_tfidf_char, y, test_size=0.2, random_state=42)

def model_training(model, x_train, y_train, x_test, y_test):

  model.fit(x_train, y_train)
  y_pred = model.predict(x_test)
  accuracy = metrics.accuracy_score(y_pred, y_test)

  return accuracy

accuracyAnalysis = {}
accuracy = model_training(naive_bayes.MultinomialNB(), x_train_count, y_train, x_test_count, y_test)
print("NB countVectorizer: ", accuracy)
accuracyAnalysis["NB countVectorizer"] = accuracy

accuracy = model_training(naive_bayes.MultinomialNB(), x_train_tfidf_word, y_train, x_test_tfidf_word, y_test)
print("NB Tfidf word: ", accuracy)
accuracyAnalysis["NB Tfidf word"] = accuracy

accuracy = model_training(naive_bayes.MultinomialNB(), x_train_ngram_tfidf_word, y_train, x_test_ngram_tfidf_word, y_test)
print("NB ngram countVectorizer: ", accuracy)
accuracyAnalysis["NB ngram countVectorizer"] = accuracy

accuracy = model_training(naive_bayes.MultinomialNB(), x_train_tfidf_char, y_train, x_test_tfidf_char, y_test)
print("NB Tfidf char: ", accuracy)
accuracyAnalysis["NB Tfidf char"] = accuracy

accuracy = model_training(naive_bayes.MultinomialNB(), x_train_ngram_tfidf_char, y_train, x_test_ngram_tfidf_char, y_test)
print("NB ngram Tfidf char: ", accuracy)
accuracyAnalysis["NB ngram Tfidf char"] = accuracy

accuracy = model_training(svm.SVC(), x_train_count, y_train, x_test_count, y_test)
print("SVM countVectorizer: ", accuracy)
accuracyAnalysis["SVM countVectorizer"] = accuracy

accuracy = model_training(svm.SVC(), x_train_tfidf_word, y_train, x_test_tfidf_word, y_test)
print("SVM Tfidf word: ", accuracy)
accuracyAnalysis["SVM Tfidf word"] = accuracy

accuracy = model_training(svm.SVC(), x_train_ngram_tfidf_word, y_train, x_test_ngram_tfidf_word, y_test)
print("SVM ngram countVectorizer: ", accuracy)
accuracyAnalysis["SVM ngram countVectorizer"] = accuracy

accuracy = model_training(svm.SVC(), x_train_tfidf_char, y_train, x_test_tfidf_char, y_test)
print("SVM Tfidf char: ", accuracy)
accuracyAnalysis["SVM Tfidf char"] = accuracy

accuracy = model_training(svm.SVC(), x_train_ngram_tfidf_char, y_train, x_test_ngram_tfidf_char, y_test)
print("SVM ngram Tfidf char: ", accuracy)
accuracyAnalysis["SVM ngram Tfidf char"] = accuracy

accuracy = model_training(linear_model.LogisticRegression(), x_train_count, y_train, x_test_count, y_test)
print("LR countVectorizer: ", accuracy)
accuracyAnalysis["LR countVectorizer"] = accuracy

accuracy = model_training(linear_model.LogisticRegression(), x_train_tfidf_word, y_train, x_test_tfidf_word, y_test)
print("LR Tfidf word: ", accuracy)
accuracyAnalysis["LR Tfidf word"] = accuracy

accuracy = model_training(linear_model.LogisticRegression(), x_train_ngram_tfidf_word, y_train, x_test_ngram_tfidf_word, y_test)
print("LR ngram countVectorizer: ", accuracy)
accuracyAnalysis["LR ngram countVectorizer"] = accuracy

accuracy = model_training(linear_model.LogisticRegression(), x_train_tfidf_char, y_train, x_test_tfidf_char, y_test)
print("LR Tfidf char: ", accuracy)
accuracyAnalysis["LR Tfidf char"] = accuracy

accuracy = model_training(linear_model.LogisticRegression(), x_train_ngram_tfidf_char, y_train, x_test_ngram_tfidf_char, y_test)
print("LR ngram Tfidf char: ", accuracy)
accuracyAnalysis["LR ngram Tfidf char"] = accuracy

accuracy = model_training(ensemble.RandomForestClassifier(), x_train_count, y_train, x_test_count, y_test)
print("RF countVectorizer: ", accuracy)
accuracyAnalysis["RF countVectorizer"] = accuracy

accuracy = model_training(ensemble.RandomForestClassifier(), x_train_tfidf_word, y_train, x_test_tfidf_word, y_test)
print("RF Tfidf word: ", accuracy)
accuracyAnalysis["RF Tfidf word"] = accuracy

accuracy = model_training(ensemble.RandomForestClassifier(), x_train_ngram_tfidf_word, y_train, x_test_ngram_tfidf_word, y_test)
print("RF ngram countVectorizer: ", accuracy)
accuracyAnalysis["RF ngram countVectorizer"] = accuracy

accuracy = model_training(ensemble.RandomForestClassifier(), x_train_tfidf_char, y_train, x_test_tfidf_char, y_test)
print("RF Tfidf char: ", accuracy)
accuracyAnalysis["RF Tfidf char"] = accuracy

accuracy = model_training(ensemble.RandomForestClassifier(), x_train_ngram_tfidf_char, y_train, x_test_ngram_tfidf_char, y_test)
print("RF ngram Tfidf char: ", accuracy)
accuracyAnalysis["RF ngram Tfidf char"] = accuracy

accuracy = model_training(ensemble.AdaBoostClassifier(), x_train_count, y_train, x_test_count, y_test)
print("AB countVectorizer: ", accuracy)
accuracyAnalysis["AB countVectorizer"] = accuracy

accuracy = model_training(ensemble.AdaBoostClassifier(), x_train_tfidf_word, y_train, x_test_tfidf_word, y_test)
print("AB Tfidf word: ", accuracy)
accuracyAnalysis["AB Tfidf word"] = accuracy

accuracy = model_training(ensemble.AdaBoostClassifier(), x_train_ngram_tfidf_word, y_train, x_test_ngram_tfidf_word, y_test)
print("AB ngram countVectorizer: ", accuracy)
accuracyAnalysis["AB ngram countVectorizer"] = accuracy

accuracy = model_training(ensemble.AdaBoostClassifier(), x_train_tfidf_char, y_train, x_test_tfidf_char, y_test)
print("AB Tfidf char: ", accuracy)
accuracyAnalysis["AB Tfidf char"] = accuracy

accuracy = model_training(ensemble.AdaBoostClassifier(), x_train_ngram_tfidf_char, y_train, x_test_ngram_tfidf_char, y_test)
print("AB ngram Tfidf char: ", accuracy)
accuracyAnalysis["AB ngram Tfidf char"] = accuracy

accuracy = model_training(xgboost.XGBClassifier(), x_train_count, y_train, x_test_count, y_test)
print("XGB countVectorizer: ", accuracy)
accuracyAnalysis["XGB countVectorizer"] = accuracy

accuracy = model_training(xgboost.XGBClassifier(), x_train_tfidf_word, y_train, x_test_tfidf_word, y_test)
print("XGB Tfidf word: ", accuracy)
accuracyAnalysis["XGB Tfidf word"] = accuracy

accuracy = model_training(xgboost.XGBClassifier(), x_train_ngram_tfidf_word, y_train, x_test_ngram_tfidf_word, y_test)
print("XGB ngram countVectorizer: ", accuracy)
accuracyAnalysis["XGB ngram countVectorizer"] = accuracy

accuracy = model_training(xgboost.XGBClassifier(), x_train_tfidf_char, y_train, x_test_tfidf_char, y_test)
print("XGB Tfidf char: ", accuracy)
accuracyAnalysis["XGB Tfidf char"] = accuracy

accuracy = model_training(xgboost.XGBClassifier(), x_train_ngram_tfidf_char, y_train, x_test_ngram_tfidf_char, y_test)
print("XGB ngram Tfidf char: ", accuracy)
accuracyAnalysis["XGB ngram Tfidf char"] = accuracy

metrics = sorted(accuracyAnalysis.items(), key=lambda x: x[1], reverse=True)
metrics

import matplotlib.pyplot as plt
!matplotlib inline

x_metrics_lemmet = []
y_metrics_lemmet = []

for i in metrics:
  x_metrics_lemmet.append(i[0])
  y_metrics_lemmet.append(i[1])


plt.xlabel("Classification Models for text Data With Lemmatization and Stopwords")
plt.ylabel("Accuracy Score")
# plt.plot(x_metrics_lemmet, y_metrics_lemmet)
plt.bar(x_metrics_lemmet, y_metrics_lemmet)
plt.xticks(x_metrics_lemmet, rotation='vertical')
plt.show()

"""#Accuracy Measures of Models with and without (Lemmatization and Stopwords)"""

plt.xlabel("Classification Models for text Data With Lemmatization and Stopwords")
plt.ylabel("Accuracy Score")
# plt.plot(x_metrics, y_metrics)
plt.bar(x_metrics, y_metrics)
plt.xticks(x_metrics, rotation='vertical')
plt.show()

plt.xlabel("Classification Models for text Data With Lemmatization and Stopwords")
plt.ylabel("Accuracy Score")
# plt.plot(x_metrics_lemmet, y_metrics_lemmet)
plt.bar(x_metrics_lemmet, y_metrics_lemmet)
plt.xticks(x_metrics_lemmet, rotation='vertical')
plt.show()