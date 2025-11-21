# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

def remove_duplicates(lst):
    new_list = []
    for item in lst:
        if item not in new_list:
            new_list.append(item)
    return new_list

a = [1, 2, 3, 1, 2, 4, 5, 3]
result = remove_duplicates(a)
print("List without duplicates:", result)
