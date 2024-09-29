import pandas as pd
dict1 = {
    "student" : ["HAbeeb", "Ameen","Praga"],
    "marks" : [12,13,14]
}

dict2 = pd.DataFrame(dict1)

print(dict2)

dict2.to_csv("new_data.csv")
