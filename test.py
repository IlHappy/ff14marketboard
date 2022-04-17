import requests
import pandas as pd

#querying universalis endpoint
base_url = "https://universalis.app"
sales_history = requests.get(f"{base_url}/api/history/brynhildr/36070?entries=50")
print(sales_history.json())

#read item data from mining repo https://github.com/xivapi/ffxiv-datamining
items = pd.read_csv("ffxiv-datamining/csv/Item.csv", header=1) 
items = items.drop([0,2])

#sorting for only endgame items
items["Level{Item}"] = items["Level{Item}"].astype("int16")
items = items.sort_values("Level{Item}", ascending = False)
endgame_items = items.loc[items["Level{Item}"] > 560 ]

#filtering to only tradable items
endgame_items["IsUntradable"] = endgame_items["IsUntradable"].astype("boolean") 
endgame_items["CanBeHq"] = endgame_items["CanBeHq"].astype("boolean") 
endgame_items_marketable = endgame_items[~endgame_items["IsUntradable"]]
endgame_items_marketable = endgame_items_marketable[endgame_items["CanBeHq"]]

#output
print(endgame_items_marketable.head())
endgame_items_marketable.to_csv("marketable", index = False)
