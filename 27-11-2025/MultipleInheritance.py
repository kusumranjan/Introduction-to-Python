#smart phone , Camera + Phone
class Camera:
    def take_photos(self):
        print("take photos")
class Phone:
    def make_call(self):
        print("make call")
class Smartphone(Camera, Phone):
    def browse_internet(self):
        print("browse internet")
sp = Smartphone()
sp.take_photos()
sp.make_call()
sp.browse_internet()

#DataScientist , Programmer + Statistian


class Programmer:
    def __init__(self, languages):
        self.languages = languages




class Statistician:
    def __init__(self, tools):
        self.tools = tools




class DataScientist(Programmer, Statistician):
    def __init__(self, languages, tools, domain):
        Programmer.__init__(self, languages)
        Statistician.__init__(self, tools)
        self.domain = domain




ds = DataScientist(["Python", "R"], ["Pandas", "NumPy"], "Machine Learning")
print(ds.languages)
print(ds.tools)
print(ds.domain)

