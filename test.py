import pymorphy2

morph = pymorphy2.MorphAnalyzer()

analyze = morph.parse('Украина')
print(analyze)