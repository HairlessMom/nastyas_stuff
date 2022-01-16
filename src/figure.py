from abc import ABC, abstractmethod
from customexceptions import NotValidFigure


class Figure(ABC):
    NAME = "Unnamed Figure"

    @staticmethod
    def _float_number(side):
        try:
            float(side)
        except ValueError:
            raise TypeError
        else:
            return float(side)

    @abstractmethod
    def _is_valid(self):
        pass

    @abstractmethod
    def _get_perimeter(self):
        pass

    @abstractmethod
    def _get_area(self):
        pass

    def add_area(self, figure: object) -> float:
        return self.area + figure.area

    def __init__(self):
        self.area = self._get_area()
        self.perimeter = self._get_perimeter()