from classifier.max_ent import train_model, process_model


def process(text):
    res = process_model(text)
    return res


# train_model('../testset')
# process([[{'content': 'Я', 'tag': 3, 'position': 0, 'cls': '_'}, {'content': 'сегодня', 'tag': 3, 'position': 1, 'cls': '_'}, {'content': ',', 'tag': 3, 'position': 2, 'cls': '_'}, {'content': 'очень', 'tag': 3, 'position': 3, 'cls': '_'}, {'content': 'хорошо', 'tag': 3, 'position': 4, 'cls': '_'}, {'content': ',', 'tag': 3, 'position': 5, 'cls': '_'}, {'content': 'отлично', 'tag': 3, 'position': 6, 'cls': '_'}, {'content': 'хорощоооо', 'tag': 3, 'position': 7, 'cls': '_'}, {'content': 'покушал', 'tag': 3, 'position': 8, 'cls': '_'}, {'content': '!', 'tag': 3, 'position': 9, 'cls': '_'}], [{'content': ' ', 'tag': 3, 'position': 0, 'cls': '_'}, {'content': 'А', 'tag': 3, 'position': 1, 'cls': '_'}, {'content': 'еще', 'tag': 3, 'position': 2, 'cls': '_'}, {'content': 'кажется', 'tag': 3, 'position': 3, 'cls': '_'}, {'content': 'Владимир', 'tag': 0, 'position': 4, 'cls': '_'}, {'content': 'Владимирович', 'tag': 2, 'position': 5, 'cls': '_'}, {'content': 'сделал', 'tag': 3, 'position': 6, 'cls': '_'}, {'content': 'тоже', 'tag': 3, 'position': 7, 'cls': '_'}, {'content': 'самое', 'tag': 3, 'position': 8, 'cls': '_'}, {'content': '.', 'tag': 3, 'position': 9, 'cls': '_'}]])