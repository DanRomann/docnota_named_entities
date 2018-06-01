# Признаки уровня предложения
# Слово первое в предложении
def is_first(token):
    return True if token['position'] == 0 else False


features = [is_first]
