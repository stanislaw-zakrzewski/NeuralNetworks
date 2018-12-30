from math import e


def f_to_approximate(x: float):
    return x ** .5


def f_identity(x: float):
    return x


def fp_identity(x: float):
    return x / x if x != 0 else 1


def f_sigmoid(x: float):
    return 1 / (1 + e ** (-x))


def fp_sigmoid(x: float):
    return (e ** -x) / (((e ** (-x)) + 1) ** 2)
