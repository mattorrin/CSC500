#Average rainfall over the years

years = int(input("How many years of data do you want? "))

#initialize values
rainfall_amount = 0.0
tot_months = 0

#Get data for the number of years, and then 12 months for each year
for year in range(1, years + 1):
        print(f'\nYear {year}: ')
        for month in range(1, 12 + 1):
                rain = float(input(f'Enter rainfall for month {month} in inches: '))
                rainfall_amount += rain
                tot_months += 1
average_rain = rainfall_amount / tot_months

print('\n---Rainfall averages---')
print(f'In a total of {tot_months} months')
print(f'It has rained a total of {rainfall_amount} inches')
print('That is an average of {:.2f} inches per month'.format(average_rain))

