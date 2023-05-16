if __name__ == "__main__":
    bill_amount = float(0)
    number_of_people = int(0)
    desired_tip_percentage = float(0)

    print('Welcome to the tip calculator.')

    while(1):
        try:
            bill_amount_input = input('What was the total bill? ')
            bill_amount = float(bill_amount_input)
            break
        except ValueError:
            print('You must enter a valid number for the bill amount.')

    while(1):
        try:
            number_of_people_input = input('How many people to split the bill? ')
            number_of_people = int(number_of_people_input)
            break
        except ValueError:
            print('You must enter a valid number for the number of people.')

    while(1):
        try:
            desired_tip_percentage_input = input('What percentage tip would you like to give? ')
            desired_tip_percentage = float(desired_tip_percentage_input)
            break
        except ValueError:
            print('You must enter a valid number for the tip percentage.')
    
    tip_amount = bill_amount * (float(desired_tip_percentage) / 100)
    total_amount = float(bill_amount) + tip_amount
    individual_amount = round(total_amount / number_of_people, 2)
    individual_amount = '{:.2f}'.format(individual_amount)

    print(f'Each person should pay: ${individual_amount}')