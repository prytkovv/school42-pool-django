from textwrap import dedent
from inspect import cleandoc
from pprint import pprint

class PeriodicTable(object):

    def __init__(self):
        self.elements = self.__get_data_from_file()

    def __multi_split(self, s:str, delims: str) -> 'generator':
        pos = 0
        for i, c in enumerate(s):
            if c in delims:
                yield s[pos:i]
                pos = i + 1
        yield s[pos:]

    def __get_data_from_file(self) -> dict:
        with open('periodic_table.txt') as table:
            elements = [
                [word.strip()
                    for word in self.__multi_split(row, ',:=')]
                for row in table.readlines()
            ]
            elements = {
                word[0]:
                {word[i]: word[i + 1] for i in range(1, len(word[1:]), 2)}
                for word in elements
            }
            return elements

    def create_html_form(self) -> 'html':
        with open('periodic_table.html', 'w') as table:
            html_head = """
            <!DOCTYPE html>
            <html>
                <head>
                <meta charset="utf-8">
                <title>Mendeleev table</title>
                </head>
                <body>
                <table>
            """
            table.write(dedent(cleandoc(html_head)))
            for i in self.elements:
                
            html_end = """
                </table>
                </body>
            </html>
            """
            table.write(dedent(html_end))


if __name__ == '__main__':
    table = PeriodicTable()
