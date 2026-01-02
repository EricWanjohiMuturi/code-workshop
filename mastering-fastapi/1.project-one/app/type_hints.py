from typing import Any

text:str = "value"
pert:int = 90
temp:float = 25.5
is_active:bool = True
number:int|float = 12

optional: str|None

optional = "Hello"

digits:list[int] = [1, 2, 3, 4, 5]

table:tuple[int, ...] = (1,2,3,5,6,7,8)

city_temp:tuple[str, float] = ("New York", 29.5 )

productA:dict[str, Any] = {
    "id": 1,
    "name": "Item A",
    "price": 29.99
}

shipments:dict[str, int|str] = {
    "id": 1,
    "name": "Item A",
    "status": "shipped"
}

def root(num:int|float, exp:float|None=.5) -> float:
    return pow(num, .5)

root_25:float = root(25)

#using custom classes as type hints
class City:
    def __init__(self, name, location):
        self.name = name
        self.location = location

kiambu = City("Kiambu", "USA")

city_tempA:tuple[City, float] = (kiambu, 29.5 )