**PyData** is a Python module making the use the pickle library easier.

### Creating a New List
Let's make a new list using this. Use the `newList()` function to do it such.

```py
Movies = newList("Movies", "Movies.dat", ["Jurrasic Park", "Stuart Little", "Back to the Future"])
```

#### Saving List to Existing File
Let's say, I want to change the variable and save to an existing file, it's still possible.

```py
Movies[2] = "Ready Player One"

saveList(Movies, "Movies.dat")
```

#### Loading Existing File to List
Okay, so what happens if you make a change to variable, and want to roll back? Don't worry!
```py
Movies[2] = "Ready Player Two"

Movies = loadList("Movies.dat")
```

#### Adding More to a List
So, I want to keep both **Ready Player One** and **Back to the Future**, while not hurting **Jurrasic Park** and **Stuart Little**, don't worry, you can keep all four.
```py
addList(Movies, "Back to the Future")
```
#### Removing From List
What happens if you want to remove an item from list, let's say, that **Stuart Little** doesn't fit with the other films by genre. We can get rid of the item.
```py
delList(Movies, "Stuart Little")
```
#### Printing All Items
So, I want to see all the items in the list? Don't worry, you can!
```py
printList(Movies)
```
### Go Bananas!
Don't worry if you can't make muiltple files, you can! Just go bananas.
```py
Stephens = newList("Stephens", "Stephens.dat", ["Stephen King", "Stephen Hawking", "Stephen Fry"])
Detectives = newList("Detectives", "Detectives.dat", ["Sherlock", "Connor", "Auguste"])
BestBurgers = newList("BestBurgers", "BestBurgers.dat", ["Freddy's Steakburgers", "Bread Burger", "Homemade Burgers"])
```
