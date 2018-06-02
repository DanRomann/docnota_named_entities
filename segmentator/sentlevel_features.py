# Признаки уровня предложения
# Слово первое в предложении
def is_first(m):
    return True if m['position'] == 0 else False


features = [is_first]
