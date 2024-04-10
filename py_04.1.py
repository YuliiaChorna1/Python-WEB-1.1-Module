# SOLID: I - Interface segregation # принцип розділення інтерфейсу
# Сущности не должны зависеть от интерфейсов, которые они не используют


class CodeProducer:
    def write_code(self):
        pass


class PizzaConsumer:
    def eat_pizza(self, slice_count):
        pass


class OficceProgrammer(CodeProducer, PizzaConsumer):
    def __init__(self, name) -> None:
        self.name = name

    def eat_pizza(self, slice_count):
        print(f"{self.name}, eat {slice_count} pizza slice!")

    def write_code(self):
        print(f"{self.name}, write code!")


class RemoteProgrammer(CodeProducer):
    def __init__(self, name) -> None:
        self.name = name

    def write_code(self):
        print(f"{self.name}, write code!")