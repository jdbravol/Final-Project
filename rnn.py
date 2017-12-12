from __future__ import print_function
from utils import *
import matplotlib.pyplot as plt
import numpy as np
import time
import pronouncing
import csv
from keras.models import Sequential
from keras.layers.wrappers import TimeDistributed
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM, SimpleRNN
import argparse

data_files = './all_artists'
batch = 50
hidden = 500
sequence = 50
pre_weights = ''
gen_length = 500
layers = 2

# generate data
X, y, VOCAB_SIZE, ix_to_char = load_data(data_files, sequence)

# build model
model = Sequential()
model.add(LSTM(hidden, input_shape=(None, VOCAB_SIZE), return_sequences=True))
for i in range(layers - 1):
  model.add(LSTM(hidden, return_sequences=True))

model.add(TimeDistributed(Dense(VOCAB_SIZE)))
model.add(Activation('softmax'))

model.compile(loss="categorical_crossentropy", optimizer="rmsprop")

# load old weights
if not pre_weights == '':
  model.load_weights(pre_weights)
  nb_epoch = int(pre_weights[pre_weights.rfind('_') + 1:pre_weights.find('.')])
else:
  nb_epoch = 0

# train if there's no old weights 
if pre_weights == '':
  while True:
    print('\nEpoch: '+ str(nb_epoch) + '\n')
    model.fit(X, y, batch=batch, verbose=1, nb_epoch=1)
    nb_epoch += 1
    generate_text(model, gen_length, VOCAB_SIZE, ix_to_char)
    if nb_epoch % 10 == 0:
      model.save_pre_weights('checkpoint_layer_{}_hidden_{}_epoch_{}.hdf5'.format(layers,hidden, nb_epoch))
      
# generate with loaded weights 
else:
  model.load_weights(pre_weights)
  generate_text(model, gen_length, VOCAB_SIZE, ix_to_char)
  print('\n\n')