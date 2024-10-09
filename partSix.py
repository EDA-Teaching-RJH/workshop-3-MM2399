def main():
    print ('Ticket Price: £'+ str(checkPrice()))

def getStudentStatus():
    while True:
        status = input('Are you are student (yes or no) > ')
        status = status.lower()
        if status == 'yes':
            return True
        elif status == 'no':
            return False
        else:
            print ('Please enter yes or no.')


def getAge():
    while True:
        try:
            age = int(input('Enter your age > '))
            if age <0:
                print ('Please enter a valid age.')
            else:
                return age
        except ValueError:
            print ('Please input your age as a whole number.')
            
def checkPrice(status = getStudentStatus(), age = getAge()):
    if age < 12 or age > 65:
        price = 5
    elif age > 12 and status == True:
        price = 8
    else:
        price = 10
    return price

main()