from math import e


def f_identity(x: float):
    return x


def fp_identity(x: float):
    return x/x if x != 0 else 1


def f_sigmoid(x: float):
    return 1 / (1 + e ** (-x))


def fp_sigmoid(x: float):
    return (e ** -x) / (((e ** (-x)) + 1) ** 2)


def substract_array(a, b):
    return [i - j for i, j in zip(a, b)]
