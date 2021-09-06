# Michael Gennery
# Functions
# June 2020
# Version 2

import datetime



# Take some text with numbers in it and turn it into a number
# e.g. '£124.99 gross' becomes 124.99

def text_to_num(num_text):

    output_text = ''
    decimal_point = False
    
    for char in num_text:
     
        t_digit = 0
        digit = ''
        
        try:
            t_digit = int(char) # Test to see if character is a number
        except ValueError:
            if char == '.' and decimal_point == False: # This makes sure there is only one decimal point
                decimal_point = True
                digit = '.'
            else:
                digit = ''
        else:
            digit = char # If the character is a number then it can be added to the string

        output_text += digit # Add the number to the numerical output string

    if output_text == '.' or output_text == '':
        return(0)
    else:
        return(float(output_text)) # Return the number as a float




# TIME



# Calculate the total number of seconds in given hours, minutes and seconds

def calc_secs(hours, mins, secs):

    # Validate = max 23:59:59

    if (hours < 0 or hours > 23) or (mins < 0 or mins > 59) or (secs < 0 or secs > 59):
        print('Time must be between 00:00:00 and 23:59:59')
    else:
        tot_secs = (hours * 3600) + (mins * 60) + secs
        return(tot_secs)


def calc_secs2(input_time):

    # Valid input 'HH:MM:SS'

    output_hours = 0
    output_mins = 0
    output_secs = 0
    error_flag = False

    error_msg = 'Invalid Time - HH:MM:SS'
    if len(input_time) != 8:
        print(error_msg)
        error_flag = True
    elif input_time[2] != ':' or input_time[5] != ':':
        print(error_msg)
        error_flag = True

    output_hours = int(input_time[0:2])
    output_mins = int(input_time[3:5])
    output_secs = int(input_time[6:8])

    if (output_hours < 0 or output_hours > 23) or (output_mins < 0 or output_mins > 59) or (output_secs < 0 or output_secs > 59):
        print('Time must be between 00:00:00 and 23:59:59')
        error_flag = True

    if error_flag == False:
        output_seconds = calc_secs(output_hours, output_mins, output_secs) 
        return(output_seconds)




# Calculate the number of hours, minutes and seconds from the total number of seconds

def calc_hours_mins_secs(seconds):

    if seconds < 0 or seconds > 863990:
        print('Seconds must be between 0 and 863990')
    else:

        temp_time = 0
        hours = 0
        hours_text = ''
        mins = 0
        mins_text = ''
        secs = 0
        secs_text = ''

        nums = {'0' : '00','1' : '01','2' : '02','3' : '03','4' : '04','5' : '05','6' : '06','7' : '07','8' : '08','9' : '09'}

        hours = int(seconds / 3600)  # Calculate Hours
    
        if (hours < 10):
            hours_text = nums[str(hours)]
        else:
            hours_text = str(hours)
        
        temp_time = seconds - (hours * 3600) # Calculate Minutes
        mins = int(temp_time / 60)

        if (mins < 10):
            mins_text = nums[str(mins)]
        else:
            mins_text = str(mins)
        
        temp_time -= (mins * 60) # Calculate Seconds
        secs = int(temp_time)

        if (secs < 10):
            secs_text = nums[str(secs)]
        else:
            secs_text = str(secs)

        run_time = (hours_text, mins_text, secs_text)

        return(run_time)



# Calculate a timedelta from the number of hours, minutes and seconds or total number of seconds



def calc_timedelta(input_time):

    output_hours = 0
    output_mins = 0
    output_secs = 0
    output_time = [0,0,0]
    error_flag = False
    
    if type(input_time) == int:

        if input_time < 0 or input_time > 86399:
            print('Seconds must be between 0 and 86399')
            error_flag = True
        else:
            output_time = calc_hours_mins_secs(input_time)
            output_hours = int(output_time[0])
            output_mins = int(output_time[1])
            output_secs = int(output_time[2])
        
    elif type(input_time) == list or type(input_time) == tuple:

        output_hours = int(input_time[0])
        output_mins = int(input_time[1])
        output_secs = int(input_time[2])

        if (output_hours < 0 or output_hours > 23) or (output_mins < 0 or output_mins > 59) or (output_secs < 0 or output_secs > 59):
            print('Time must be between 00:00:00 and 23:59:59')
            error_flag = True

    elif type(input_time) == str:

        # Valid input 'HH:MM:SS'

        error_msg = 'Invalid Time - (HH,MM,SS) or [HH,MM,SS]'
        if len(input_time) != 8:
            print(error_msg)
            error_flag = True
        elif input_time[2] != ':' or input_time[5] != ':':
            print(error_msg)
            error_flag = True

        output_hours = int(input_time[0:2])
        output_mins = int(input_time[3:5])
        output_secs = int(input_time[6:8])

        if (output_hours < 0 or output_hours > 23) or (output_mins < 0 or output_mins > 59) or (output_secs < 0 or output_secs > 59):
            print('Time must be between 00:00:00 and 23:59:59')
            error_flag = True

    if error_flag == False:
        output_time_delta = datetime.timedelta(hours=output_hours, minutes=output_mins, seconds=output_secs)
        return(output_time_delta)
    


# DATE



# Converts a date and turns it into a number



def date_to_num(input_date):

    """ This function takes a date and turns it into a number

    The date can be in any of the following formats: -

        8 character string - YYYYMMDD
        Three item tuple (YYYY,MM,DD)
        Three item list [YYYY,MM,DD] 

    e.g.    January 1st 1900 / '19000101' / (1900,1,1) / [1900,1,1] will return 1
            January 1st 2000 / '20000101' / (2000,1,1) / [2000,1,1] will return 36525

    """


    calender = {
        0 : 0,
        1 : 31, # January
        2 : 28, # February
        3 : 31, # March
        4 : 30, # April
        5 : 31, # May
        6 : 30, # June
        7 : 31, # July
        8 : 31, # August
        9 : 30, # September
        10 : 31, # October
        11 : 30, # November
        12 : 31  # December
        }
    
    day_number = 0

    leap_year = False

    test_leap_year = 0

    test_month = 0




    # STRING
    # Extract Year, Month and Day from a string

    
    if type(input_date) == str:

        if input_date.lower() == 'today' or input_date.lower() == 'tomorrow' or input_date.lower() == 'yesterday':

            today = datetime.datetime.today()   # Extract date variables from today's date
            input_date = input_date.lower()     # Convert to lowercase

            year = int(today.strftime('%Y'))
            month = int(today.strftime('%m'))
            day = int(today.strftime('%d'))

        else:
            error_msg = '\nDate must be an 8 digit string in the following format - YYYYMMDD'

            date_string = input_date
        
            try:
                date_string_length = len(date_string)
            except TypeError:
                print(error_msg)
                return(0)
            except ValueError:
                print(error_msg)
                return(0)
        
            # Check Date is valid and in the correct format

            if date_string_length != 8:
                print(error_msg)
                return(0)

            # EXTRACT YEAR

            try:
                year = int(date_string[:4])
            except TypeError:
                print(error_msg)
                return(0)
            except ValueError:
                print(error_msg)
                return(0)

            # EXTRACT MONTH
    
            try:
                month = int(date_string[4:6])
            except TypeError:
                print(error_msg)
                return(0)
            except ValueError:
                print(error_msg)
                return(0)

            # EXTRACT DAY
        
            try:
                day = int(date_string[6:8])
            except TypeError:
                print(error_msg)
                return(0)


    # LIST or TUPLE
    # Extract Year, Month and Day from a list or tuple

        
    elif type(input_date) == tuple:

        error_msg = '\nDate must be a tuple in the following format - (YYYY,MM,DD)'
        
        date_list = []
        for i in input_date: # Convert the tuple into a list
            date_list.append(i)

        year =  int(date_list[0]) # Assign values from list to date variables
        month = int(date_list[1])
        day =   int(date_list[2])

    elif type(input_date) == list:

        error_msg = '\nDate must be a list in the following format - [YYYY,MM,DD]'
        
        year =  int(input_date[0]) # Assign values from list to date variables
        month = int(input_date[1])
        day =   int(input_date[2])

    elif type(input_date) == datetime.datetime:

        error_msg = '\nDate must be a datetime object in the following format - datetime.datetime(year=YYYY, month=MM, day=DD)'

        year =  input_date.year # Assign values datetime object list to date variables
        month = input_date.month
        day =   input_date.day

    else:

        error_msg = '\nDate must be a list in the following format - [YYYY,MM,DD]'
        print(error_msg)
        return(0)

        


# Validate Year

    if year < 1900 or year > 2099:
        print(error_msg)
        print('\nYear must be between 1900 and 2099')
        return(0)

# Validate month

    if month < 1 or month > 12:
        print(error_msg)
        print('\nMonth must be between 1 and 12')
        return(0)

# Validate day

    if (month == 2 and day == 29):
        test_month = 29
    else:
        test_month = int(calender[month])

    if day < 1 or day > test_month:
        print(error_msg)
        print('\nDay must be between 1 and ',calender[month])
        if month == 2:
            print('\nDay must be between 1 and  29 for a leap year')
        return(0)



    # CALCULATE THE DAY NUMBER
    
    # YEARS
    
    day_number = year * 365.25
              
    # Check to see if it's a leap year

    test_leap_year = day_number - int(day_number)

    if test_leap_year == 0 and year != 1900: # 1900 was not a leap year
        leap_year = True
        calender[2] += 1 # Add one day to February if it's a leap year
    else:
        if (month == 2 and day == 29):
            print(error_msg)
            print('\nDay must be between 1 and 28')
            return(0)
        leap_year = False

    day_number = int(day_number)

    day_number -= 693975 # This makes January 1st, 1900 Day 1
        
    if leap_year:           # If it's a leap year it's not known if it's February 29th yet
        day_number -= 1     # A day is therefore subtracted for the leap day that has already been added
                            # This is because we have only calculated as far as the beginning of the year 

    # MONTHS

    for check_month in range(1,month + 1):              # Go through the calender up until the requested month
        day_number += calender[check_month - 1]         # Add the days for the previous month (this will be 0 for January)
        if check_month == month:    
            day_number += day                           # When you get to the requested month, add the days for that month

    if input_date == 'tomorrow':
        day_number += 1 # Tomorrow, tomorrow I love you tomorrow. You're only a day away
        
    if input_date == 'yesterday':
        day_number -= 1 # Yesterday, all my troubles seemed so far away. Now it looks like they're here to stay
        
    return(day_number)
    




# DATE





def call_date_to_num(*args, **kwargs):

    """ This function takes a date and turns it into a number

    The date can be in any of the following formats: -

        Three variables YYYY, MM, DD
        
        Three Keywords
            Year=YYYY, Month=MM, Day=DD
            year=YYYY, month=MM, day=DD
            YYYY=YYYY, MM=MM, DD=DD
            yyyy=YYYY, mm=MM, dd=DD
            Y=YYYY, M=MM, D=DD
            y=YYYY, m=MM, d=DD

    e.g.    January 1st 1900 / 1900,1,1 / Year=1900, Month=1, Day=1 will return 1
            January 1st 2000 / 2000,1,1 / year=2000, month=1, day=1 will return 36525
            January 1st 1900 / 1900,1,1 / YYYY=1900, MM=1, DD=1 will return 1
            January 1st 2000 / 2000,1,1 / Y=2000, M=1, D=1 will return 36525
            January 1st 1900 / 1900,1,1 / yyyy=1900, mm=1, dd=1 will return 1
            January 1st 2000 / 2000,1,1 / y=2000, m=1, d=1 will return 36525

    """

    input_date = args
    input_date_dict = kwargs

    if input_date:
        output_date_num = date_to_num(input_date)
        return(output_date_num)

    if input_date_dict:
        output_date = [0,0,0]
        for item in input_date_dict:
            if item == 'Year' or item == 'year' or item == 'YYYY' or item == 'yyyy' or item == 'Y' or item == 'y' :
                output_date[0] = input_date_dict[item]
            elif item == 'Month' or item == 'month' or item == 'MM' or item == 'mm' or item == 'M' or item == 'm' :
                output_date[1] = input_date_dict[item]
            elif item == 'Day' or item == 'day' or item == 'DD' or item == 'dd' or item == 'D' or item == 'd':
                output_date[2] = input_date_dict[item]
            else:
                print('Incorrect key word used')
                return

    output_date_num = date_to_num(output_date)

    
        
    return(output_date_num)





# Converts a number into a date




def num_to_date(input_date_num):

    """ This function takes a number and turns it into a date

    The date is returned as a three item list [YYYY,MM,DD] 

    e.g.    1 will return January 1st 1900 / [1900,1,1]
            36525 will return January 1st 2000 / [2000,1,1] 

    """


    calender = {
        1 : 31, # January
        2 : 28, # February
        3 : 31, # March
        4 : 30, # April
        5 : 31, # May
        6 : 30, # June
        7 : 31, # July
        8 : 31, # August
        9 : 30, # September
        10 : 31, # October
        11 : 30, # November
        12 : 31  # December
        }

  
    date_num_year = 0
    date_num_month = 0
    date_num_day = 0
    
    leap_year = False
    test_leap_year = 0

    error_msg = 'Date number must be an interger between 1 (1st January 1900) and 73049 (31st December 2099!)'
    
    NYD_date_num = 0 # New Year's day / First day of the year

    # Validate date number

    if type(input_date_num) == str:
        try:
            date_num = int(float(input_date_num))
        except TypeError:
            print(error_msg)
            return(0,0,0)
        except ValueError:
            print(error_msg)
            return(0,0,0)
    elif type(input_date_num) == int:
        date_num = input_date_num
        if date_num < 1 or date_num > 73049:
            print(error_msg)
            return(0,0,0)
    elif type(input_date_num) == float:
        date_num = int(input_date_num) # Remove any decimal places from the inputed number
        if date_num < 1 or date_num > 73049:
            print(error_msg)
            return(0,0,0)
    else:
        print(error_msg)
        return(0,0,0)
              
    # Calculate the year

    date_num_year = int(date_num / 365.25)

    date_num_year += 1900

    # Is it a leap year?

    test_leap_year = (date_num_year / 4) - (date_num_year // 4)
    
    if test_leap_year == 0 and date_num_year != 1900: # 1900 was not a leap year
        leap_year = True
        calender[2] += 1  # Add one day to February if it's a leap year
    else:
        leap_year = False

    # Calculate the day number for January 1st for the year

    NYD_date_num = date_to_num([date_num_year,1,1])

    days_in_year = date_num - NYD_date_num # Calculate how many days old the year is
    days_in_year += 1 # A Day is added to include the date itself

    # Calculate the month and day

    # Go through the months of the year, subtracting the days for that month until you get to the correct month

    for calc_month in calender:
        if days_in_year <= calender[calc_month]:
            date_num_month = calc_month
            date_num_day = days_in_year
        else:
            days_in_year -= calender[calc_month]
        if date_num_day > 0: # Break out of the loop if you have arrived at the correct month
            break
                
    return([date_num_year,date_num_month,date_num_day])




# Find out what day of the week a date is




def day_of_week(input_date):

    """ Discover which day of the week a certain day falls on """

    day_name = {
        1 : 'Monday',       # Monday's Child is fair of face
        2 : 'Tuesday',      # Tuesday's Child is full of grace
        3 : 'Wednesday',    # Wednesday's Child is full of woe
        4 : 'Thursday',     # Thursday's Child has far to go
        5 : 'Friday',       # Friday's Child is loving and giving
        6 : 'Saturday',     # Saturday's Child works hard for a living
        0 : 'Sunday'        # But the child who is born on the Sabbath Day Is bonny and blithe, merry and gay
        }
        
    if (type(input_date) == str) or (type(input_date) == tuple) or (type(input_date) == list): # The user can pass in a date number, string, tuple or list
        date_num = date_to_num(input_date)
    else:
        date_num = int(input_date)

    if date_num < 1 or date_num > 73049:
        return('Date must be between 1st January 1900 and 31st December 2099!')
        
    # The reaminder of dividing the day number by the number of days in the week i.e. 7 will determine which day it is
    
    day_index = date_num // 7           # Divide date number by 7 and get rid of the decimal places

    day_index *= 7                      # Multiply this number by 7

    day_index = date_num - day_index    # This difference between these two numbers tells you which day it is
    
    return(day_name[day_index])



# Takes a date and turns it into text



def date_to_text(input_date):

    """ Takes a date and turns it into text

    e.g.    1 / [1900,1,1] / (1900,1,1) / '19000101' will return 'Monday, January 1st 1900'
            36525 / [2000,1,1 ] (2000,1,1) / '20000101' will return 'Saturday, January 1st 2000'

    """

    calender = {
        1 : 'January ',
        2 : 'February ',
        3 : 'March ',
        4 : 'April ',
        5 : 'May ',
        6 : 'June ',
        7 : 'July ',
        8 : 'August ',
        9 : 'September ',
        10 : 'October ',
        11 : 'November ',
        12 : 'December '
        }

    # Variables
    
    input_date_list = []

    weekday_text = ''
    month_text = ''
    day_text_1 = ''
    day_text_1 = ''
    year_text = ''

    output_date_list = []

    # Convert the date into a list depending on the input type
    
    # Year  - input_date_list[0]
    # Month - input_date_list[1]
    # Day   - input_date_list[2]

    if type(input_date) == int:
        input_date_list = num_to_date(input_date)
        
    elif type(input_date) == tuple:
        input_date_list.append(input_date[0])
        input_date_list.append(input_date[1])
        input_date_list.append(input_date[2])

    elif type(input_date) == list:
        input_date_list.append(input_date[0])
        input_date_list.append(input_date[1])
        input_date_list.append(input_date[2])

    elif type(input_date) == str:

        if input_date.lower() == 'today' or input_date.lower() == 'tomorrow' or input_date.lower() == 'yesterday':

            today = datetime.datetime.today()   # Extract date variables from today's date
            input_date = input_date.lower()     # Convert to lowercase

            input_date_list.append(int(today.strftime('%Y')))
            input_date_list.append(int(today.strftime('%m')))
            input_date_list.append(int(today.strftime('%d')))

            if input_date.lower() == 'tomorrow' or input_date.lower() == 'yesterday': # This is necessary in order to add / subtract 1 day
                input_date_num = date_to_num(input_date)
                input_date_list = num_to_date(input_date_num)

        else:
            input_date_list.append(int(input_date[0:4]))
            input_date_list.append(int(input_date[4:6]))
            input_date_list.append(int(input_date[6:8]))
    
    if type(input_date) != int and date_to_num(input_date) < 1: # This checks the date is valid
        return('\nThat is an invalid date')

    # Extract the various date components and convert into text
    
    weekday_text = day_of_week(input_date_list) + ', '  # Day of week

    month_text = calender[input_date_list[1]]           # Month

    day_text_1 = str(input_date_list[2])                # Day

    if input_date_list[2] == 1 or input_date_list[2] == 21 or input_date_list[2] == 31:
        day_text_2 = 'st '
    elif input_date_list[2] == 2 or input_date_list[2] == 22:
        day_text_2 = 'nd '
    elif input_date_list[2] == 3 or input_date_list[2] == 23:
        day_text_2 = 'rd '
    else:
        day_text_2 = 'th '

    year_text = str(input_date_list[0])                 # Year

    # Put components together in a list

    output_date_list.append(weekday_text)               # The Function returns the components seperatley
    output_date_list.append(month_text)
    output_date_list.append(day_text_1+day_text_2)
    output_date_list.append(year_text)

    output_date_list.append(weekday_text+month_text+day_text_1+day_text_2+year_text) # The Functions also combines the components into one text string
    
    return(output_date_list)
    


# Takes a date and turns it into a datetime object




def date_to_datetime(input_date):

    if type(input_date) == int:
        output_date = num_to_date(input_date)
        output_year = output_date[0]
        output_month = output_date[1]
        output_day = output_date[2]
        
    elif type(input_date) == tuple or type(input_date) == list:
        output_year = int(input_date[0])
        output_month = int(input_date[1])
        output_day = int(input_date[2])

    elif type(input_date) == str:

        if input_date.lower() == 'today' or input_date.lower() == 'tomorrow' or input_date.lower() == 'yesterday':

            today = datetime.datetime.today()   # Extract date variables from today's date
            input_date = input_date.lower()     # Convert to lowercase

            output_year = int(today.strftime('%Y'))
            output_month = int(today.strftime('%m'))
            output_day = int(today.strftime('%d'))
            
            if input_date.lower() == 'tomorrow' or input_date.lower() == 'yesterday': # This is necessary in order to add / subtract 1 day
                input_date_num = date_to_num(input_date)
                input_date_list = num_to_date(input_date_num)
                output_year = input_date_list[0]
                output_month = input_date_list[1]
                output_day = input_date_list[2]
            
        else:
            output_year = int(input_date[0:4])
            output_month = int(input_date[4:6])
            output_day = int(input_date[6:8])

    else:
        return('\nThat is an invalid date')

    if type(input_date) != int and date_to_num(input_date) < 1: # This checks the date is valid
        return('\nThat is an invalid date')
    else:
        return(datetime.datetime(year=output_year, month=output_month, day=output_day)) # Return datetime object




def _test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    _test()

