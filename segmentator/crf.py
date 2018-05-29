from pystruct.models import ChainCRF
from pystruct.learners import FrankWolfeSSVM

import convert
from segmentator.features_segmentator import features
import numpy as np

train_data = convert.convert_test_dataset('testset')


def word2features(sent):
    f_list = []
    for i, token in enumerate(sent):
        feat = [f(token) for f in features]
        f_list.append(np.array(feat))
    return f_list


def sent2tag(sent):
    return [token.tag for token in sent]


def sent2content(sent):
    return [token.content for token in sent]


X_Train = np.array([np.array(word2features(sent)) for sent in train_data])
Y_Train = np.array([np.array(sent2tag(sent)) for sent in train_data])
print(X_Train[0])
print(Y_Train[0])

model = ChainCRF(n_states=5)
ssvm = FrankWolfeSSVM(model=model, C=.1, max_iter=10)
ssvm.fit(X_Train, Y_Train)
