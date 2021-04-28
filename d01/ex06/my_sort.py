def sort_dict() -> None:
    d = {
        'Hendirx': '1942',
        'Allman': '1946',
        'King': '1925',
        'Clapton': '1945',
        'Johnson': '1911',
        'Berry': '1926',
        'Vaughan': '1954',
        'Cooder': '1947',
        'Page': '1944',
        'Richards': '1943',
        'Hammett': '1962',
        'Cobain': '1967',
        'Garcia': '1942',
        'Besk': '1944',
        'Santana': '1947',
        'Ramone': '1948',
        'White': '1975',
        'Frusciante': '1970',
        'Thompson': '1949',
        'Burton': '1939',
    }
    print('Sorted in alphabetical order of names')
    for i in sorted(d):
        print(i)
    print('Sorted in ascending order of years')
    for i in {k: v for k, v in sorted(d.items(), key=lambda x: x[1])}.keys():
        print(i)


if __name__ == '__main__':
    sort_dict()
