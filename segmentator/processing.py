from io import StringIO
import re, sys
from tokenize import generate_tokens
from convert import bilou
from segmentator.crf import process_model, train_model


def text_to_sentences(text):
    regex = re.compile("""
        (?:
            (?:
                (?<!\\d(?:р|г|к))
                (?<!и\\.т\\.(?:д|п))
                (?<!и(?=\\.т\\.(?:д|п)\\.))
                (?<!и\\.т(?=\\.(?:д|п)\\.))
                (?<!руб|коп)
            \\.) |
            [!?\\n]
        )+
        """, re.X)
    res = []
    sear = regex.search(text)
    while sear:
        res.append(text[:sear.end()])
        text = text[sear.end():]
        sear = regex.search(text)
    res.append(text)
    return res


def sentence_to_tokens(sent):
    STRING = 1
    return list({
                    'content': token[STRING],
                    'tag': bilou.find('O'),
                    'position': i,
                    'cls': '_'
                } for i, token in enumerate(generate_tokens(StringIO(sent).readline)))[:-1]


def process(text):
    text_tokens = [sentence_to_tokens(sent) for sent in text_to_sentences(text)]
    for sent in text_tokens:
        val = process_model(sent)
        for i, t in enumerate(sent):
            t['tag'] = val[i]
    return text_tokens


train_model('../testset')
print(process('Я сегодня, очень хорошо, отлично хорощоооо покушал! А еще кажется Владимир Владимирович сделал тоже самое.'))