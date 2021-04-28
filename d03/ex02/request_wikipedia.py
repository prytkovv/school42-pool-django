import sys
import requests
import dewiki


def search(searched_text: str):
    url = 'https://en.wikipedia.org/w/api.php'
    params = {
        'action': 'query',
        'prop': 'revisions',
        'rvprop': 'content',
        'titles': searched_text,
        'format': 'json'
    }
    response = requests.get(url=url, params=params)
    if response.status_code == 200:
        response_dict = response.json()
        pages = response_dict['query']['pages']
        pageid = ''.join(pages.keys())
        if pageid != '-1':
            with open(searched_text.replace(' ', '_') + '.wiki', 'w') as f:
                f.write(dewiki.from_string(pages[pageid]['revisions'][0]['*']))
                return
    print('Invalid query')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        search(sys.argv[1])
    else:
        print('Bad parameters')
