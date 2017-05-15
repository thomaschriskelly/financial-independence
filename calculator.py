import math

net_worth = int(input('What is your net worth?'))
yearly_savings = int(input('What is your yearly savings?'))
yearly_spending = int(input('How much do you spend per year?'))

SAFE_WITHDRAWL_RATE = 0.04
safe_withdrawl = net_worth * SAFE_WITHDRAWL_RATE
print('Your safe withdrawl amount is ${} per year'.format(safe_withdrawl))
retirement_required = yearly_spending / SAFE_WITHDRAWL_RATE
print('You need to earn ${} (${} more) to retire'.format(retirement_required, retirement_required - net_worth))

HISTORICAL_RETURNS = 0.07

def compound_interest_with_contributions(initial, yearly_contrib, yearly_interest, years):
    '''
    Calculate future net worth taking into account annual contributions
    and average yearly interest
    https://math.stackexchange.com/questions/1698578/compound-interest-formula-adding-annual-contributions
    P = Initial Amount
    i = yearly interest rate
    A = yearly contribution or deposit added.
    n = the deposits will be made for 10 consecutive years.
    F = final amount obtained.
    (P + A/i)(1+i)^years - A/i
    '''
    return (initial + yearly_contrib / yearly_interest)*(1 + yearly_interest)**years - yearly_contrib / yearly_interest

print('In five years you will have ${}'.format(
    compound_interest_with_contributions(net_worth, yearly_savings, HISTORICAL_RETURNS, 5)
))

def years_to_retirement(initial, yearly_contrib, yearly_interest, amount_required):
    x = (amount_required + yearly_contrib / yearly_interest) / (initial + yearly_contrib / yearly_interest)
    return math.log(x, (1 + yearly_interest))

print('You can safely retire in {} years'.format(years_to_retirement(net_worth, yearly_savings, HISTORICAL_RETURNS, retirement_required)))
