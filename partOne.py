def main():
    age = int(input('Enter your age > '))
    print (checkAge(age))
    
def checkAge(age):
    if age >= 18:
        return 'You are an adult'
    else:
        return 'You are a child'

main()