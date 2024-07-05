import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate: int = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        if len(new_name) > 10:
            self._name = new_name[:10]
        else:
            self._name = new_name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, filename: str) -> None:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                price = cls.string_to_number(row['price'])
                quantity = cls.string_to_number(row['quantity'])
                item = cls(name, price, quantity)

    @staticmethod
    def string_to_number(value: str) -> float:
        try:
            return float(value)
        except ValueError:
            return 0.0

    def __repr__(self):
        return f"{self.__class__.__name__}('{self._name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self._name}'