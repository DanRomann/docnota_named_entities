import pymorphy2

# анализатор слов
morph = pymorphy2.MorphAnalyzer()


# TODO Грамматические признаки
# Существительное
def is_noun(token):
    m = morph.parse(token['content'])[0]
    return True if m.tag.POS == 'NOUN' else False


# Прилагательное(полное)
def is_adjf(token):
    m = morph.parse(token['content'])[0]
    return True if m.tag.POS == 'ADJF' else False


# Прилагательное (краткое)
def is_adjs(token):
    m = morph.parse(token['content'])[0]
    return True if m.tag.POS == 'ADJS' else False


# Компаратив
def is_comp(token):
    m = morph.parse(token['content'])[0]
    return True if m.tag.POS == 'COMP' else False


# Существительное
def is_verb(token):
    m = morph.parse(token['content'])[0]
    return True if m.tag.POS == 'VERB' else False


# Существительное
def is_infn(token):
    m = morph.parse(token['content'])[0]
    return True if m.tag.POS == 'INFN' else False


# Существительное
def is_prtf(token):
    m = morph.parse(token['content'])[0]
    return True if m.tag.POS == 'PRTF' else False


# Существительное
def is_prts(token):
    m = morph.parse(token['content'])[0]
    return True if m.tag.POS == 'PRTS' else False


# Существительное
def is_grnd(token):
    m = morph.parse(token['content'])[0]
    return True if m.tag.POS == 'GRND' else False


# Существительное
def is_nmbr(token):
    m = morph.parse(token['content'])[0]
    return True if m.tag.POS == 'NUMR' else False


# Существительное
def is_advb(token):
    m = morph.parse(token['content'])[0]
    return True if m.tag.POS == 'ADVB' else False


# Существительное
def is_npro(token):
    m = morph.parse(token['content'])[0]
    return True if m.tag.POS == 'NPRO' else False


# Существительное
def is_pred(token):
    m = morph.parse(token['content'])[0]
    return True if m.tag.POS == 'PRED' else False


# Существительное
def is_prep(token):
    m = morph.parse(token['content'])[0]
    return True if m.tag.POS == 'PREP' else False


# Существительное
def is_conj(token):
    m = morph.parse(token['content'])[0]
    return True if m.tag.POS == 'CONJ' else False


# Существительное
def is_prcl(token):
    m = morph.parse(token['content'])[0]
    return True if m.tag.POS == 'PRCL' else False


# Существительное
def is_intj(token):
    m = morph.parse(token['content'])[0]
    return True if m.tag.POS == 'INTJ' else False


features = [is_adjf, is_adjs, is_advb, is_comp, is_conj, is_grnd, is_infn, is_intj, is_nmbr, is_noun, is_npro, is_prcl, is_pred, is_prep, is_prtf, is_prts, is_verb]