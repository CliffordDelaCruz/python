#list_element_swap.py
#this swaps the first and last element, then 2nd and 2nd to the last element.. etc.
my_list = [10, 1, 8, 3, 5, 9, 6, 5]
length = len(my_list)
print(length // 2)
for i in range(length // 2):

    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)