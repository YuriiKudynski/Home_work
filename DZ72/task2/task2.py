import matplotlib.pyplot as plt
from abc import ABC, abstractmethod

# Абстрактний метод продукту


class Chart(ABC):

    @abstractmethod
    def draw(self):
        pass

# Конкретні класи продуктів


class LineChart(Chart):
    def draw(self):
        plt.plot([1, 2, 3, 4], [10, 20, 25, 5], color="red")
        plt.ylabel("some numbers")


class BarChart(Chart):
    def draw(self):
        plt.bar([1, 2, 3, 4], [10, 20, 25, 5])
        plt.ylabel("some number")


class ChartFactory(ABC):
    @abstractmethod
    def create_chart(self):
        pass

    def draw_chart(self):
        chart = self.create_chart()
        chart.draw()
        # plt.show()


class LineChartFactory(ChartFactory):

    def create_chart(self):
        return LineChart()


class BarChartFactory(ChartFactory):

    def create_chart(self):
        return BarChart()


class Client:
    def __init__(self,factory):
        self.factory = factory

    def draw_char(self):
        self.factory.draw_chart()


if __name__ == '__main__':

    line_factory = Client(LineChartFactory())
    line_factory.draw_char()

    bar_factory = Client(BarChartFactory())
    bar_factory.draw_char()
    plt.show()