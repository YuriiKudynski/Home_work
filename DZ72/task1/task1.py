from abc import ABC, abstractmethod


class Computer:

    def __init__(self):
        self.processor = None
        self.memory = None
        self.storage = None
        self.graphics_card = None
        self.operating_system = None

    def __str__(self):
        return f"""
                   Processor: {self.processor}
                   Memory: {self.memory}
                   Storage: {self.storage}
                   Graphics card: {self.graphics_card}
                   Operating system: {self.operating_system}"""


class Builder(ABC):

    def __init__(self):
        self.computer = Computer()

    def get_computer(self) -> Computer:
        # reset and get
        comp = self.computer
        self.computer = Computer()
        return comp

    @abstractmethod
    def add_processor(self, processor):
        pass

    @abstractmethod
    def add_memory(self, memory):
        pass

    @abstractmethod
    def add_storage(self, storage):
        pass

    @abstractmethod
    def add_graphics_card(self, graphics_card):
        pass

    @abstractmethod
    def add_operating_system(self, operating_system):
        pass


class ComputerBuilder(Builder):

    def add_processor(self, processor):
        self.computer.processor = processor

    def add_memory(self, memory):
        self.computer.memory = memory

    def add_storage(self, storage):
        self.computer.storage = storage

    def add_graphics_card(self, graphics_card):
        self.computer.graphics_card = graphics_card

    def add_operating_system(self, operating_system):
        self.computer.operating_system = operating_system


class Director:

    def __init__(self, builder: Builder) -> None:
        self.builder = builder

    def builder_minimal_computer(self, specs: dict) -> None:
        self.builder.add_processor(specs['processor'])
        self.builder.add_memory(specs['memory'])
        self.builder.add_storage(specs['storage'])
        self.builder.add_graphics_card(specs['graphics_card'])

    def builder_full_computer(self, specs: dict) -> None:
        self.builder_minimal_computer(specs)
        self.builder.add_operating_system(specs['operating_system'])


specs_full = {
    'processor': 'Intel Core i5',
    'memory': '8GB',
    'storage': '512GB SSD',
    'graphics_card': 'Integrated',
    'operating_system': 'Windows 11',
}

specs_min = {
    'processor': 'Intel Core i5',
    'memory': '8GB',
    'storage': '512GB SSD',
    'graphics_card': 'Integrated'
}


if __name__ == "__main__":
    comp_builder = ComputerBuilder()
    comp_director = Director(comp_builder)

    comp_director.builder_minimal_computer(specs_min)
    computer_1 = comp_builder.get_computer()

    comp_director.builder_full_computer(specs_full)
    computer_2 = comp_builder.get_computer()

    print("Minimal computer", computer_1)
    print("Full complication computer", computer_2)