name = 'Duncan'
num = 3
print('My name is ',name,' and my favourite number is ',num)
for a in range(num**2+1):
    print(a)
    
class Engineers:
    skill = "problem solver"
    
    def __init__(self,name,typ,years):
        self.name = name
        self.typ = typ
        self.years = years
        
    def print(self):
        print('The Engineer is called',self.name)
        print(self.name, 'is a', self.typ, 'Engineer with', self.years, 'years of experience')
    
    def rev(self):
        name_temp = ''
        while len(self.name) > 0:
            name_temp += self.name[-1].lower()
            self.name = self.name[0:-1]
        self.name = name_temp
        self.name = self.name[0].upper() + self.name[1::]


b = Engineers('Andrew', 'Mechanical', 23)
c = Engineers('Jemimah', 'Civil', 32)
b.print()
c.rev()
c.print()