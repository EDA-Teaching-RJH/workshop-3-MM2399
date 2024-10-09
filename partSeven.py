def main():
    while True:
        num1 = getNumber(1)
        if num1 == 'quit':
            print ('Quitting.')
            break
        num2 = getNumber(2)
        if num2 == 'quit':
            print ('Quitting.')
            break
        if doCalculation(num1, num2, operator = getOperator()) == False:
            print ('Quitting.')
            break
    
def getNumber(index):
    while True:
        number = input(f'Enter number {index} > ')
        try:
            number = float(number)
            return number
        except ValueError:
            try:
                number = number.lower()
                if number == 'quit':
                    return 'quit'
            except ValueError:
                print ('Please enter a valid number.')
                continue                

def getOperator():
    operators = ['+','-','*','/','^','%']
    while True:
        operator = input('Enter operator > ')
        if operator in operators:
            return operator
        try:
            operator = operator.lower()
            if operator == 'quit':
                return 'quit'
        except ValueError:
            print ('Please enter a valid operator.')
            continue

def doCalculation(num1, num2, operator):
    if num1 == 'quit' or num2 == 'quit':
        return False
    match operator:
        case '+':
            result = num1 + num2
            print (f'{num1} + {num2} = {result}')
        case '-':
            result = num1 - num2
            print (f'{num1} - {num2} = {result}')
        case '*':
            result = num1 * num2 
            print (f'{num1} * {num2} = {result}')
        case '/':
            result = num1 / num2
            print (f'{num1} / {num2} = {result}')
        case '^':
            result = num1 ** num2
            print (f'{num1} ^ {num2} = {result}')
        case '%':
            result = num1 % num2
            print (f'{num1} % {num2} = {result}')
        case 'quit':
            return False

main()