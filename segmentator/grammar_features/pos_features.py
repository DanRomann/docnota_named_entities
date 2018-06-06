

# TODO Грамматические признаки
# Существительное
def is_noun(m):
    return True if m['morph'].tag.POS == 'NOUN' else False


# Прилагательное(полное)
def is_adjf(m):
    return True if m['morph'].tag.POS == 'ADJF' else False


# Прилагательное (краткое)
def is_adjs(m):
    return True if m['morph'].tag.POS == 'ADJS' else False



# Компаратив
def is_comp(m):
    return True if m['morph'].tag.POS == 'COMP' else False


# Существительное
def is_verb(m):
    return True if m['morph'].tag.POS == 'VERB' else False


# Существительное
def is_infn(m):
    return True if m['morph'].tag.POS == 'INFN' else False


# Существительное
def is_prtf(m):
    return True if m['morph'].tag.POS == 'PRTF' else False


# Существительное
def is_prts(m):
    return True if m['morph'].tag.POS == 'PRTS' else False


# Существительное
def is_grnd(m):
    return True if m['morph'].tag.POS == 'GRND' else False


# Существительное
def is_nmbr(m):
    return True if m['morph'].tag.POS == 'NUMR' else False


# Существительное
def is_advb(m):
    return True if m['morph'].tag.POS == 'ADVB' else False


# Существительное
def is_npro(m):
    return True if m['morph'].tag.POS == 'NPRO' else False


# Существительное
def is_pred(m):
    return True if m['morph'].tag.POS == 'PRED' else False


# Существительное
def is_prep(m):
    return True if m['morph'].tag.POS == 'PREP' else False


# Существительное
def is_conj(m):
    return True if m['morph'].tag.POS == 'CONJ' else False


# Существительное
def is_prcl(m):
    return True if m['morph'].tag.POS == 'PRCL' else False


# Существительное
def is_intj(m):
    return True if m['morph'].tag.POS == 'INTJ' else False


features = [is_adjf, is_adjs, is_advb, is_comp, is_conj, is_grnd, is_infn, is_intj, is_nmbr, is_noun, is_npro, is_prcl, is_pred, is_prep, is_prtf, is_prts, is_verb]