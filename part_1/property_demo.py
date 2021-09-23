class Person():

    def __init__(self, firstname, lastname):
        self.first = firstname
        self.last = lastname

    @property    
    def fullname(self):
        return self.first + ' '+ self.last

    #The setter method should have the same name 
    # as the equivalent method that @property decorates.

    @fullname.setter
    def fullname(self, name):
        firstname, lastname = name.split()
        self.first = firstname
        self.last = lastname

    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

# Create a Person object
person = Person('bob', 'alpha')
# Change last name to beta
person.last = 'beta'
print(f"last name = {person.last}")
# Next, print the person's full name ( first + last ):
#person.fullname = 'mr moo'
print(f"full name = {person.fullname}") 
print(person.email())