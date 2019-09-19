def extract_time_components(s):
    """
    >>> extract_time_components('21:30:00')
    {'hours': 21, 'minutes': 30, 'seconds': 0}
    >>> extract_time_components('09:01:53')
    {'hours': 9, 'minutes': 1, 'seconds': 53}
    """
    #create a list that separates the values
    s = s.split(":")
    #turn the list into a dictionary with key
    time_in_dict = {}
    time_in_dict['hours'] = int(s[0])
    time_in_dict['minutes'] = int(s[1])
    time_in_dict['seconds'] = int(s[2])
    
    return time_in_dict
    