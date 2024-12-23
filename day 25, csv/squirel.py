import pandas as pd

df = pd.read_csv("day 25, csv/2018_Central_Park.csv")
gray = df[df["Primary Fur Color"] == "Gray"]
white = df[df["Primary Fur Color"] == "Black"]
cinnamon = df[df["Primary Fur Color"] == "Cinnamon"]

gray_count = gray["Primary Fur Color"].count()
cinnamon_count = (cinnamon["Primary Fur Color"].count())
white_count = (white["Primary Fur Color"].count())

dict = {"Fur Color": ["gray", "red", "white"],
        "count" : [gray_count, cinnamon_count, white_count]}

dictpd = pd.DataFrame(dict)

dictpd.to_csv("day 25, csv/squirrel_count")