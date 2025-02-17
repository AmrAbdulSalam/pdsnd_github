import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = input('Enter the city you want see data for Chicago, New York city, Washington : ')
    city = city.casefold()
    while city not in CITY_DATA:
        city = input('Please Try Again')
        city = city.casefold()
    
    month = input('Please enter a month between January and June or choose "all" .... ')
    month = month.casefold()
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    
    while month not in months:
        month = input('Please Try Again')
        month = month.casefold()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = input('Enter a weekday or choose "all" .....')
    day = day.casefold()
    while day not in days:
        day = input('Invalid day name.Please Try Again!')
        day = day.casefold()

    print('-'*40)
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
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
   
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        # Useing the index of the months list to get corresponding integer
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # Filtering by month to create new dataframe
        df = df[df['month'] == month]

        
        
    # Filtering by day of week if applicable
    if day != 'all':
        # Filtering by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    
    popular_month = df['month'].mode()[0]
    
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    
    print('Most Common Month:', months[popular_month - 1])

    
    df['day_of_week'] = df['Start Time'].dt.dayofweek
   
    popular_day = df['day_of_week'].mode()[0]
    
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    print('Most Common Day:', days[popular_day])

    df['hour'] = df['Start Time'].dt.hour
    
    popular_hour = df['hour'].mode()[0]
    
    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    most_visited_start_station = df['Start Station'].mode()[0]
    print('Most visited station is : ' , most_visited_start_station)
    
    most_visited_end_station = df['End Station'].mode()[0]
    print('Most visited station is : ' , most_visited_end_station)


    most_visited_start_end_station = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('Most frequent combination of start station and end station trip : ' , most_visited_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time : ' , total_travel_time)

    average_travel_time = df['Trip Duration'].mean()
    print('Average travel time : ' , average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    count_user_type = df['User Type'].value_counts()
    print(count_user_type)

    if 'Gender' in df.columns:    
        gender = df['Gender'].value_counts()
        print(gender)

    if 'Birth Year' in df.columns:
        print('Earliest year of Birth:', df['Birth Year'].min())
        print('Most Recent year of Birth:', df['Birth Year'].max())
        print('Most Common year of Birth:', df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        enter = ['yes','no']
        user_input = input('Would you like to see more data?')
        
        while user_input.lower() not in enter:
            user_input = input('Please try again')
            user_input = user_input.lower()
        x = 0        
        while True :
            if user_input.lower() == 'yes':
        
                print(df.iloc[x : x + 5])
                x += 5
                user_input = input('Would you like to see more data? ')
                while user_input.lower() not in enter:
                    user_input = input('Please try again')
                    user_input = user_input.lower()
            else:
                break 
                
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('program ended ... ')
            break


if __name__ == "__main__":
	main()
