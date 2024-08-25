auction = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\\
'''

print(auction)
bids = {}

continue_bid = True

while continue_bid:
    name = input("Enter user name: ")
    bid_amount = int(input("Enter the bid amount: $"))

    bids[name] = bid_amount
    print("\n" * 1000)
    check = input("Do you want to add more bidders? (yes/no): ").lower()
    print("\n"*1000)
    if check == 'no':
        continue_bid = False
name = ""
max = 0
for i in bids:
    if bids[i] > max:
        name = i
        max = bids[i]

print(f"THe highest bidder is {name} with amount {max}")
