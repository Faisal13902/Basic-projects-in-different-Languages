weight = input("Enter weight: ")

index = input("P for pound and K for kg ")

if index == "p":
    weight = float(weight) *.45
    print("Weight is ", weight)

elif index == "k":
    weight = float(weight) * 2.20
    print("Weight is ", weight)