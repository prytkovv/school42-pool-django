from local_lib.path import Path


if __name__ == '__main__':
    d = Path('/home/xubuntu_admin/Desktop/42/d03/ex01/test_dir/')
    d.mkdir_p()
    f = Path('/home/xubuntu_admin/Desktop/42/d03/ex01/test_dir/test_file.txt')
    f.touch()
    f.open()
    f.write_text('test text')
    print(f.text())
