#biljet 1-14 barnbiljet blijet 15 - 20 ungdomsbiljet <20 biljet 65+ seniorbiljet
print("hur gammal är du?")
age = input()
age = int(age)
if age <= 15:
    print("barnbiljet")
elif age <= 20:
    print("ungdomsbiljet")
elif age < 20 and age > 65:
    print("biljet")
else:
    print("seniorbiljet")
    