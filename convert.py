import numpy as np
import glob
import os


bilou = 'BILOU'


# class Token:
#     # tag = 'O'
#     id = 0
#     tag = bilou.find('O')
#     cls = '_'
#     content = ''
#     position = 0
#
#     def __str__(self):
#         return '<' + str(self.id) + ' ' + self.tag + ' ' + self.cls + ' ' + self.content + ' position:' + str(self.position) + '>'


class Span:
    tokens = []
    cls = '_'
    tag = 'O'

    def __str__(self):
        return '<' + str(self.id) + ' ' + self.cls + ' ' + str(self.tokens) + ' ' + self.tag + '>'


class Object:
    spans = []

    def __str__(self):
        return '<' + str(self.id) + ' ' + self.cls + ' ' + str(self.spans) + '>'


def read_tokens(file):
    sentence = []
    tokens = []
    file = open(file + '.tokens', 'r')
    for token in file:
        # print(token.strip())
        if token.strip() != '':
            params = token.strip().split(" ")
            # t = Token()
            # t.id = int(params[0])
            # t.content = params[3]
            t = {
                'cls': '_',
                'tag': bilou.find('O'),
                'id': int(params[0]),
                'content': params[3],
                'position': 0
            }
            tokens.append(t)

        else:
            sentence.append(tokens)
            tokens = []
    return sentence


def read_spans(file):
    spans = []
    file = open(file + '.spans', 'r')
    for span in file:
        params = span.strip().split(" ")
        spn = Span()
        spn.id = int(params[0])
        spn.tokens = []
        count = int(params[5])
        for i in range(0, count):
            spn.tokens.append(int(params[8 + i]))
        spans.append(spn)
    return spans


def read_objects(file):
    objects = []
    file = open(file + '.objects', 'r')
    for obj in file:
        params = obj.strip().split(" ")
        object = Object()
        object.id = int(params[0])
        object.cls = params[1]
        object.spans = []
        i = 2
        while params[i] != '#':
            object.spans.append(int(params[i]))
            i += 1
        objects.append(object)
    return objects


def set_params_on_spans(span, objs):
    for obj in objs:
        if span.id in obj.spans:
            span.cls = obj.cls
            if len(obj.spans) == 1:
                span.tag = 'U'
            elif len(obj.spans) > 1:
                if obj.spans[0] == span.id:
                    span.tag = 'B'
                elif obj.spans[-1] == span.id:
                    span.tag = 'L'
                else:
                    span.tag = 'I'


def set_params_on_tokens(token, spans):
    tag = 'O'
    for span in spans:
        if token['id'] in span.tokens and span.cls != '_' and token['tag'] == bilou.find('O'):
            token['cls'] = span.cls
            if span.tag == 'B':
                if token['id'] == span.tokens[0]:
                    tag = 'B'
                else:
                    tag = 'I'
            elif span.tag == 'I':
                tag = 'I'
            elif span.tag == 'L':
                if token['id'] == span.tokens[-1]:
                    tag = 'L'
                else:
                    tag = 'I'
            elif span.tag == 'U':
                if len(span.tokens) > 1:
                    if token['id'] == span.tokens[0]:
                        tag = 'B'
                    elif token['id'] == span.tokens[-1]:
                        tag = 'L'
                    else:
                            tag = 'I'
                elif len(span.tokens) == 1:
                    tag = 'U'
    token['tag'] = bilou.find(tag)
    # token.tag = tag


def convert_test_dataset(files):
    text = []
    sent_vector = []
    # os.chdir(dir)
    # files = os.listdir()
    dict_files = list(map(lambda t: os.path.splitext(t)[0], (list(filter(lambda x: x.endswith('.txt'), files)))))
    # print(len(dict_files))
    for name in dict_files:
        sentences = read_tokens(name)
        spans = read_spans(name)
        objects = read_objects(name)
        for spn in spans:
            set_params_on_spans(spn, objects)
        # print(len(sentences))

        for sent in sentences:
            for index, tkn in enumerate(sent):
                set_params_on_tokens(tkn, spans)
                tkn['position'] = index
            text.append(sent)
    return text

