from random import randint

def roll_dice(ndm):
    """
    >>> roll_dice('4d4')
    [1, 3, 2, 2]
    >>> roll_dice('2d10')
    [8, 3]
    """
    #split the ndn input with d as delimiter
    list_split = ndm.split("d")
    print(list_split)
    dice_count = int(list_split[0])
    side = int(list_split[1])
    #produce a list with side as the length of the list with each element = randint(1, n1)
    random_list = []
    while len(random_list) < side:
        random_number = randint(1, dice_count)
        print(random_number)
        random_list.append(random_number)
    return random_list


# # Write a function named chunk. It should split a list into n-sized chunks

# def chunk(user_list, n):
#     """
#     >>> my_list = [1, 2, 3, 4, 5, 6, 7, 8]
#     >>> chunk(my_list, 2)
#     [[1, 2], [3, 4], [5, 6], [7, 8]]
#     >>> chunk(my_list, 3)
#     [[1, 2, 3], [4, 5, 6], [7, 8]]
#     """
#     #split the list with n length
#     list_of_lists = []
#     for i in range(int(len(user_list)/n))
#         list_of_lists.append([])
#             for num in user_list:
            
#     return list_of_lists

# # new_list = [[i for i in range(10)] for j in range(10)]

# my_list = [1, 2, 3, 4, 5, 6, 7, 8]
# print(chunk(my_list,2))

# Write a function named map it should accept a list and a function and apply the function to every element in the list

# map([1, 2, 3], lambda n: n + 1)
# [2, 3, 4]

# define a function named format_phone_number it should standardize different phone number formats

# >>> format_phone_number('210.867.5309')
# '(210) 867-5309'
# >>> format_phone_number('2108675309')
# '(210) 867-5309'
# >>> format_phone_number('210-867-5309')
# '(210) 867-5309'
# >>> format_phone_number('(210) 867-5309')
# '(210) 867-5309'

# that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
def remove_duplicates(l):
    new_list = set(l)
    new_list = list(new_list)
    return new_list

print(remove_duplicates([1,2,4,4,5,3,2,1]))

