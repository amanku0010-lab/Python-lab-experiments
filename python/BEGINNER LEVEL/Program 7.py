# Take a list, say for example this one: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] and write a program that prints out all the elements of the 
# list that are less than 5. Extras:  
# a) Instead of printing the elements one by one, make a new list that has all the elements less 
# than 5 from this list in it and print out this new list. 
# b) Write this in one line of Python. 
# c) Ask the user for a number and return a list that contains only elements from the original list a 
# that are smaller than that number given by the user

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
less_than_5 = []
for number in a:
    if number < 5:
        less_than_5.append(number)

print(less_than_5) 

print([x for x in a if x < 5])

num = int(input("Enter a number: "))
filtered_list = [x for x in a if x < num]
print(filtered_list)


