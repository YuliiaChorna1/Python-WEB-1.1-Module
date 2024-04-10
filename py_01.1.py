# SOLID: S - Single responsibility # принцип єдиної відповідальності


class PersonAddress:
    def __init__(self, zip, city, street) -> None:
        self.zip = zip
        self.city = city
        self.street = street
    
    def value_of(self):
        return f"{self.zip}, {self.city}, {self.street}"


class Person:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address

    def get_address(self):
        return self.address.value_of()


if __name__ == "__main__":

    
    person = Person("Alex", PersonAddress("36007", "Poltava", "European, 28"))
    print(person.get_address())