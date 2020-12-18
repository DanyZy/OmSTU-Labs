# Определить иерархию классов напитков для бара. Должны быть как простые напитки,
# так и коктейли, состоящие из нескольких составляющих. Для каждого заказа напитков в баре
# реализовать отдельный расчёт стоимости алкогольных и безалкогольных напитков.

import unittest

"""Интерфейс напитков"""
class Beverage:

    def get_price(self):
        raise NotImplementedError

    def get_volume(self):
        raise NotImplementedError

    def is_alcohol(self):
        raise NotImplementedError


"""Класс заказа"""
class Order:

    """Конструктор заказа, volume в заказе - количество напитков.
       Стоимость алкогольных напитков повышена на 5% (отдельный расчет стоимости?)"""
    def __init__(self, *args: Beverage):
        self.volume = 0
        self.price = 0
        for el in args:
            self.volume += 1
            self.price += el.get_price() if not el.is_alcohol() else el.get_price() * 1.05

    """Геттеры заказа"""
    def get_price(self):
        return self.price

    def get_volume(self):
        return self.volume


"""Класс 'атомарного' напитка"""
class BaseDrink(Beverage):

    """Конструктор базового напитка, цена указывается за литр"""
    def __init__(self, price: float, volume: float, alcohol: bool = False):
        self.price = price
        self.volume = volume
        self.alcohol = alcohol

    """Геттеры базового напитка, цена зависит от объема"""
    def get_price(self):
        return self.price * self.volume

    def get_volume(self):
        return self.volume

    def is_alcohol(self):
        return self.alcohol


"""Класс коктейля"""
class Cocktail(Beverage):

    """Конструктор в качетве аргументов принимает базовые напитки"""
    def __init__(self, *args: BaseDrink):
        self.volume = 0
        self.price = 0
        self.alcohol = False
        for el in args:
            if el.is_alcohol():
                self.alcohol = True
            self.volume += el.get_volume()
            self.price += el.get_price()

    """Геттеры коктейля"""
    def get_price(self):
        return self.price

    def get_volume(self):
        return self.volume

    def is_alcohol(self):
        return self.alcohol


"""Юнит-тесты"""
class Tests(unittest.TestCase):

    """Тест функциональности класса базового напитка"""
    def test_base_brink(self):
        self.assertEqual(BaseDrink(100, 0.4).get_price(), 40)
        self.assertEqual(BaseDrink(73, 0.1).is_alcohol(), False)
        self.assertEqual(BaseDrink(15, 2, True).is_alcohol(), True)

    """Тест функциональности класса коктейля"""
    def test_cocktail(self):
        self.assertEqual(Cocktail(BaseDrink(35, 0.2), BaseDrink(120, 0.05, False), BaseDrink(50, 0.5)).get_price(), 38)
        self.assertEqual(Cocktail(BaseDrink(35, 0.2), BaseDrink(120, 0.05, True), BaseDrink(50, 0.5)).is_alcohol(), True)
        self.assertEqual(Cocktail(BaseDrink(35, 0.2), BaseDrink(120, 0.05, True), BaseDrink(50, 0.5)).get_volume(), 0.75)

    """Тест функциональности класса заказа
       assertAlmostEqual из-за неточных вычислений с плавающей точкой"""
    def test_order(self):
        self.assertAlmostEqual(Order(Cocktail(BaseDrink(35, 0.2), BaseDrink(120, 0.05, False), BaseDrink(50, 0.5)),
                               Cocktail(BaseDrink(10, 2), BaseDrink(60, 0.6, True)),
                               BaseDrink(15, 0.1)).get_price(), 98.3)
        self.assertEqual(Order(Cocktail(BaseDrink(35, 0.2), BaseDrink(120, 0.05, False), BaseDrink(50, 0.5)),
                               Cocktail(BaseDrink(10, 2), BaseDrink(60, 0.6, True)),
                               BaseDrink(15, 0.1)).get_volume(), 3)


if __name__ == '__main__':
    unittest.main()
