import requests
import urllib3

from http_codes import isError

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

# Get user from server
def getUser(url, name):
    resource = 'user/' + name
    request = '/'.join([url, resource])

    try:
        r = requests.get(request)

        print('Request: {}\nReponse: {}HTTP Code: {}'
            .format(request, r.text, r.status_code))

    # Handle failures
    except ConnectionError as e:
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
                getUser(url, resourceInput)
                
        except ConnectionError as e:
            print(e)
            exit(1)


if __name__ == '__main__':
    main()