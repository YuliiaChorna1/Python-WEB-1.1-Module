class Animal:
    def __init__(self, nickname, age) -> None:
        self.nickname = nickname
        self.age = age

    def get_info(self):
        return f"It's an animal. Its name is {self.nickname} and it's {self.age} years old"
    

class Owner:
    def __init__(self, name, phone) -> None:
        self.name = name
        self.phone = phone

    def get_info(self):
        return f"{self.name} - {self.phone}"


class Cat(Animal):
    def __init__(self, nickname, age, name, phone) -> None:
        super().__init__(nickname, age)
        self.owner = Owner(name, phone)

    def sound(self):
        return f"{self.nickname} say meow!"
    

if __name__ == "__main__":
    cat = Cat("Boris", 4, "Denys", "05000119221")
    print(cat.owner.get_info)