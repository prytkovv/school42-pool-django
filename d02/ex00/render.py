import os
import sys
import re


class Render(object):

    def __init__(self, filename: str):
        self.filename = filename
        self.data_dict = self.__get_data_from_file()

    def __get_data_from_file(self) -> dict:
        try:
            with open(self.filename) as f:
                return {
                    re.split(r'\W+', line)[0]: re.split(r'\W+', line)[1]
                    for line in f.readlines()
                }
        except FileNotFoundError:
            print("File doesn't exitst")
            exit(1)

    def handle_HTML(self, filename):
        try:
            with open(filename) as source:
                file_text = source.read()
        except FileNotFoundError:
            print("File doesn't exist")
            exit(1)
        else:
            file_path = os.path.splitext(filename)
            if file_path[1] == '.template':
                with open(str(file_path[0]) + '.html', 'w') as revised_file:
                    revised_file.write(file_text.format(**self.data_dict))
            else: print('Incorrect file extension')


if __name__ == '__main__':
    if len(sys.argv) == 3:
        render = Render(sys.argv[1])
        render.handle_HTML(sys.argv[2])
