from sklearn.linear_model import LogisticRegression

from convert import bilou
from convert import convert_test_dataset

from classifier import wordlevel_features
from classifier.grammar_features import case_features
from classifier.grammar_features import gender_features
from classifier.grammar_features import number_features
from classifier.grammar_features import pos_features

import numpy as np

import pymorphy2

morph = pymorphy2.MorphAnalyzer()

features = list(
    set().union(wordlevel_features.features, case_features.features, gender_features.features, number_features.features,
                pos_features.features))

print(features)


class Entity:
    sentence = -1
    tokens = []
    cls = ''
    content = ''

    def init_content(self):
        content = [token['content'] for token in self.tokens]
        self.content = ' '.join(content)

    def __str__(self):
        self.init_content()
        return '<' + self.content + ' cls:' + self.cls + ' tokens:' + str([token['id'] for token in self.tokens])

classifier = LogisticRegression()


def init_entities(sent, sent_id=-1):
    entities = []
    entity = None
    for i, token in enumerate(sent):
        if token['tag'] == bilou.find('B'):
            entity = Entity()
            entity.tokens = []
            entity.tokens.append(token)
            entity.cls = token['cls']
            entity.sentence = sent_id
        elif token['tag'] == bilou.find('I') and entity is not None and entity.cls == token['cls']:
            entity.tokens.append(token)
        elif token['tag'] == bilou.find('L') and entity is not None and entity.cls == token['cls']:
            entity.tokens.append(token)
            entity.init_content()
            entities.append(entity)
            entity = None
        elif token['tag'] == bilou.find('U') and entity is None:
            entity = Entity()
            entity.tokens = []
            entity.sentence = sent_id
            entity.tokens.append(token)
            entity.cls = token['cls']
            entity.init_content()
            entities.append(entity)
            entity = None

    return entities


def train_model(files):
    dataset = convert_test_dataset(files)

    # test_entities = [init_entities(sent) for sent in dataset]
    test_entities = [entity for sent in dataset for entity in init_entities(sent)]

    test_content = [{'content': entity.content, 'morph': morph.parse(entity.content)[0], } for entity in test_entities]
    # print(test_content[0])
    test_features = np.array([np.array([f(content) for f in features]) for content in test_content])
    test_cls = np.array([entity.cls for entity in test_entities])

    # print(str(test_entities[0]))
    # for feat in test_features:
    #     print(feat)
    # print(test_cls[0])

    classifier.fit(test_features, test_cls)


def process_model(text):
    entities = [entity for i, sent in enumerate(text) for entity in init_entities(sent, i)]
    content = [{'content': entity.content, 'morph': morph.parse(entity.content)[0], } for entity in entities]
    # print(test_content[0])
    feats = np.array([np.array([f(content) for f in features]) for content in content])
    # for feat in feats:
    res = classifier.predict(feats)
    print(res)
    for i, ent in enumerate(entities):
        for j in ent.tokens:
            text[ent.sentence][j['position']]['cls'] = res[i]
    print(text)
    return text

