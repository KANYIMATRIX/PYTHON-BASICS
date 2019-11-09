number=23
guess=int(input("enter an integer : "))

if guess==number:
    print("congrats")

elif guess<number:
    print("number is a bit higher than that")

else:
    print("number is lower than that")

print("done")
