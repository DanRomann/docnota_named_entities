import pymorphy2


def is_first(token):
    return True if token.position == 0 else False


def is_lower(token):
    return token.content.islower()


def is_upper(token):
    return token.content.isupper()


def is_title(token):
    return token.content.istitle()


def is_digit(token):
    return token.content.isdigit()


features = [is_first, is_lower, is_upper, is_title, is_digit]
