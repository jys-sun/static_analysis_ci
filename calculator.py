def add(a, b):
    return a + b


def record(value, history=None):
    if history is None:
        history = []
    history.append(value)


def broken_total(x, y):
    return x * 7
