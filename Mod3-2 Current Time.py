#Finding military time with an alarm

#Get current and alarm times, ensuring valid inputs
while True:
    try:
        current_time = int(input('What time is it currently (0-23)? '))
        if current_time in range(24):
            while True:
                try:
                    alarm_hours = int(input('In how many hours do you want the alarm to go off? '))
                    break
                except ValueError:
                    print('Not an integer, try again!')
            break
        else:
            print('Not a valid time, try another time')
    except ValueError:
        print('Not a valid answer, enter a proper integer between 0-23')              

#Get remainder from dividing total hours by 24
#Also converting that time to remainder from 12 to get non-military time
alarm_time = (current_time + alarm_hours) % 24
real_time = alarm_time % 12

time_meridiem = ()
alarm_meridiem = ()
non_mil_time = real_time

#Converting total hours into days and hours
time_days = alarm_hours // 24
time_hours = alarm_hours % 24

#Determines the Meridiem of alarm time
if 0 < alarm_time <=11:
    alarm_meridiem = ('AM')
    
elif 12 <= alarm_time <= 23:
    alarm_meridiem = ('PM')
    non_mil_time = alarm_time - 12

else:
    alarm_meridiem = ('AM')
    non_mil_time = alarm_time + 12

    
print(f'\nThe time is currently {current_time}:00')
print(f'The alarm will go off in {alarm_hours} hours, which will be {time_days} days, {time_hours} hours')
print(f'\nThat will be {alarm_time}:00 ({non_mil_time}:00 {alarm_meridiem})')


