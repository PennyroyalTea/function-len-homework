from typing import Callable


def dist(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def calculate_function_len_on_a_segment_with_n_steps(
        a: float,
        b: float,
        f: Callable[[float], float],
        n: int = 100000) -> float:
    """

    :param a: начало отрезка
    :param b: конец отрезка
    :param f: функция, длина которой должна быть вычислена
    :param n: количество отрезков, которыми функция приближается
    :return: длину функции на отрезке [a, b], приближенную n отрезками
    """

    # TODO: реализовать здесь код функции