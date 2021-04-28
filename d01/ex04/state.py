import sys


def get_key_from_dict(my_dict:dict, value: str) -> str:
    for k, v in my_dict.items():
        if v == value:
            return k
    raise KeyError


def get_state(capital: str) -> str:
    states = {
        'Oregon': 'OR',
        'Alabama': 'AL',
        'New Jersey': 'NJ',
        'Colorado': 'CO'
    }
    capital_cities = {
        'OR': 'Salem',
        'AL': 'Montgomery',
        'NJ': 'Trenton',
        'CO': 'Denver'
    }
    try:
        return get_key_from_dict(states, get_key_from_dict(capital_cities, capital))
    except KeyError:
        return 'Unknown capital city'


if __name__ == '__main__':
    if (len(sys.argv) == 2):
        print(get_state(sys.argv[1]))
