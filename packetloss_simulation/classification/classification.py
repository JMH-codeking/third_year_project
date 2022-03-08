import pathlib
import random
from typing import List
import numpy as np
data_label = list() 

'''turn string into 0 and 1
'''
def demap(_list: List):
    return [0 if _l=='None' else 1 for _l in _list[1:] ]

def hundredize(inputlist: List):
    _l = int(len(inputlist) / 100)
    len_input = _l * 100
    return inputlist[:len_input]

'''split dataset into samples for model training
'''

def data_split(inputlist: List):
    len_samples = int (len(inputlist) / 100)
    final_samplelist = list()

    for i in range(len_samples):
        sample = inputlist[100*i:100*(i+1)]
        final_samplelist.append(sample)

    return final_samplelist

def mix_datasets(
    input_data: List,
    labels: List
):
    final_output = list()
    '''change the datalist into list of dict, then shuffle
    '''

    for _data, _label in zip(input_data, labels):
        data = {
            tuple(_data): _label
        }
        final_output.append(data)

    return final_output

'''label of all data, whole sample data
'''

labels = list() 
sample_list = list()

for a in range (1,4):
    with open (f'../datafile/datafile{a}.txt') as _f:
        data = _f.read().split('\n')

    data = demap(data[:-1])

    data_label.append(data[0])

    real_data = data[1:]
    len_real_data = len(real_data)

    # print (f'''
    #     type of len: {type(len_real_data)}\ntype of data[0]: {type(data[0])}
    # ''')
    failure_node = int(len_real_data * data[0])


    normal_data = real_data[:failure_node]

    fading_data = real_data[failure_node:]
    '''make the data consisted of data having the integer number of hundreds

    Label the datasets and create the whole dataset
    for training and testing
    '''

    normal_data_list = hundredize(normal_data)
    fading_data_list = hundredize(fading_data)
    normal_samplelist = data_split(normal_data_list)
    fading_samplelist = data_split(fading_data_list)


    '''label the data
    '''

    sample_list.extend(normal_samplelist)
    sample_list.extend(fading_samplelist)

    labels.extend([0] * len(normal_samplelist))
    labels.extend([1] * len(fading_samplelist))

final_list = mix_datasets(sample_list, labels)
random.shuffle(final_list)

'''Up to here, processing of data is done
################################################################################

here is the machine learning algorithm
'''



from sklearn.model_selection import train_test_split

'''demap the dict list
'''


data_sets = list()

for _key in final_list:
    data_sets.extend(list(_key.keys()))
data_sets = np.array(data_sets)

data_labels = list()

for _k in final_list:
    data_labels.extend(list(_k.values()))

data_labels = np.array(data_labels)

X_train, X_test, y_train, y_test =  \
    train_test_split(data_sets, data_labels)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.layers import LSTM
from tensorflow.keras.utils import to_categorical

def evaluate_model(trainX, trainy, testX, testy):
    verbose, epochs, batch_size = 0, 15, 64
    n_timesteps, n_features, n_outputs = trainX.shape[1], trainX.shape[2], trainy.shape[1]
    
    model = Sequential()
    model.add(LSTM(100, input_shape=(n_timesteps,n_features)))
    model.add(Dropout(0.5))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(n_outputs, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    
    model.fit(trainX, trainy, epochs=epochs, batch_size=batch_size, verbose=verbose)

    _, accuracy = model.evaluate(testX, testy, batch_size=batch_size, verbose=0)
    return accuracy
        

def run_experiment(trainX, trainy, testX, testy, repeats=10):
    scores = list()
    for r in range(repeats):
        score = evaluate_model(trainX, trainy, testX, testy)
        score = score * 100.0
        print('>#%d: %.3f' % (r+1, score))
        scores.append(score)
    
    m, s = np.mean(scores), np.std(scores)
    print('Accuracy: %.3f%% (+/-%.3f)' % (m, s))








# from sklearn.model_selection import train_test_split

# '''demap the dict list
# '''

# data_set = np.array([list(_keys.keys()) for _keys in final_list])
# data_labels = np.array([list(_keys.values()) for _keys in final_list])

# X_train, X_test, y_train, y_test =  \
#     train_test_split(data_set, data_labels)

# print(y_train.shape)
# print(X_train.shape)

# W1 = np.random.normal(0.0, 1, (100, 200))
# W2 = np.random.normal(0.0, 1, (200, 2)) # two types, 100 data once
# eta = 0.01

# def sigmoid(x):
#     return 1 / (1+np.exp(-x))

# def acc (y_train, y_pred):
#     return sum(y_train = y_pred) / len(y_train)


# for i in range (1):
#     out1 = np.dot(X_train, W1)
#     act1 = sigmoid(out1) # second layer output
#     out2 = np.dot(act1, W2)
#     act2 = sigmoid(out2) # second layer output

#     error = y_train - act2

#     h_err = np.dot(error, W2.T) 

#     W2_der = np.dot(act1.T, -error * act2 * (1 - act2))
#     W1_der = np.dot(X_train.T, -h_err * act1 * (1 - act1))

#     W2 -=  W2_der * eta
#     W1 -=  W1_der * eta

# print (W2_der.shape)
# o1 = np.dot(X_test, W1)
# a1 = sigmoid(o1) # second layer output
# o2 = np.dot(a1, W2)
# a2 = sigmoid(o2) # second layer output

# rs = list()
# for i in range (a2.shape[0]):
#     rs.append(np.argmax(a2[i]))
# rs = np.array(rs)

# print (y_test, rs)



