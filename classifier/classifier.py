from sklearn.linear_model import LogisticRegression

from convert import bilou
from convert import convert_test_dataset

from classifier.feature_classifier import features

import numpy as np

class Entity:
    tokens = []
    cls = ''
    content = ''

    def init_content(self):
        content = [token.content for token in self.tokens]
        self.content = ' '.join(content)

    def __str__(self):
        self.init_content()
        return '<' + self.content + ' cls:' + self.cls + ' tokens:' + str([token.id for token in self.tokens])


def init_entities(sent):
    entities = []
    entity = None
    for token in sent:
        if token.tag == bilou.find('B'):
            entity = Entity()
            entity.tokens = []
            entity.tokens.append(token)
            entity.cls = token.cls
        elif token.tag == bilou.find('I') and entity != None and entity.cls == token.cls:
            entity.tokens.append(token)
        elif token.tag == bilou.find('L') and entity != None and entity.cls == token.cls:
            entity.tokens.append(token)
            entities.append(entity)
            entity = None
        elif token.tag == bilou.find('U') and entity == None:
            entity = Entity()
            entity.tokens = []
            entity.tokens.append(token)
            entity.cls = token.cls
            entities.append(entity)
            entity = None
    return entities


dataset = convert_test_dataset('testset')

# test_entities = [init_entities(sent) for sent in dataset]
test_entities = [entity for sent in dataset for entity in init_entities(sent)]

test_content = [entity.content for entity in test_entities]
test_features = np.array([np.array([f(content) for f in features]) for content in test_content])
test_cls = np.array([entity.cls for entity in test_entities])

for ent in test_entities:
    print(str(ent))

classifier = LogisticRegression()

print(test_features.shape)
print(test_cls.shape)

classifier.fit(test_features, test_cls)






