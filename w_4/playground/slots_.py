class Jedi:
    """
    Suposse to be only one!
    """
    __slots__ = ['anakin']

    def __init__(self):
        super(Jedi, self).__init__()
        self.anakin = 'The Choosen One'


obj = Jedi()
obj.luke = 'The Choosen Two'
