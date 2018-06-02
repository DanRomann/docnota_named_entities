# Признаки-падежи


# Именительный падеж
def is_noun(m):
    return True if m['morph'].tag.case == 'nomn' else False


# Именительный падеж
def is_gent(m):
    return True if m['morph'].tag.case == 'gent' else False


# Именительный падеж
def is_datv(m):
    return True if m['morph'].tag.case == 'datv' else False


# Именительный падеж
def is_accs(m):
    return True if m['morph'].tag.case == 'accs' else False


# Именительный падеж
def is_ablt(m):
    return True if m['morph'].tag.case == 'ablt' else False


# Именительный падеж
def is_loct(m):
    return True if m['morph'].tag.case == 'loct' else False


# Именительный падеж
def is_voct(m):
    return True if m['morph'].tag.case == 'voct' else False


# Именительный падеж
def is_gen2(m):
    return True if m['morph'].tag.case == 'gen2' else False


# Именительный падеж
def is_acc2(m):
    return True if m['morph'].tag.case == 'acc2' else False


# Именительный падеж
def is_loc2(m):
    return True if m['morph'].tag.case == 'loc2' else False


features = [is_ablt, is_acc2, is_accs, is_datv, is_gen2, is_gent, is_loc2, is_loct, is_noun, is_voct]