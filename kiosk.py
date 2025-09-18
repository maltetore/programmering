gold = 200
print("welcome to my shop. do you wish to buy or sell things?")
if input() == "sell":
    print("what do you want to sell?")
    itemname = input()
    print(f"how much do you want to sell {itemname} for?")
    itemprice = input()
    itemprice = int(itemprice)

    print("deal.")
    gold = gold + itemprice
    print(f"you have {gold} gold. please buy something")

print("do you what do you want to buy?")

item = input()
if item == "ice":
    item = 30
elif item == "hotdog":
    item = 15
elif item == "soda":
    item = 15
elif item == "candy":
    item = 10
else:
    print("we dont have that")
    quit()


print("how many")
ammount = input()
ammount = int(ammount)

print(f"that will be {item * ammount}")
print("pay")
if input() == "yes":
    gold = (item * ammount) - gold
    print("thanks")
elif input() == "no":
    print("no items for you")
    quit()
else:
    print("in english, please.")
print(gold)
quit()


