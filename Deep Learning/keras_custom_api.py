# -*- coding: utf-8 -*-
"""keras_custom_api.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1krTKGLypMa1g3tqPQpQdXWseOqQaJm-O
"""

import pandas as pd
import numpy as np
import tensorflow, keras

from keras.layers import Dense, Embedding, Input, GRU, Bidirectional, LeakyReLU, Multiply, Concatenate, merge
from keras.models import Model

num_words = 256


input_1 = Input(shape=(None, ))

emb = Embedding(input_dim = num_words+1 , output_dim = 200)(input_1)

bigru_1 = Bidirectional(GRU(256, return_sequences=True))(emb)

dense_1 = Dense(256)(bigru_1)

dense_hidden_1 = Dense(128, activation='relu')(dense_1)

dense_hidden_2 = Dense(256, activation=LeakyReLU(alpha=0.1))(dense_hidden_1)

# emb_2 = Concatenate([dense_1, dense_hidden_2])
# inputs=Concatenate[dense_1, dense_hidden_2]
bigru_2 = Bidirectional(GRU(256))(dense_hidden_2)

# dense_concat = Dense(256)(bigru_2)

input_ran = Input(shape=(256, )) # -- all events in a sentence input

concat = Concatenate()([bigru_2, input_ran])

dense_3 = Dense(256)(concat)

dense_hidden_3 = Dense(128, activation='relu')(dense_3)

dense_hidden_4 = Dense(256, activation=LeakyReLU(alpha=0.1))(dense_hidden_3)

output_1 = Dense(256, activation='sigmoid')(dense_hidden_4)

# input_2 = Input(shape=(256, ))
# output_2 = Multiply()([input_2, output_1])

model = Model(
    inputs=[input_1, input_ran],
    outputs=[output_1]
)

model.summary()

num_words = 256


input_1 = Input(shape=(None, ))

emb = Embedding(input_dim = num_words + 1, output_dim = 200)(input_1)

bigru_1 = Bidirectional(GRU(256, return_sequences=True))(emb)

dense_1 = Dense(256,)(bigru_1)

dense_hidden_1 = Dense(128, activation='relu')(dense_1)

dense_hidden_2 = Dense(256, activation=LeakyReLU(alpha=0.1))(dense_hidden_1)

bigru_2 = Bidirectional(GRU(256))(dense_hidden_2)

output_1 = Dense(256, activation='sigmoid')(bigru_2)

input_2 = Input(shape=(256, ))

output_2 = Multiply()([input_2, output_1])

model = Model(
    inputs=[input_1, input_2],
    outputs=[output_2],
)

model.summary()

keras.utils.plot_model(model, "model_creation.png", show_shapes=True)