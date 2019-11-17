import requests
import urllib3

from http_codes import isError
from user import User, getUserEndpoint

EXIT = 'exit'


# Prompt the user for an HTTP Request type
def printActionTypePrompt():
    print('Please enter an action (available actions: get, put, post, delete)'
    ' or \'exit\' to end the program:')


# Prompt the user for a user name
def printUserNamePrompt():
    print('Please enter a user name:')


# Goodbye message printed when program ends
def printGoodbyeMessage():
    print('Goodbye!')


# Get action type from user
def getActionType():
    actionInput = ''
    actions = ['get', 'put', 'post', 'delete', 'exit']

    while actionInput not in actions:
        if actionInput != '':
            print('Invalid action: "{}"'.format(actionInput))

        printActionTypePrompt()
        actionInput = input('> ')
    
    return actionInput


# Get User name from user
def getResourceName():
    printUserNamePrompt()
    resourceInput = input('> ')
    return resourceInput


# Get User from server by name and print response
def printUser(url, name):
    resource = 'user/' + name
    request = '/'.join([url, resource])

    try:
        r = requests.get(request)

        print('Response: {}\nHTTP Code: {}'
            .format(r.text, r.status_code))

    # Handle failures
    except ConnectionError as e:
        raise ConnectionError


# Get User from server by name and return User object
def getUser(url, name):
    resource = 'user/' + name
    request = '/'.join([url, resource])
    user = User()

    try:
        r = requests.get(request)
        userData = r.json()

        if isError(r.status_code):
            print('Error retrieving user {}: returned code {}'
                .format(name, r.status_code))
            return None
        else:
            user.name = userData['name']
            user.age = userData['age']
            user.occupation = userData['occupation']
            return user

    except ConnectionError:
        raise ConnectionError


# Update user 
def updateUser(url, name):
    field = -1
    newName, newAge, newOccupation = None, None, None

    # Prompt user for field to change
    while field < 1 or field > 3:
        print('Which field do you want to update for this user?')
        print('1.\tName')
        print('2.\tAge')
        print('3.\tOccupation')

        field = int(input('> '))
    
    if field == 1:
        newName = input('Enter a new name for this user > ')
    elif field == 2:
        newAge = input('Enter a new age for this user > ')
    elif field ==3 :
        newOccupation = input('Enter a new occupation for this user > ')
    
    try:
        # Get user from server
        user = getUser(url, name)

        # Update user data locally
        if newName:
            user.name = newName
        if newAge:
            user.age = newAge
        if newOccupation:
            user.occupation = newOccupation

        # Send PUT request using new User data
        resource = 'user/' + getUserEndpoint(user)
        request = '/'.join([url, resource])
        r = requests.put(request)

        # Show results
        print('Request: {}'.format(request))
        printUser(url, user.name)

    # Handle failures
    except ConnectionError:
        raise ConnectionError



def main():
    localhostIP = '127.0.0.1'
    port = '5000'
    url = 'http://' + localhostIP + ':' + port
    userInput = ''

    # Main loop
    while userInput != EXIT:

        actionInput = ''
        resourceInput = ''

        # Prompt user for api action and user name
        actionInput = getActionType()

        # Handle exit
        if actionInput == EXIT:
            printGoodbyeMessage()
            exit(0)

        resourceInput = getResourceName()

        # Handle API request
        try:
            if actionInput == 'get':
                printUser(url, resourceInput)
            elif actionInput == 'put':
                updateUser(url, resourceInput)
                

        except ConnectionError as e:
            print(e)
            exit(1)


if __name__ == '__main__':
    main()