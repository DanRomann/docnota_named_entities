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


# X_Test = []
# for i, sent in enumerate(train_data):
#     X_Test.append(word2features(sent))
#     # index = str(i+1) + ' from ' + str(len(train_data))
#     # print(index)
# X_Test = np.array(X_Test)
# Y_Test = np.array([np.array(sent2tag(sent)) for sent in train_data])

model = ChainCRF()
ssvm = FrankWolfeSSVM(model=model, C=.1, max_iter=10)


def train_model(dir, x_test=None, y_test=None):
    train_data = convert.convert_test_dataset(dir)
    x__train = []
    for i, sent in enumerate(train_data):
        x__train.append(word2features(sent))
        index = str(i + 1) + ' from ' + str(len(train_data))
        print(index)
    x__train = np.array(x__train)
    y__train = np.array([np.array(sent2tag(sent)) for sent in train_data])
    ssvm.fit(x__train, y__train)
    if x_test is not None and y_test is not None:
        print("Test score with chain CRF: %f" % ssvm.score(x_test, y_test))


def process_model(tokens):

    x__data = np.array([word2features(tokens)])
    print(x__data.shape[1])
    print(model.n_features)
    print(tokens)
    y__data = ssvm.predict(x__data)[0]
    print(y__data)
    return y__data

