# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) 
# and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean. 

def number_in_list(ordered_list, num):
    for item in ordered_list:
        if item == num:
            print(True)
            return True
        elif item > num:
            print(False)
            return False

    print(False)
    return False

lst = [1, 3, 5, 7, 9, 11, 15]
number_in_list(lst, 7)   
number_in_list(lst, 8)   
