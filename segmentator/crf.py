from pystruct.models import ChainCRF
from pystruct.learners import FrankWolfeSSVM

import convert

from segmentator import wordlevel_features
from segmentator import sentlevel_features
from segmentator.grammar_features import case_features
from segmentator.grammar_features import gender_features
from segmentator.grammar_features import number_features
from segmentator.grammar_features import pos_features

import numpy as np

import time

import pymorphy2

train_data = convert.convert_test_dataset('testset')

features = list(set().union(wordlevel_features.features, sentlevel_features.features, case_features.features, gender_features.features, number_features.features, pos_features.features))

morph = pymorphy2.MorphAnalyzer()


def word2features(sent):
    f_list = []
    start_time = time.time()
    for token in sent:
        word = {
            'morph': morph.parse(token['content'])[0],
            'content': token['content'],
            'position': token['position']
        }
        feat = []
        for f in features:
            feat.append(f(word))
        f_list.append(feat)
    print(time.time() - start_time)
    return np.array(f_list)


def sent2tag(sent):
    return [token['tag'] for token in sent]


def sent2content(sent):
    return [token['content'] for token in sent]


X_Train = []
for i, sent in enumerate(train_data):
    X_Train.append(word2features(sent))
    index = str(i+1) + ' from ' + str(len(train_data))
    print(index)
X_Train = np.array(X_Train)
Y_Train = np.array([np.array(sent2tag(sent)) for sent in train_data])
# X_Train = np.array(word2features(train_data[0]))
# Y_Train = np.array(sent2tag(train_data[0]))
# print(X_Train[0])
# print(Y_Train[0])

X_Test = []
for i, sent in enumerate(train_data):
    X_Test.append(word2features(sent))
    # index = str(i+1) + ' from ' + str(len(train_data))
    # print(index)
X_Test = np.array(X_Test)
Y_Test = np.array([np.array(sent2tag(sent)) for sent in train_data])

model = ChainCRF()
ssvm = FrankWolfeSSVM(model=model, C=.1, max_iter=10)
ssvm.fit(X_Train, Y_Train)

print("Test score with chain CRF: %f" % ssvm.score(X_Test, Y_Test))
