import pymorphy2


morph = pymorphy2.MorphAnalyzer()


# Признаки уровня слова
# Нижний регистр
def is_lower(token):
    return token['content'].islower()


# Верхний регистр
def is_upper(token):
    return token['content'].isupper()


# Название
def is_title(token):
    return token['content'].istitle()


# Числовое значение
def is_digit(token):
    return token['content'].isdigit()


# Пунктуация
def is_pnct(token):
    m = morph.parse(token['content'])[0]
    return True if 'PNCT' in m.tag else False


# Латинские символы
def is_latn(token):
    m = morph.parse(token['content'])[0]
    return True if 'LATN' in m.tag else False


# число
def is_numb(token):
    m = morph.parse(token['content'])[0]
    return True if 'NUMB' in m.tag else False


features = [is_lower, is_upper, is_title, is_digit, is_pnct, is_numb, is_latn]
