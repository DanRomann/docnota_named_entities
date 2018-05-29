def is_lower(content):
    return content.islower()


def is_upper(content):
    return content.isupper()


def is_title(content):
    return content.istitle()


def is_digit(content):
    return content.isdigit()


features = [is_lower, is_upper, is_title, is_digit]