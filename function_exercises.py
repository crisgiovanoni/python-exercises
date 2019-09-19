def is_two(n):
    """
    Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2 False otherwise.
    """
    if n == 2 or n == "2":
        return True
    else:
        return False

def is_vowel(x):
    """
    Define a function named is_vowel.
    It should return True if the passed string is a vowel, False otherwise.
    """
    if x in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
        return True
    else:
        return False

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