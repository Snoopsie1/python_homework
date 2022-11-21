from datetime import datetime, date, time
import random

"""
Welcome to myUtilities module. This is a module made in a class exercise
Here is its requirements:
- the function must take 4 arguments (period_as_timedelta, time_of_day, number_of_meetings, start_date=now())
- the function should then return a list of datetimes for a series of meetings that should take place from start_date and evenly distributed throughout the period.
- create another list of number of attendents, that was actually there at each meeting.
- create a bar plot of attendance through the series of meetings.
"""
#Ved ærlig talt ikke helt hvordan det skal struktureres
def arrange_meetings(period_as_timedelta, time_of_day, number_of_meetings, start_date):
        print("myAss")
        list_of_meetings = []
        first_meeting = start_date
        for day in range(period_as_timedelta.days):
                while number_of_meetings > 0:

                        list_of_meetings.append()
