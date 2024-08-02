from random import randint

def random_index(names: list) -> int:
    """_Generate an index between o and len of array_

    Args:
        names (list): _list of names_

    Returns:
        int: _random int_
    """
    len_arr = len(names) - 1
    return randint(0, len_arr)

def get_name(arr_index: int, names: list) -> str:
    """_Get a name from a list given index of name_

    Args:
        arr_index (int): _index of name to get_
        names (list): _List to access_

    Returns:
        str: _name in given index_
    """
    return names[arr_index]