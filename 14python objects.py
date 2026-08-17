class PartyAnimal:
    def __init__(self):
        self.x = 0

    def party(self):
        self.x = self.x + 1
        print('So far', self.x)

an = PartyAnimal()

an.party()

print('dir', dir(an))
print('type', type(an))
print(type(an.x))
print(type(an.party))

class PartyAnimal:
    def __init__(self):
        print('construct')
        self.x = 0

    def party(self):
        self.x = self.x + 1
        print('So far', self.x)

    def __del__(self):
        print('destruct', self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42 # 这里对an再次赋值了，所以把an注销了
print('an contains', an) # 对比函数就是可以在内部产生值，an.x如果是函数在函数使用结束会销毁，而这里会保留

class PartyAnimal:
    def __init__(self):
        self.x = 0

    def party(self):
        self.x = self.x + 1
        print('So far', self.x)

class FootballFAn(PartyAnimal):
    def __init__(self):
        super().__init__()
        self.points = 0

    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.points)

a = PartyAnimal()
b = FootballFAn()
a.party()
b.touchdown() # 输出两个1是正常的，因为1属于不同的对象，一个是a.x一个是b.x