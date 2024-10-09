
def main():
    score = int(input('Enter the numerical score (0-100) > '))
    print (checkGrade(score))
    
def checkGrade(score):
    if score < 0 or score > 100:
        return 'Invalid input, please enter between 0 and 100'
    elif score <60:
        return 'F'
    elif score < 70:
        return 'D'
    elif score < 80:
        return 'C'
    elif score < 90:
        return 'B'
    else:
        return 'A'

main()