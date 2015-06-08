# -*- coding: utf-8 -*-

"""
    times_and_dates.py - Advanced Topics 5 - Time and Dates in Python
"""

import time
import datetime

"""
    At its core, all times in Python are determined by the number of seconds since what is 
    called the UNIX epoch, which started arbitrarily at Jan 1, 1970.  We gotta start somewhere
"""

# This gives us the exact UNIX timestamp as defined above
print "Right now is: {} since the UNIX epoch".format(time.time())  

"""
    This, however, can be a little unruly for most people to stare at, it ignores many human level
    time and date interactions (ie Hour, Day, Year, Timezone, etc).  Thus the datetime module.
    
    The datetime module contains a few key objects, datetime.datetime, datetime.date, and datetime.timedelta
    datetime is the object to work with date/times (ie 3:45 Feb 6, 2015),
    date is a simplified version of datetime ignoring the time
    timedelta is a difference between two datetime objects
"""

print "Right now, datetime: {}".format(datetime.datetime.now())
print "When working with servers, use utcnow(): {}".format(datetime.datetime.utcnow())

# raw_input("More...")
print

"""
    Date and Datetime objects can be created manually by passing in relevant date and time arguments
"""

my_birthday = datetime.date(1981, 06, 07)
my_exact_birthday = datetime.datetime(1981, 06, 07, 19, 17)

print
print "I was born on {}".format(my_birthday)
print "I was really born at {}".format(my_exact_birthday)

"""
    Addition / Subtraction operators with datetimes use the timedelta objects
"""
today = datetime.date.today()
my_age = today - my_birthday
print "This means I am {}".format(today - my_birthday)

"""
    Timedelta objects let you extract the information you want in certain steps, days, seconds, microseconds
"""

print "In human terms, I am {} years old".format(my_age.days / 365)

# raw_input("More...")

"""
    You can format a datetime object to whatever form you wish using defined codes and your current locale, ie:
        %a:     Day of week     Sun, Mon, Tues
        %A:                     Sunday, Monday, Tuesday
        %d:     Day of Month    01, 02, 03, ..., 31
        %b:     Month           Jan, Feb, Mar
        %B:                     January, February, March
        %y:     Year            01, 12
        %Y:                     2001, 2012
        %I:     Hour            01, 02, ..., 12
        %M:     Minute          01, 02, ..., 60
        
    There are many more, check the docs
"""
print
print "Today is: {}".format(today.strftime('%b %d, %Y'))

"""
    A little trickier, but very useful is the ability to parse a date string to a datetime object
"""

some_day = datetime.datetime.strptime('Feb 02, 2015', '%b %d, %Y')
some_day_td = datetime.datetime.now() - some_day
print "Some day is {} which was {} days ago".format(some_day, some_day_td.days)