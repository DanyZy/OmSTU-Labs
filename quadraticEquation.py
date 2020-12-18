# Определить класс Квадратное уравнение. Реализовать методы для поиска корней, экстремумов,
# а также интервалов убывания/возрастания. Создать массив/список/множество объектов
# и определить наибольшие и наименьшие по значению корни.

import math
import unittest


class QuadraticEquation:

    """Конструктор класса, при инициализации объекта вызывает свои приватные методы:
       рассчет корней, рассчет экстремума функции, рассчет интервалов возрастания и убывания."""
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__roots = self.__calculate_roots()
        self.__extr = self.__calculate_extremum()
        self.__inc_interval = self.__calculate_intervals()[0]
        self.__dec_interval = self.__calculate_intervals()[1]

    """Рассчет корней уравнения"""
    def __calculate_roots(self):
        if self.__a != 0:
            dis = self.__b ** 2 - 4 * self.__a * self.__c
            if dis > 0:
                x1 = (-self.__b + math.sqrt(dis)) / (2 * self.__a)
                x2 = (-self.__b - math.sqrt(dis)) / (2 * self.__a)
                return x1, x2
            elif dis == 0:
                x3 = -self.__b / (2 * self.__a)
                return x3
            else:
                return None

    """Рассчет экстремума квадратичной функции"""
    def __calculate_extremum(self):
        x = -self.__b / (2 * self.__a)
        y = self.__a * (x ** 2) + self.__b * x + self.__c
        return x, y

    """Получение интервалов возрастания и убывания через точку экстремума"""
    def __calculate_intervals(self):
        inc = None
        dec = None
        if self.__a != 0:
            inc = (-math.inf, self.__calculate_extremum()) if self.__a < 0 else (self.__calculate_extremum(), math.inf)
            dec = (-math.inf, self.__calculate_extremum()) if self.__a > 0 else (self.__calculate_extremum(), math.inf)
        return inc, dec

    """ToString() объекта"""
    def __str__(self):
        return "Roots: {}\nExtremum: {}\nIncreasing interval: {}\nDecreasing interval: {}".format(
            self, self.get_roots(), self.get_extremum(), self.get_inc_interval(), self.get_dec_interval())

    """Геттеры"""
    def get_roots(self):
        return self.__roots

    def get_extremum(self):
        return self.__extr

    def get_inc_interval(self):
        return self.__inc_interval

    def get_dec_interval(self):
        return self.__dec_interval


"""Функция получения максимального значения корня уравнения из набора объектов типа QuadraticEquation"""
def get_max_roots(*equations: QuadraticEquation):
    root_list = []
    for eq in equations:
        try:
            root_list.append(max(eq.get_roots()))
        except TypeError:
            if eq.get_roots() is None:
                continue
            else:
                root_list.append(eq.get_roots())
    return max(root_list)


"""Функция получения минимального значения корня уравнения из набора объектов типа QuadraticEquation"""
def get_min_roots(*equations: QuadraticEquation):
    root_list = []
    for eq in equations:
        try:
            root_list.append(min(eq.get_roots()))
        except TypeError:
            if eq.get_roots() is None:
                continue
            else:
                root_list.append(eq.get_roots())
    return min(root_list)


"""Юнит-тесты"""
class Tests(unittest.TestCase):

    """Тесты рассчета корней уровнения"""
    def test_roots_1(self):
        self.assertTupleEqual(QuadraticEquation(1, 0, -1).get_roots(), (1, -1))

    def test_roots_2(self):
        self.assertEqual(QuadraticEquation(1, 0, 2).get_roots(), None)

    def test_roots_3(self):
        self.assertEqual(QuadraticEquation(1, 0, 0).get_roots(), 0)

    def test_roots_4(self):
        self.assertTupleEqual(QuadraticEquation(1, 1, -2).get_roots(), (1, -2))

    def test_roots_5(self):
        self.assertTupleEqual(QuadraticEquation(2, 4, 0).get_roots(), (0, -2))

    """Тесты рассчета экстремумов квадратичный функции"""
    def test_extremum_1(self):
        self.assertTupleEqual(QuadraticEquation(1, 0, -1).get_extremum(), (0, -1))

    def test_extremum_2(self):
        self.assertTupleEqual(QuadraticEquation(1, 0, 2).get_extremum(), (0, 2))

    def test_extremum_3(self):
        self.assertTupleEqual(QuadraticEquation(1, 0, 0).get_extremum(), (0, 0))

    """Тесты получения интервалов возрастания и убывания функции"""
    def test_interval_1(self):
        self.assertTupleEqual(QuadraticEquation(1, 0, -1).get_inc_interval(), ((0, -1), math.inf))
        self.assertTupleEqual(QuadraticEquation(1, 0, -1).get_dec_interval(), (-math.inf, (0, -1)))

    def test_interval_2(self):
        self.assertTupleEqual(QuadraticEquation(1, 0, 2).get_inc_interval(), ((0, 2), math.inf))
        self.assertTupleEqual(QuadraticEquation(1, 0, 2).get_dec_interval(), (-math.inf, (0, 2)))

    def test_interval_3(self):
        self.assertTupleEqual(QuadraticEquation(1, 0, 0).get_inc_interval(), ((0, 0), math.inf))
        self.assertTupleEqual(QuadraticEquation(1, 0, 0).get_dec_interval(), (-math.inf, (0, 0)))

    def test_interval_4(self):
        self.assertTupleEqual(QuadraticEquation(-1, 0, 2).get_inc_interval(), (-math.inf, (0, 2)))
        self.assertTupleEqual(QuadraticEquation(-1, 0, 2).get_dec_interval(), ((0, 2), math.inf))

    """Тесты получения максимального значения корня из набора уравнений"""
    def test_max_root(self):
        self.assertEqual(get_max_roots(QuadraticEquation(1, 0, -1), QuadraticEquation(2, 4, 0)), 1)
        self.assertEqual(get_max_roots(QuadraticEquation(1, 1, -2), QuadraticEquation(1, 0, 2)), 1)
        self.assertEqual(get_max_roots(QuadraticEquation(1, 0, -1), QuadraticEquation(1, 0, 0), QuadraticEquation(1, 0, 2)), 1)

    """Тесты получения минимального значения корня из набора уравнений"""
    def test_min_root(self):
        self.assertEqual(get_min_roots(QuadraticEquation(1, 0, -1), QuadraticEquation(2, 4, 0)), -2)
        self.assertEqual(get_min_roots(QuadraticEquation(1, 1, -2), QuadraticEquation(1, 0, 2)), -2)
        self.assertEqual(get_min_roots(QuadraticEquation(1, 0, -1), QuadraticEquation(1, 0, 0), QuadraticEquation(1, 0, 2)), -1)


if __name__ == '__main__':
    unittest.main()
