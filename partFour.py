def main():
    while True:
        if authenticator() == False:
            continue
        else:
            break
    
def checkUsername(username):
    correctUsername = 'admin'
    if username == correctUsername:
        return True
    else:
        return False

def checkPassword(password):
    correctPassword = 'Password123'
    if password == correctPassword:
        return True
    else:
        return False    

def authenticator():
    username = input('Enter username > ')
    if checkUsername(username) == True:
        password = input('Enter password > ')
        if checkPassword(password) == True:
            print ('Access Granted')
            return True
        else:
            print ('Incorrect Password.')
            return False
    else:
        print ('Incorrect Username.')
        return False
        
main()