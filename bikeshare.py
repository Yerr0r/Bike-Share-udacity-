import time
import pandas as pd
import math
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

# Creating two list to store week_days and months.
months = ['january' , 'february' , 'march' , 'april' , 'may', 'june' ,'all']
week_days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'sunday' , 'all']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # Running this loop to ensure the correct user input gets selected or repeat all over again.
    while True:
        # get user input for city (chicago, new york city, washington)
        print("\nWould you like to take a look on which city data..Chicago, New York, or Washington?")
        city = input().strip().lower()
        #Check if input not correct or not if not print msg for the user.
        if city in CITY_DATA.keys():
            break
        else:
            print("\nPlease check your input, it doesn\'t appear to be conforming to any of the accepted input formats.")
    # Running this loop to ensure the correct user input gets selected or repeat all over again.
    while True:
        print("\nWould you like to filter output data with day or month or both or none..?")
        user_input = input().strip().lower()
        # ask user to filter data by month, day, both, or none
        if user_input == 'month':
            # get user input for month (all, january, february, ... , june)
            print("\nwhich month you would like to see result of - January, February, March, April, May, or June:")
            month = input().strip().lower()
            # check if month is in months
            while month not in months:
                print("\nPlease check your input, it doesn\'t appear to be conforming to any of the accepted input formats.")
                month = input('Please take your time and put valid input ... :  ')
            else:
                day = "all"
            break

        elif user_input == 'day':
            # get user input for day of week (all, monday, tuesday, ... sunday)
            print('which day you would like to see result of - saturday,sunday,monday,tuesday,..(Please Type)?')
            day = input().strip().lower()
            # check if day is in days
            while day not in week_days:
                print("\nPlease check your input, it doesn\'t appear to be conforming to any of the accepted input formats.")
                day = input('Please take your time and put valid input ... :  ')
            else:
                month = "all"
            break

        elif user_input == 'both':
            # get user input for month (all, january, february, ... , june)
            month = input('Which month? January, February, March, April, May, June or All? : ').strip().lower()
            while month not in months:
                print("\nPlease check your input, it doesn\'t appear to be conforming to any of the accepted input formats.")
                month = input('Please take your time and put valid input ... :  ')
                # get user input for day of week (all, monday, tuesday, ... sunday)
            day = input('Which day?  Sunday, Monday, Tuesday, Wednesday.....Saturday or All ? : ').strip().lower()
            # check if month in months and day in days
            while day not in week_days:
                print('\n Day not valid')
                day = input('Enter day again...:')
            break

        elif user_input == 'none':
            month = "all"
            day = "all"
            break
        else:
            print("\nPlease check your input, it doesn\'t appear to be conforming to any of the accepted input formats.")
            pass

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['week_days'] = df['Start Time'].dt.day_name()
    # Filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    # Filter by day of week if applicable
    if day != 'all':
        df = df[df['week_days'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    common_month= df['month'].value_counts().idxmax()
    # Print with Formatted string literals.
    # we used months[month -1] so we can pick month name instead of month number
    print(f'The most common month is:{months[common_month-1]} ')

    # TO DO: display the most common day of week
    common_day = df['week_days'].value_counts().idxmax()
    # Print with Formatted string literals.
    print(f'the most common day is:{common_day}')

    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most common hour
    common_start_Hour = df['hour'].value_counts().idxmax()
    # Print with Formatted string literals.
    # Check if ocommon_start_Hour less than 10 so we add 0 and AM to just look like that 09:00AM
    if common_start_Hour < 10:
        print(f"The most common start hour is:0{common_start_Hour}:00AM")
    elif common_start_Hour <= 12:
        print(f"The most common start hour is:{common_start_Hour}:00AM")
    else:
        print(f"The most common start hour is:{common_start_Hour}:00PM")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    # Uses value_counts().idxmax() method to find the most common start station
    commonly_used_start_station= df['Start Station'].value_counts().idxmax()
    # Print with Formatted string literals.
    print(f'The most commonly used start station is:{commonly_used_start_station}. ')

    # TO DO: display most commonly used end station
    # Uses value_counts().idxmax() method to find the most common end station
    commonly_used_end_station = df['End Station'].value_counts().idxmax()
    # Print with Formatted string literals.
    print(f'The  most commonly used end station is:{commonly_used_end_station}. ')

    # TO DO: display most frequent combination of start station and end station trip
    # Here we can use alot of good methods like .
    # .size() (sizes.idxmax(), sizes.max())
    #df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    #df.groupby(['Start Station', 'End Station']).size().idxmax()
    # But i think use size() and sort_values return more clear data so i used it.

    df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # #Calculating the total trip duration using sum method and print it in dd:hh:mm:ss.
    total_travel_duration = df['Trip Duration'].sum()
    day = total_travel_duration // (24 * 3600)
    total_travel_duration = total_travel_duration % (24 * 3600)
    hour = total_travel_duration // 3600
    total_travel_duration %= 3600
    minutes = total_travel_duration // 60
    total_travel_duration %= 60
    seconds = total_travel_duration

    print("Total travel time is:\nd:H:M:S-> \n%d:%d:%d:%d" % (day, hour, minutes, seconds))
    # TO DO: display mean travel time
    # Calculating the average trip duration using mean method and print it in dd:hh:mm:ss.
    travel_time_mean = df['Trip Duration'].mean()
    weeks = total_travel_duration / (7 * 24 * 60 * 60)
    day = travel_time_mean // (24 * 3600)
    travel_time_mean = travel_time_mean % (24 * 3600)
    hour = travel_time_mean // 3600
    travel_time_mean %= 3600
    minutes = travel_time_mean // 60
    travel_time_mean %= 60
    seconds = travel_time_mean
    # Print with Formatted string literals.

    print("Mean travel time is:\nd:H:M:S-> \n%d:%d:%d:%d" % (day, hour, minutes, seconds))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    # Print with Formatted string literals.
    print(f'counts of user types is: \n{user_type_count} \n')
    # TO DO: Display counts of gender
    # This try clause is implemented to display the numebr of users by Gender coz of washington file dose not have gender column.
    try:
        count_of_gender = df['Gender'].value_counts()
         # Print with Formatted string literals.
        print(f'counts of user gender is: \n{count_of_gender}\n')
    except:
         print("This file dose not have 'Gander' column ")
         # TO DO: Display earliest, most recent, and most common year of birth
         # Also here repet this try clause is implemented to display the numebr of users by Gender coz of washington file dose not have year of birth column.
    try:
       earliest_year =df['Birth Year'].min()
       most_recent_year=df['Birth Year'].max()
       most_common_year= df['Birth Year'].value_counts().idxmax()
       # Print with Formatted string literals.
       #add math.trunc to remove dicimal values
       print(f'The earliest Year is:{ math.trunc(earliest_year)} \nThe most recent year is:{math.trunc(most_recent_year)} \nThe most common year is:{math.trunc(most_common_year)} ')
    except:
        print("There are no birth year details in this file.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    """Displays raw data on user request."""
    print("Would you like to see a sample of data... 'Yes , No'")
    #Take user answer as input
    answer = input().lower()
    #Cheack is user input match or not
    if answer == 'yes':
        #Print Data head.
        print(df.head())
    value = 0
    #loop to keep check user want more data or not
    while True:
        #Take user input
        view_raw_data = input('\nDo you want extra 5 row of raw data? Enter yes or no.\n')
        # Cheack is user input match or not
        if view_raw_data.lower() == 'no':
            return

        elif view_raw_data.lower() == 'yes':
            value += 5
            print(df.iloc[value:value + 5])
        else:
            print("\nPlease check your input, it doesn\'t appear to be conforming to any of the accepted input formats.")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()

