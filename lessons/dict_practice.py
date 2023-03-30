"""practice with dictionaries"""

ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}

#adding
ice_cream["mint"] = 3
print("After adding mint:")
print(ice_cream)

#removing
ice_cream.pop("mint")
print("after removing mint:")
print(ice_cream)