'''
Joining Sets
1. union() and update(): The union() and update() methods prints all items that are present in the two sets. 
The union() method returns a new set whereas update() method adds item into the existing set from another set.

2. intersection and intersection_update(): The intersection() and intersection_update() methods prints only items that are similar to both the sets. 
The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.

3. symmetric_difference and symmetric_difference_update(): The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets. 
The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.

4. difference() and difference_update(): The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets. 
The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.
'''

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
print(cities3)

cities.update(cities2)
print(cities)


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)

cities.intersection_update(cities2)
print(cities)


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)

cities.symmetric_difference_update(cities2)
print(cities)


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.difference(cities2)
print(cities3)

print(cities.difference(cities2))