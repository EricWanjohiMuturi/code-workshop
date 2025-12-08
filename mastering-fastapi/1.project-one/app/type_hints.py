from typing import Any

text: str = "value"
percent: int = 90
temp: float = 9.3
numbers:int | float = 12
digits: list[int] = [1,2,3,4,5]
table_5:tuple[int, ...] = (1,2,3,4,5)
city_temp : tuple[str, float] = ("City", 20.5)
shipment: dict[str,str | int]={
    "id" : 12701,
    "content" : "wooden table",
    "status" : "in transit",
}

shipment2: dict[str,Any]={
    "id" : 12701,
    "weight" : 23.5,
    "content" : "wooden table",
    "status" : "in transit",
}


