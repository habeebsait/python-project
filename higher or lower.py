import random

users = [
    {"name": "Alice Johnson", "follower_count": 123456, "description": "A passionate writer", "country": "United States"},
    {"name": "Bob Smith", "follower_count": 234567, "description": "A talented artist", "country": "Canada"},
    {"name": "Charlie Brown", "follower_count": 345678, "description": "A skilled musician", "country": "Australia"},
    {"name": "David Lee", "follower_count": 456789, "description": "A successful entrepreneur", "country": "China"},
    {"name": "Emily Taylor", "follower_count": 567890, "description": "A dedicated scientist", "country": "Japan"},
    {"name": "Frank Williams", "follower_count": 678901, "description": "A passionate gamer", "country": "Germany"},
    {"name": "Grace Miller", "follower_count": 789012, "description": "A talented dancer", "country": "France"},
    {"name": "Henry Davis", "follower_count": 890123, "description": "A skilled athlete", "country": "United Kingdom"},
    {"name": "Isabella Clark", "follower_count": 901234, "description": "A passionate photographer", "country": "Italy"},
    {"name": "Jack Brown", "follower_count": 1012345, "description": "A dedicated volunteer", "country": "Spain"},
    {"name": "Kate Wilson", "follower_count": 1112345, "description": "A talented chef", "country": "Brazil"},
    {"name": "Liam Johnson", "follower_count": 1212345, "description": "A successful actor", "country": "Russia"},
    {"name": "Mia Smith", "follower_count": 1312345, "description": "A passionate blogger", "country": "India"},
    {"name": "Noah Miller", "follower_count": 1412345, "description": "A skilled engineer", "country": "Mexico"},
    {"name": "Olivia Davis", "follower_count": 1512345, "description": "A dedicated teacher", "country": "Argentina"},
    {"name": "Paul Clark", "follower_count": 1612345, "description": "A talented musician", "country": "South Africa"},
    {"name": "Quinn Brown", "follower_count": 1712345, "description": "A passionate gamer", "country": "Australia"},
    {"name": "Riley Wilson", "follower_count": 1812345, "description": "A skilled athlete", "country": "Canada"},
    {"name": "Sophia Johnson", "follower_count": 1912345, "description": "A successful entrepreneur", "country": "China"},
    {"name": "Thomas Smith", "follower_count": 2012345, "description": "A dedicated scientist", "country": "Japan"},
    {"name": "Uma Miller", "follower_count": 2112345, "description": "A passionate dancer", "country": "Germany"},
    {"name": "Vincent Davis", "follower_count": 2212345, "description": "A talented chef", "country": "France"},
    {"name": "William Clark", "follower_count": 2312345, "description": "A successful actor", "country": "United Kingdom"},
    {"name": "Xavier Brown", "follower_count": 2412345, "description": "A dedicated volunteer", "country": "Italy"},
    {"name": "Yara Wilson", "follower_count": 2512345, "description": "A skilled engineer", "country": "Spain"},
    {"name": "Zara Johnson", "follower_count": 2612345, "description": "A passionate photographer", "country": "Brazil"},
    {"name": "Aaron Smith", "follower_count": 2712345, "description": "A talented musician", "country": "Russia"},
    {"name": "Beth Miller", "follower_count": 2812345, "description": "A successful entrepreneur", "country": "India"},
    {"name": "Caleb Davis", "follower_count": 2912345, "description": "A dedicated scientist", "country": "Mexico"},
    {"name": "Daniela Clark", "follower_count": 3012345, "description": "A passionate dancer", "country": "Argentina"},
    {"name": "Elijah Brown", "follower_count": 3112345, "description": "A skilled athlete", "country": "South Africa"},
    {"name": "Fiona Wilson", "follower_count": 3212345, "description": "A successful actor", "country": "Australia"},
    {"name": "Gabriel Johnson", "follower_count": 3312345, "description": "A dedicated volunteer", "country": "Canada"},
    {"name": "Hannah Smith", "follower_count": 3412345, "description": "A talented chef", "country": "China"},
    {"name": "Isaac Miller", "follower_count": 3512345, "description": "A passionate gamer", "country": "Japan"},
    {"name": "Jasmine Davis", "follower_count": 3612345, "description": "A skilled engineer", "country": "Germany"},
    {"name": "Kevin Clark", "follower_count": 3712345, "description": "A successful entrepreneur", "country": "France"},
    {"name": "Laura Brown", "follower_count": 3812345, "description": "A dedicated scientist", "country": "United Kingdom"},
    {"name": "Mason Wilson", "follower_count": 3912345, "description": "A passionate dancer", "country": "Italy"},
    {"name": "Nora Johnson", "follower_count": 4012345, "description": "A talented chef", "country": "Spain"},
    {"name": "Oliver Smith", "follower_count": 4112345, "description": "A successful actor", "country": "Brazil"},
    {"name": "Penelope Miller", "follower_count": 4212345, "description": "A dedicated volunteer", "country": "Russia"},
    {"name": "Quentin Davis", "follower_count": 4312345, "description": "A skilled engineer", "country": "India"},
    {"name": "Riley Clark", "follower_count": 4412345, "description": "A passionate photographer", "country": "Mexico"},
    {"name": "Sarah Brown", "follower_count": 4512345, "description": "A talented musician", "country": "Argentina"},
    {"name": "Thomas Wilson", "follower_count": 4612345, "description": "A successful entrepreneur", "country": "South Africa"},
    {"name": "Uma Johnson", "follower_count": 4712345, "description": "A dedicated scientist", "country": "Australia"},
    {"name": "Vincent Smith", "follower_count": 4812345, "description": "A passionate dancer", "country": "Canada"},
    {"name": "William Miller", "follower_count": 4912345, "description": "A talented chef", "country": "China"},
    {"name": "Xavier Davis", "follower_count": 5012345, "description": "A successful actor", "country": "Japan"},
    {"name": "Yara Clark", "follower_count": 5112345, "description": "A dedicated volunteer", "country": "Germany"},
    {"name": "Zara Brown", "follower_count": 5212345, "description": "A skilled engineer", "country": "France"},
    {"name": "Aaron Wilson", "follower_count": 5312345, "description": "A passionate photographer", "country": "United Kingdom"},
    {"name": "Beth Johnson", "follower_count": 5412345, "description": "A talented musician", "country": "Italy"}
]



guess = True
count = 0
while guess:
    print(f"\n\n\nNUMBER OF RIGHT GUESSES: {count}")
    choice1 = random.randint(0,63)
    A = users[choice1]["follower_count"]
    print("\n\n**************** First Member *****************\n")
    print("Name: ", end = "")
    print(users[choice1]["name"], end = ", ")
    print("Description: ", end = "")
    print(users[choice1]["description"],end = ", ")
    print("Country: ",end = "")
    print(users[choice1]["country"])

    print("\n\n")

    choice2 = random.randint(0,63)
    B = users[choice2]["follower_count"]
    print("\n**************** Second Member *****************\n")
    print("Name: ", end = "")
    print(users[choice2]["name"], end = ", ")
    print("Description: ", end = "")
    print(users[choice2]["description"],end = ", ")
    print("Country: ",end = "")
    print(users[choice2]["country"],end ="\n\n")

    choice = input("Enter your choice: (A / B): ")
    if A>B:
        if choice == "A":
            count = count + 1
        else:
            break

    elif B>A:
        if choice == "B":
            count = count + 1

        else:
            break
    
    else:
        print("********!!!!!!ERROR!!!!!!*****")

print(f"Your score is {count}")