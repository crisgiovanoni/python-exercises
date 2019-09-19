def is_two(n):
    """
    Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2 False otherwise.
    """
    if n == 2 or n == "2":
        return True
    else:
        return False

print(is_two("2"))

def is_vowel(x):
    """
    Define a function named is_vowel.
    It should return True if the passed string is a vowel, False otherwise.
    """
    if x in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
        return True
    else:
        return False

print(is_vowel("i"))

def is_consonant(x):
    """
    Define a function named is_consonant.
    It should return True if the passed string is a consonant, False otherwise.
    Use your is_vowel function to accomplish this.
    """
    if is_vowel(x) == False:
        return True
    else:
        return False

print(is_consonant("b"))

def capitalize_consonant(x):
    """
    Define a function that accepts a string that is a word.
    The function should capitalize the first letter of the word
    if the word starts with a consonant.
    """
    if is_consonant(x[0]) == True:
        return x.capitalize()
    else:
        return x

print(capitalize_consonant("apple"))

#short version of if-else
def cap_if_consonant(word):
    return word.capitalize() if is_consonant(word[0]) else word

def calculate_tip(tip=0.2, bill_total=65):
    """
    Define a function named calculate_tip.
    It should accept a tip percentage (a number between 0 and 1) and the bill total, and
    return the amount to tip.
    """
    total_tip = tip * bill_total
    return total_tip

print(calculate_tip(0.2,40))
    
def apply_discount(original_price=1000, discount_percentage=.4):
    """
    Define a function named apply_discount.
    It should accept a original price, and a discount percentage, and
    return the price after the discount is applied.
    """
    discounted_price = original_price - (original_price * discount_percentage)
    return discounted_price

print(apply_discount(1000,.4))

def handle_commas(num_with_comma):
    """
    Define a function named handle_commas.
    It should accept a string that is a number that contains commas in it as input, and
    return a number as output.
    """
    num_with_comma = num_with_comma.replace(",","")
    return int(num_with_comma)

print(handle_commas("1,000"))

type(handle_commas("1,000"))

def get_letter_grade(grade):
    """
    Define a function named get_letter_grade.
    It should accept a number and return the letter grade associated with that number (A-F).
    """
    if grade >= 88 and grade <= 100:
        return "A"
    elif grade >= 80 and grade <= 87:
        return "B"
    elif grade >= 67 and grade <= 79:
        return "C"
    elif grade >= 60 and grade <= 66:
        return "D"
    elif grade >= 0 and grade <= 59:
        return "F"
    else:
        return "Grade entered is invalid."

print(get_letter_grade(97))

def remove_vowels(word):
    """
    Define a function named remove_vowels that accepts a string and
    returns a string with all the vowels removed.
    """
    for letter in str(word):
        if letter in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            word = word.replace(letter,"")
        else:
            return word

print(remove_vowels("apple"))

def normalize_name(word):
    """
    Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
    anything that is not a valid python identifier should be removed
    leading and trailing whitespace should be removed -- strip
    everything should be lowercase -- lower
    spaces should be replaced with underscores --replace
    """
    word = word.strip()
    word = word.lower()
    word = word.replace(" ","_")
    return word

print(normalize_name(" Hello World"))

# def cumsum(my_list):
#     """
#     Write a function named cumsum that accepts a list of numbers and
#     returns a list that is the cumulative sum of the numbers in the list.
#     """
#     my_list.insert(0,0)
#     new_list = []

#     for num in my_list:
#         num = num + my_list[my_list.index(num)-1] + my_list[my_list.index(num)-2] #num = value of num + value of before num
#         new_list.append(num) #insert num on the list
#         if  new_list.index(num) == len(my_list): #position of num = position of last value
#             break
    
#     del new_list[0]
#     return new_list

# print(cumsum([1,2,3,4]))

def cumsum(my_list):
    """
    Write a function named cumsum that accepts a list of numbers and
    returns a list that is the cumulative sum of the numbers in the list.
    """
    new_list = []
    for num in my_list:
        my_list.append(num)
        sum_list = sum(sum_list)
        


## use this as value of num >> my_list[my_list.index(num)

my_list.index(num) = position of num
my_list.index(num) - 1 = position

my_list = [1, 2, 3, 4]
my_list.index(3) = position of 2
my_list.index(2) - 1 = position of before 2

my_list[my_list.index(2)] 
my_list[my_list.index(2)-1] 

my_list.index(num) = position of num
my_list.index(num) - 1 = position of before num
my_list.index(num) - 1 = position of before num


my_list[my_list.index(num)] = value of num
my_list[my_list.index(num)-1] = value of before num

• cumsum([1, 1, 1]) returns [1, 2, 3]


cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]