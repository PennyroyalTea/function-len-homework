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
    distance_btw_points = (b -a)/n
    main_distance_x = a
    function_distance = 0
    for i in range(1,n+1):
        cordA = [main_distance_x,f(main_distance_x)]
        cordB = [main_distance_x + distance_btw_points,f(main_distance_x + distance_btw_points)]
        main_distance_x += distance_btw_points
        function_distance += dist(cordA,cordB)
    return function_distance
