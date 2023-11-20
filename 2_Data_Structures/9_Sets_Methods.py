# isdisjoint(): The isdisjoint() method checks if one or more items of a particular set are present in original set.
# This method returns False if items are present, else it returns True.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))


# issuperset(): The issuperset() method checks if all the items of a particular set are present in the original set.
# It returns True if all the items are present, else it returns False.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Madrid"}
print(cities.issuperset(cities2))


# issubset(): The issubset() method checks if all the items of the original set are present in the particular set.
# It returns True if all the items are present, else it returns False.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))


# add(): to add a single item to the set
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)


# update(): to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary),
# and use the update() method to add it into the existing set.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)

'''remove()/discard(): to remove items from the list.
The main difference between remove and discard is that, if we try to delete an item which is not present in set,
then remove() raises an error, whereas discard() does not raise any error.'''
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)

cities.discard('Madrid')
print(cities)


'''pop(): This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered.
However, you can access the popped item if you assign the pop() method to a variable.'''
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities, item)


# clear(): This method clears all items in the set and prints an empty set.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)


# del: del is not a method, rather it is a keyword which deletes the set entirely.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
# print(cities) # We get an error because our entire set has been deleted and there is no variable called cities which contains a set.


# Check if item exists
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")