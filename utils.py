"""
This is utils which include common func
"""

PER_PAGE = 100


def get_header(config):
    """url header"""
    header = {}
    for (each_key, each_val) in config.items("headers"):
        header[each_key] = each_val
    return header


def get_param(page):
    """set basic params"""
    params = {}
    params["page"] = page
    params["per_page"] = PER_PAGE
    params["order"] = "desc"
    return params


def is_contains(value, str):
    """if value contains str"""
    value = value.lower()
    str = str.lower()
    return str in value


def is_start_with(value, str):
    """if value start with str"""
    value = value.lower()
    str = str.lower()
    return value.startswith(str)
