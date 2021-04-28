import sys


def get_capital(state: str) -> str:
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
        return capital_cities[states[state]]
    except KeyError:
        return 'Unknown state'


if __name__ == '__main__':
    if (len(sys.argv) == 2):
        print(get_capital(sys.argv[1]))
