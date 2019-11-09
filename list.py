shoplist=["apple","mango","carrot","banana"]

print("i have",len(shoplist),"items to purchase")

print("these items are : ", end=" ")

for item in shoplist:
    print(item,end="")

print("i also have to buy rice")
shoplist.append("rice")

print("my shoplist is",shoplist)

print("i will sort my shopping now")
shoplist.sort()
print("my  sorted shopping list is",shoplist)

print("the first item i will buy is",shoplist[0])
olditem=shoplist[0]

del shoplist[0]
print("i bought the",olditem)
print("my shopping list is now",shoplist)
