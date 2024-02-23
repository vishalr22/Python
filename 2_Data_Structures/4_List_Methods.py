'''
List Methods

list.sort() - sorts the list in ascending order. The original list is updated
list.sort(reverse=True) - sorts the list in descending order. The original list is updated
list.reverse() - reverses the order of the list. The original list is updated
list.index(list_item) - returns the index of the first occurrence of the list item. 
list.count(list_item) - returns the count of the number of items with the given value.
list.copy() - Returns copy of the list. This can be done to perform operations on the list without modifying the original list.
list.append("new_item") - appends item to the end of the existing list.
list.extend("multiple_new_items") - adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.
list.insert(index_number, item) - inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.
list.pop(item_index_number) - removes the item from the list based on the given item index number.
list.remove(list_item) - removes the first occurence of the list item.

Concatenating two lists
concatenated_list = list1 + list2
'''

colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)

colors.sort(reverse=True)
print(colors)

colors.reverse()
print(colors)

print(colors.index('indigo'))
print(colors.count('indigo'))

colors2 = colors.copy()
print(colors2)

colors.append('red')
print(colors)

colors.extend(['white', 'black', 'yellow'])
print(colors)

colors.insert(2, 'purple')
print(colors)

colors.pop(3)
print(colors)

colors.remove('purple')
print(colors)

final_colors = colors + colors2
print(final_colors)
