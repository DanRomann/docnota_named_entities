# Число
import pymorphy2

morph = pymorphy2.MorphAnalyzer()


# Единственное
def is_sing(m):
    return True if m['morph'].tag.number == 'sing' else False


# Множественное
def is_plur(m):
    return True if m['morph'].tag.number == 'plur' else False


features = [is_plur, is_sing]