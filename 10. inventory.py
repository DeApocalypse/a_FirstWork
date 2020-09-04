#inventory.py

stuff={"rope":1,"torch":6,"gold coin":42,"dagger":1,"arrow":12}

def displayInventory(inventory):
    print("Inventory:")
    item_total=0
    for k,v in inventory.items():
        print(str(v)+" "+k)
        item_total+=v
    print("Total number of items: "+str(item_total))

displayInventory(stuff)

i=0
while i==0:
    try:
        nextStep=int(input("Enter 1 to continue, 0 to exit...>> "))
        if nextStep==1:
            i=1
        elif nextStep==0:
            print("Exit...")
            break
        else:
            raise KeyError
    except:
        print("Enter 0 or 1!")

def addToInventory(inventory,addedItems):
    for k in dragonLoot:
        if k in inventory:
            inventory[k]+=1
        else:
            inventory.setdefault(k,1)

inv={"gold coin":42,"rope":1}
dragonLoot=["gold coin","dagger","gold coin","gold coin","rubby"]
addToInventory(inv,dragonLoot)
displayInventory(inv)
