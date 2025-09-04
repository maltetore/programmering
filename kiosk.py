print("what will it be, traveler?")


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


print("how many")
ammount = input()
ammount = int(ammount)

print(f"that is worth {item * ammount}")



