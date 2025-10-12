from Address import Address
from Mailing import Mailing

to_address = Address
from_address = Address
to_address = 660018, "г. Красноярск", "ул. Мира", 81, 1
from_address = 368844, "г. Краснодар", "ул. Лазо", 21, 8

sending = Mailing
sending(to_address, from_address, 1900, 1234560)

print(
    "Отправление",
    sending.track,
    "из",
    from_address,
    "в",
    to_address,
    ". Стоимость",
    sending.cost,
    "рублей.",
)