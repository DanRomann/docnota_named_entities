# Род


# Мужской
def is_masc(m):
    return True if m['morph'].tag.gender == 'masc' else False


# Женский
def is_femn(m):
    return True if m['morph'].tag.gender == 'femn' else False


# Средний
def is_neut(m):
    return True if m['morph'].tag.gender == 'neut' else False


features = [is_femn, is_masc, is_neut]
