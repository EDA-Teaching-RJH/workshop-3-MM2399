def main():
    day = input('What day is it? > ')
    checkIfWeekend(day)
    
def checkIfWeekend(day):
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = day.lower()
    if day in days:
        if day == 'saturday' or day == 'sunday':
            print ("It's the weekend!")
        else:
            print ("It's a weekday.")
    else:
        print ('That is not a valid day.')

main()