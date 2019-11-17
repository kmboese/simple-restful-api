DEFAULT_AGE = 35
DEFAULT_USER = 'DefaultUser'
DEFAULT_OCCUPATION = 'DefaultOccupation'

class User():
    def __init__(self, name=None, age=None, occupation=None):
        if name:
            self.name = name
        else:
            self.name = DEFAULT_USER
        if age:
            self.age = age
        else:
            self.age = DEFAULT_AGE
        if occupation:
            self.occupation = occupation
        else:
            self.occupation = DEFAULT_OCCUPATION

    def __str__(self):
        ret = 'User:\n'
        ret += 'Name: {}\n'.format(self.name)
        ret += 'Age: {}\n'.format(self.age)
        ret += 'Occupation: {}\n'.format(self.occupation)

        return ret
        
### Helper Functions ###

# Get URL endpoint given a User object
def getUserEndpoint(user):
    endpoint = str(user.name) + '?'
    endpoint += 'age=' + str(user.age)
    endpoint += '&occupation=' + str(user.occupation)

    return endpoint