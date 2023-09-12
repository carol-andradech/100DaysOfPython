logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
finished = False
bid_dictionary = {}
print(f"{logo}")


def find_bid(bids):
    win = 0
    aux = 0
    name = ""
    for key in bids:
        if bids[key] > win:
            aux = bids[key]
            win = aux
            name = key

    print(f"The Winner is {name} with the bid of ${win:.2f}")


while not finished:
    name = input("What's your name?: ")
    bid = float(input("What's your bid?: "))
    bid_dictionary[name] = bid
    check = input("Are there another bidders? Type 'yes' or 'no': ")
    if check == "no":
        finished = True
        find_bid(bid_dictionary)
