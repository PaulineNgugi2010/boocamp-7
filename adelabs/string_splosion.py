class StringSplosion(object):
    '''
    This is a class that does spring explosion
        i.e
        phone  => pphphophonphone
        ab     => aab
        like   => lliliklike

    '''

    def __init__(self , string):
        self.string = string

    def manipulate(self):
        output = ''
        for i in range(len(self.string)+1):
            output += self.string[:i]
        return output