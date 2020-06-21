# Import Pickle
import pickle

# Create New List
def newList(ListName, FileName, ListItems):
    ListName = ListItems
    pickle.dump(ListName, open(FileName, "wb"))
    return ListItems

# Save Current List
def saveList(ListName, FileName):
    pickle.dump(ListName, open(FileName, "wb"))

# Load Current List
def loadList(FileName):
   return pickle.load(open(FileName, "rb"))

# Add To List
def addList(ListName, NewItem):
    ListName.append(NewItem)

# Remove To List
def delList(ListName, DelList):
    ListName.remove(DelList)

# Print List
def printList(ListName):
    for x in ListName:
      print(x)
    print("----------")
