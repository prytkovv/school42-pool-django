def var_to_dict() -> None:
    musicians_list = [
        ('Hendrix', '1942'),
        ('Allman', '1946'),
        ('King', '1925'),
        ('Clapton', '1945'),
        ('Johnson', '1911'),
    ]
    musicians_dict = {value[1]: value[0] for value in musicians_list}
    for k, v in musicians_dict.items():
        print('{} : {}'.format(k,v))


if __name__ == '__main__':
    var_to_dict()
