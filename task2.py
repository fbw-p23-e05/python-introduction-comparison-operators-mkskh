print('List of months: January, February, March, April, May, June, July, August, September, October, November, December')

month = input('Input the name of Month: ')
days31 = ['January', 'March', 'May', 'July', 'August', 'October', 'December']
days30 = ['April', 'June', 'September', 'November']
feb = 'February'

if month in days31:
    print('Number of days: 31 days')
elif month in days30:
    print('Number of days: 30 days')
elif month == feb:
    print('Number of days: 28 days')
else: 
    print('Please write the month')
