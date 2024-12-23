def calculate_love_score(name1, name2):
    
    check1 = ["T","R","U","E","t","r","u","e"]
    check2 = ["L","O","V","E","l","o","v","e"]
    
    count1 = 0
    count2 = 0
    
    for i in name1:
        if i in check1:
            count1 = count1 +1
            
            
    for i in name2:
        if i in check1:
            count1 = count1 +1
            
    for i in name1:
        if i in check2:
            count2 = count2 +1
            
            
    for i in name2:
        if i in check2:
            count2 = count2 +1
            
    print(f"{count1}{count2}")

name1 = "Habeeb"
name2 = "Jafer"

calculate_love_score(name1,name2)