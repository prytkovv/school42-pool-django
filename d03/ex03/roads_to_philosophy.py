import sys
import requests
import bs4


def get_href(contents: bs4.element.ResultSet) -> 'href':
    for content in contents:
        for tag in content.find_all('a'):
            if tag.get('title') is not None:
                if 'Help' not in tag.get('title'):
                    ref = tag.get('href')
                    return ref


def get_road_to_philosophy(query: str) -> str:
    roads_counter = 0
    visited = []
    while True:
        url = 'https://en.wikipedia.org/wiki/' + query
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.content, 'html.parser')
        heading = soup.find(id='firstHeading').get_text()
        if len(visited) > 2 and heading == visited[-2]:
            return 'It leads to infinity loop!'
        visited.append(heading)
        if heading.lower() == 'philosophy':
            return '%d roads from %s to philosophy!' % (roads_counter, query)
        try:
            contents = soup.find(class_='mw-parser-output').find_all('p')
            first_ref = get_href(contents)
            query = first_ref.split('/')[2]
        except AttributeError:
            return 'It leads to dead end!'
        roads_counter += 1
        print(heading)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(get_road_to_philosophy(sys.argv[1]))
