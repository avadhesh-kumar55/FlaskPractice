class Animal:
    says = 'hello'
    def __init__(self):
        self.species = 'kite'

    # instance method
    def runs(self):
        print(self.species)

    # static method
    @staticmethod
    def add(a,b):
        return a+b


    @classmethod
    def jungle(cls):
        print(cls.says)

a1 = Animal()
# print(Animal.says)
# print(a1.says)
# print(a1.species)

a1.runs()
print(a1.add(1,2))
a1.jungle()

Animal().runs()
Animal.jungle()
print(Animal.add('hello ','kamlesh'))

