import requests
import matplotlib as mpl
import matplotlib.pyplot as plt
import json
import pandas as pd

#general parameters
WORLD_NAME = "brynhildr"
base_url = "https://universalis.app"

def query_sales_with_item_list(world, itemList, entriesNumber):
    itemIds = ""
    for i in itemList:
        itemIds += f"{i}," 
    #querying universalis endpoint
    sales_history = requests.get(f"{base_url}/api/history/{WORLD_NAME}/{itemIds}?entries={entriesNumber}")

    return sales_history.json()

def get_endgame_items():
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
    return endgame_items_marketable


itemList = ["36070", "35057"]
sales = query_sales_with_item_list(WORLD_NAME, itemList, 50)
histo = sales["items"][0]["stackSizeHistogram"]

plt.bar(range(len(histo)), list(histo.values()), align="center")
plt.xticks(range(len(histo)), list(histo.keys()))

plt.show()
