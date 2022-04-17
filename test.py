import requests
import pandas as pd

class Item:
    def __init__(self, id) -> None:
        self.id = id 
a = "https://universalis.app"
r = requests.get(f"{a}/api/history/brynhildr/36070?entries=50")
r.status_code

r.headers['content-type']

r.encoding

r.text

r.json()

print(r.json())



""" items = pd.read_csv("ffxiv-datamining/csv/Item.csv" ,header = 1 )

items = items.drop([0,2])

items["Level{Item}"] = items["Level{Item}"].astype("int16")
items = items.sort_values("Level{Item}", ascending = False)

endgame_items = items.loc[items["Level{Item}"] > 560 ]
endgame_items["IsUntradable"] = endgame_items["IsUntradable"].astype("boolean") 
endgame_items["CanBeHq"] = endgame_items["CanBeHq"].astype("boolean") 

endgame_items_marketable = endgame_items[~endgame_items["IsUntradable"]]
endgame_items_marketable = endgame_items_marketable[endgame_items["CanBeHq"]]
print(endgame_items_marketable.head())
endgame_items_marketable.to_csv("marketable", index = False) """