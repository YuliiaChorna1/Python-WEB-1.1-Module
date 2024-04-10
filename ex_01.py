# SOLID: S - Single responsibility # принцип єдиної відповідальності


class ValidPhoneNumber(Exception):
    pass


class PersonInfo:
    def value_of(self):
        raise NotImplementedError


class PersonPhoneNumber(PersonInfo):
    def __init__(self, phone: str, operator_code: str) -> None:
        self.phone = phone
        self.operator_code = operator_code
        if operator_code != "050":
            raise ValidPhoneNumber
        
    def value_of(self):
        return f"+380({self.operator_code}){self.phone}"


class PersonAddress(PersonInfo):
    def __init__(self, zip, city, street) -> None:
        self.zip = zip
        self.city = city
        self.street = street

    def value_of(self):
        return f"{self.zip}, {self.city}, {self.street}"
    
    
class Person:
    def __init__(self, name: str, phone: PersonPhoneNumber, address: PersonAddress) -> None:
        self.name = name
        self.phone = phone
        self.address = address

    def get_phone_number(self):
        return f"{self.name}: {self.phone.value_of()}"
    
    def get_address(self):
        return f"{self.name}: {self.address.value_of()}"
    

if __name__ == "__main__":
    phone = PersonPhoneNumber("9995555", "050")
    address = PersonAddress("49086", "Dnipro", "Abaya 40")
    person = Person("Alex", phone, address)
    print(person.get_phone_number())
    print(person.get_address())