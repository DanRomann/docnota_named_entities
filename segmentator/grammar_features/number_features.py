# Число
import pymorphy2

morph = pymorphy2.MorphAnalyzer()


# Единственное
def is_sing(token):
    m = morph.parse(token['content'])[0]
    return True if m.tag.number == 'sing' else False


# Множественное
def is_plur(token):
    m = morph.parse(token['content'])[0]
    return True if m.tag.number == 'plur' else False


features = [is_plur, is_sing]