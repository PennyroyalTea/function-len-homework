from main.main import calculate_function_len_on_a_segment_with_n_steps as func_len
from main.functions import f_linear, f_sqrt, f_sine, f_square


def eq_approx(a: float, b: float) -> bool:
    """
    Проверим равенство двух дробных чисел (с учетом погрешности)
    :param a: первое число
    :param b: второе число
    :return: равны ли два дробных числа
    """
    return abs(a - b) < 0.001


def test_linear():
    # проверим, что у линейной функции длина на разных участках одинаковая
    assert eq_approx(
        func_len(-200, -100, f_linear),
        func_len(0, 100, f_linear)
    )

    # проверим, что длина линейной функции от 0 до 1 это корень из 2
    assert eq_approx(
        func_len(0, 1, f_linear),
        2 ** 0.5
    )


def test_sqrt():
    # проверим длину функции y = корень(x) от 0 до 1
    assert eq_approx(
        func_len(0, 1, f_sqrt),
        1.47894
    )


def test_square():
    # x^2 — симметричная функция, поэтому длина от 0 до -x такая же как от 0 до x (для любого x!)
    assert eq_approx(
        func_len(-3.745, 0, f_square),
        func_len(0, 3.745, f_square)
    )

    # ну и проверим конкретное значение
    assert eq_approx(
        func_len(1, 5, f_square),
        24.395301
    )


def test_sine():
    # проверим численное значение y = sin(x) от 10 до 12
    assert eq_approx(
        func_len(10, 12, f_sine),
        2.24778
    )