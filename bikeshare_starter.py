import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
VALID_MONTHS = [
    "january", "february", "march", "april", "may", "june",
    "july", "august", "september", "october", "november", "december"
]

VALID_DAYS = [
    "monday", "tuesday", "wednesday", "thursday", 
    "friday", "saturday", "sunday"
]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # get user input for city (chicago, new york city, washington).
    while True:
        city = input("Please input City (Chicago, New York City or Washington): ").strip().lower()
        if city in CITY_DATA:
            break
        print("Invalid city! Please choose Chicago, New York City or Washington.")
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please input month (all, january, february, ...): ").strip().lower()
        if month == 'all' or month in VALID_MONTHS:
            break
        print("Invalid input! Please type 'all' or a valid month.")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please input day (all, monday, tuesday, ...): ").strip().lower()
        if day == 'all' or day in VALID_DAYS:
            break
        print("Invalid input! Please type 'all' or a valid day.")
    

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
    try:
        df = pd.read_csv(CITY_DATA[city.lower()])

        # Convert the 'Start Time' column to datetime objects
        df['Start Time'] = pd.to_datetime(df['Start Time'])

        # Extract month and day of week from Start Time to create new columns
        df['month'] = df['Start Time'].dt.month_name()

        df['day_of_week'] = df['Start Time'].dt.day_name()

        if month != 'all':
            df = df[(df['month'].str.lower() == month)]
                    
        if day != 'all':
            df = df[(df['day_of_week'].str.lower() == day)]
        
        return df
    except FileNotFoundError:
        print(f"Error: The CSV file for '{city}' was not found.")
        return None


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()