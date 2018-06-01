# Признаки-падежи
import pymorphy2

morph = pymorphy2.MorphAnalyzer()


# Именительный падеж
def is_nomn(token):
    m = morph.parse(token['content'])[0]
    return True if m.tag.case == 'nomn' else False


# Именительный падеж
def is_gent(token):
    m = morph.parse(token['content'])[0]
    return True if m.tag.case == 'gent' else False


# Именительный падеж
def is_datv(token):
    m = morph.parse(token['content'])[0]
    return True if m.tag.case == 'datv' else False


# Именительный падеж
def is_accs(token):
    m = morph.parse(token['content'])[0]
    return True if m.tag.case == 'accs' else False


# Именительный падеж
def is_ablt(token):
    m = morph.parse(token['content'])[0]
    return True if m.tag.case == 'ablt' else False


# Именительный падеж
def is_loct(token):
    m = morph.parse(token['content'])[0]
    return True if m.tag.case == 'loct' else False


# Именительный падеж
def is_voct(token):
    m = morph.parse(token['content'])[0]
    return True if m.tag.case == 'voct' else False


# Именительный падеж
def is_gen2(token):
    m = morph.parse(token['content'])[0]
    return True if m.tag.case == 'gen2' else False


# Именительный падеж
def is_acc2(token):
    m = morph.parse(token['content'])[0]
    return True if m.tag.case == 'acc2' else False


# Именительный падеж
def is_loc2(token):
    m = morph.parse(token['content'])[0]
    return True if m.tag.case == 'loc2' else False


features = [is_ablt, is_acc2, is_accs, is_datv, is_gen2, is_gent, is_loc2, is_loct, is_nomn, is_voct]