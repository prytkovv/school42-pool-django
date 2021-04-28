class Intern(object):

    def __init__(self, name: str =
        """My name? I'm nobody, year intern, I have no name."""):
        self.name = name

    def __str__(self) -> str:
        return self.name

    class Coffee(object):

        def __str__(self):
            return 'This is the worst coffee you ever tested.'

    def work(self):
        raise Exception("I'm just-year intern, I cant't do that...")

    def make_coffee(self) -> Coffee:
        return self.Coffee()


if __name__ == '__main__':
    Mark = Intern('Mark')
    print(Mark.make_coffee())
    try:
        no_name_intern = Intern()
        no_name_intern.work()
    except Exception as e:
        print(e)
