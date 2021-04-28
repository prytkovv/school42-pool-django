def get_numbers_from_file() -> None:
    with open('numbers.txt') as my_file:
        numbers = ''.join(my_file.readlines()).split(',')
        for i in numbers:
            print(i)


if __name__ == '__main__':
    get_numbers_from_file()
