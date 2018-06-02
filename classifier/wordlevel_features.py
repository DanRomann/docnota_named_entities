import pymorphy2


morph = pymorphy2.MorphAnalyzer()


# Признаки уровня слова
# Нижний регистр
def is_lower(m):
    return m['content'].islower()


# Верхний регистр
def is_upper(m):
    return m['content'].isupper()


# Название
def is_title(m):
    return m['content'].istitle()


# Числовое значение
def is_digit(m):
    return m['content'].isdigit()


# Пунктуация
def is_pnct(m):
    return True if 'PNCT' in m['morph'].tag else False


# Латинские символы
def is_latn(m):
    return True if 'LATN' in m['morph'].tag else False


# число
def is_numb(m):
    return True if 'NUMB' in m['morph'].tag else False


features = [is_lower, is_upper, is_title, is_digit, is_pnct, is_numb, is_latn]
