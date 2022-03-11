class Animal:
    def __init__(self,Animal):
        print(Animal, 'é um animal.')


class mamifero(Animal):
    def __init__(self, mammalName):
        print(mammalName, 'é um animal sangue quente')
        super().__init__(mammalName)

class Naovoa(mamifero):
    def __init__(self, naovoaBicho):
        print(naovoaBicho, 'nao voa')
        super().__init__(naovoaBicho)

class naoNada(mamifero):
    def __init__(self, naoNada):
        print(naoNada, 'nao nada')
        super().__init__(naoNada)

class dog(naoNada,Naovoa):
    def __init__(self):
        print('Joel')
        super().__init__('Joel')

catioto=mamifero('baleia')
print(catioto)