x=50
def func():
    global x
    print("x is still",x)
    x=2
    print("changed global x to",x)

func()
print("x is still",x)
