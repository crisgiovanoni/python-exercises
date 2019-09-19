def normalize_name(word):
    """
    Define a function named ``normalize_name``. It should accept a string and
    return a valid python identifier
    """
    special_char = "/'!@#$%^&*()-+={|\]}?><,.~`"
    word_list = []
    for c in word:
        if c not in special_char:
            word_list.append(c)
    word = ''.join(word_list)
    return word.lower().strip().replace(" ","_")

def cumsum(num_list):
    """
    Write a function named ``cumsum`` that accepts a list of numbers and returns
    a list that is the cumulative sum of the numbers in the list.
    """
    total = 0
    cum_list = []
    for n in num_list:
        total += n
        cum_list.append(total)
    return cum_list