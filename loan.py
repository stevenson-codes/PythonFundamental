# Get details of loan
money_owed = float(input('How much money do you owe, in dollars?\n'))
apr = float(input('What is the annual percentage rate of the loan?\n'))
payment = float(input('How much will ou pay off each month in dollars?\n'))
months = int(input('How many months do you want to see the results for?\n'))

monthly_rate = apr/100/12

for i in range(months):
    interest_paid = money_owed * monthly_rate
    amount_paid = payment - interest_paid

    if money_owed - payment < 0:
        print(f'The last payment is {money_owed}')
        print('You paid off the loan in', i + 1, 'months')
        break
    
    money_owed -= amount_paid

    print(f'Paid {payment} of which {interest_paid} was interest', end=' ')
    print('Now I owe', money_owed)