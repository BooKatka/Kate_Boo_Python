
class Address:
    index = "000000"
    city = "name"
    street = "name"
    house_number = "00"
    flat = "00"
    def __init__(self, index, city, street, house_number, flat):
        self.index = index
        self.city= city
        self.street = street
        self.house = house_number
        self.flat = flat

    def __str__(self):
        return f"Индекс:{self.index}, Город - {self.city}, Улица -  {self.street}, дом - {self.house}, квартира -  {self.flat}"