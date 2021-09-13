import calendar
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
    while True:
        city=input("Which of these cities(chicago, new york city, washington) you would like to filter? \n ").lower()
        if city not in ["chicago", "new york city", "washington"]:
            print("The data you entered is wrong")
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input("which of these months(all, january , february, march, april, may, june,) you would like to filter? \n ").lower()
        if month not in ["all", "january" , "february", "march", "april", "may", "june",]:
            print("The data you entered is wrong")
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input("which of these days (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday) you would like to filter? \n").lower()
        if day not in ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
           print("The data you entered is wrong")
        else:
            break
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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months=  months = ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month = df['month'].mode()[0]
    print('The most Frequent month: {}'.format(calendar.month_name[popular_month]))


    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The most Frequent day: {}'.format(popular_day))


    # TO DO: display the most common start hour
    df['hour'] = df["Start Time"].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most Frequent Start Hour: {}'.format(popular_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most Frequent Start Station: {}'.format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station= df["End Station"].mode()[0]
    print('The most Frequent End Station: {}'.format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    popular_start_end= (df["Start Station"]+ " - "+ df["End Station"]).mode()[0]
    print("The most frequent combination of start station and end station trip: {}".format(popular_start_end))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time= df["Trip Duration"].sum()
    print("Total travel time: {}".format(total_travel_time))
    # TO DO: display mean travel time
    mean_travle_time= df["Trip Duration"].mean()
    print("Mean travel time: {}".format(mean_travle_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types= df["User Type"].value_counts()
    print("\nCounts of user types: {}".format(counts_of_user_types))

    # TO DO: Display counts of gender
    if "Gender" in df:
      counts_of_gender=df["Gender"].value_counts()
      print("Counts of gender: {} \n".format(counts_of_gender))
    else:
      print('Gender stats cannot be calculated because Gender does not appear in the dataframe')


    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
     earliest_year_of_birth= df["Birth Year"].min()
     print("The earliest year of bith: {}".format(earliest_year_of_birth))
     recent_year_of_birth= df["Birth Year"].max()
     print("The most recent year of bith: {}".format(recent_year_of_birth))
     common_year_of_birth= df["Birth Year"].mode()[0]
     print("The most common year of birth: {} " .format(common_year_of_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df) :
    start_loc = 0
    while True:
        view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no? \n").lower()
        if view_data=="yes":
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
        else:
            break
            view_display = input("Do you wish to continue?: \n").lower()
            if view_display !="yes":
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
