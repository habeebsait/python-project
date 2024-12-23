import pandas as pd

df = pd.read_csv('weather_data.csv')
print(type(df))

monday = df[df.day == "Monday"]
c_temp = monday.temp
f_temp = c_temp *9/5+32
print(f_temp)


dict1 = {
    "student" : ["HAbeeb", "Ameen","Praga"],
    "marks" : [12,13,14]
}

dict2 = pd.DataFrame(dict1)

print(dict2)

dict2.to_csv("new_data.csv")
