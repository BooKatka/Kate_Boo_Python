from smartphon  import Smartphone

Catalog = [Smartphone ("Apple", "16 Pro", "+7 902-929-29-29"),
    Smartphone("Sumsung", "120 max", "+7 902-929-29-20"),
    Smartphone("MI", "12", "+7 902-950-29-21"),
    Smartphone("Readme", "9 S", "+7 902-929-29-00"),
    Smartphone("Nokia", "3310", "+7 902-929-29-10")
]
for phone in Catalog:
    print(f"{phone.brand}-{phone.model}, {phone.number}")

