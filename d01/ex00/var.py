def my_var() -> None:
    int_var = 42
    string_var = '42'
    alphabetic_string_var = 'forty two'
    float_var = 42.0
    bool_var = True
    list_var = [42]
    dict_var = {42: 42}
    tuple_var = (42,)
    set_var = set()
    for value in locals().values():
        print('{} is of type {}'.format(value, type(value)))


if __name__ == '__main__':
    my_var()
