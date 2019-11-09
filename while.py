number=22
running = True
while running:
    guess=int(input("enter an integer : "))

    if guess==number:
        print("got it")
        running = False

    elif guess<number:
        print("number is higher than that")

    else:
        print("number is lower than that")


print("done")
