# 06_dictionaries.py

countries = {
    "CZ": "Česko",
    "SK": "Slovensko",
    "DE": "Německo",
    "AT": "Rakousko",
    "PL": "Polsko",
}

def invert_dict(dictionary):
    '''
    Inverts the given dictionary by swapping its keys and values.

    Args:
        dictionary (dict): The dictionary to invert.

    Returns:
        dict: A new dictionary with keys and values swapped from the input dictionary.
    '''
    inverted_dictionary = {}

    for key, value in dictionary.items():
        inverted_dictionary[value] = key
    
    return inverted_dictionary


def get_value_lengths(dictionary):
    '''
    Creates a new dictionary with the same keys as the input dictionary,
    but replaces each value with the length of the original value.

    Args:
        dictionary (dict): The input dictionary whose values must be iterable
                           (e.g., strings, lists, tuples).

    Returns:
        dict: A dictionary with the same keys as the input, where each value
              is the length of the corresponding value in the input dictionary.
    '''
    counted_values_dictionary = {}

    for key, value in dictionary.items():
        counted_values_dictionary[key] = len(value)
    
    return counted_values_dictionary

def main():
    countries_name = invert_dict(countries)
    countries_len = get_value_lengths(countries)
    print(countries_name, countries_len)

if __name__ == '__main__':
    main()

