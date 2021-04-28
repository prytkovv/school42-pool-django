import sys


def get_key_from_dict(my_dict: dict, value: str) -> str:
    return ''.join([k for k, v in my_dict.items() if v == value])


def get_capital_or_state(word: str) -> str:
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
    if word.lower() in {k.lower(): v for k, v in states.items()}:
        word = ''.join(k for k in states.keys() if k.lower() == word.lower())
        return '%s is the capital of %s' % (capital_cities[states[word]], word)
    elif get_key_from_dict({k: v.lower() for k, v in capital_cities.items()}, word.lower()):
        word = ''.join(v for v in capital_cities.values() if v.lower() == word.lower())
        return '%s is the capital of %s' % (word, get_key_from_dict(states, get_key_from_dict(capital_cities, word)))
    else:
        return '%s is not a capital or a state' % word


if __name__ == '__main__':
    if len(sys.argv) == 2:
        for i in [i.strip() for i in sys.argv[1].split(',')]:
            if i != '':
                print(get_capital_or_state(i))
