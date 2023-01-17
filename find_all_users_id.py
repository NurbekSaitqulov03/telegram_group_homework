from read_data import read_data

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    a = []
    b = data['messages']
    for i in b:
        if 'actor_id' in i:
            a.append(i['actor_id'])
    return a
print(find_all_users_id(read_data('data/result.json')))