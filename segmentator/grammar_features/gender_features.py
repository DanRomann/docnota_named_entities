# Род
import pymorphy2

morph = pymorphy2.MorphAnalyzer()


# Мужской
def is_masc(token):
    m = morph.parse(token['content'])[0]
    return True if m.tag.gender == 'masc' else False


# Женский
def is_femn(token):
    m = morph.parse(token['content'])[0]
    return True if m.tag.gender == 'femn' else False


# Средний
def is_neut(token):
    m = morph.parse(token['content'])[0]
    return True if m.tag.gender == 'neut' else False


features = [is_femn, is_masc, is_neut]
