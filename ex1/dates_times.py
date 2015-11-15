# Copyright (c) 2015,Vienna University of Technology,
# Department of Geodesy and Geoinformation
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#   * Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the Vienna University of Technology,
#      Department of Geodesy and Geoinformation nor the
#      names of its contributors may be used to endorse or promote products
#      derived from this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL VIENNA UNIVERSITY OF TECHNOLOGY,
# DEPARTMENT OF GEODESY AND GEOINFORMATION BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''
Exercises for using the datetime and the calendar module
'''
from datetime import date, time, datetime, timedelta
import calendar

# Define a function named last_of_month that takes an argument dt of type date
# and returns a date object representing the last day of the month dt was in.

def last_of_month(dt):
	""" Creates a datetime.date object with the last day of month
		
	Parameters
	----------
	dt: datetime.date object
	
	Returns
	-------
	datetime.date object
		Last day of the month
	
	Example
	-------
	>>>print(last_of_month(date(2015,10,3)))
	2015-10-31
	"""
	day = calendar.monthrange(dt.year,dt.month)[1]
	return date(dt.year,dt.month,day)

# Define a function named feed_the_gremlin which takes a time object as an
# argument. It should return False between midnight and 6:30AM and True
# otherwise.

def feed_the_gremlin(dt):
	""" Returns true if the time dt isn't in the timespan 0:01 to 6:29
		
	Parameters
	----------
	dt: datetime.time object
	
	Returns
	-------
	True
		when dt not in timespan 0:01 to 6:29
	False
		dt is in timespan 0:01 to 6:29
		
	Example
	-------
	>>>print(feed_the_gremlin(time(5)))
	False
	>>>print(feed_the_gremlin(time(6,30)))
	True
	>>>print(feed_the_gremlin(time(0)))
	True
	"""
	if dt < time(6,30) and dt > time(0,0):
		return False
	else:
		return True
        
# Define a function named how_long that takes two datetime objects dt and ref
# where ref is the reference datetime, calculates the difference between them and
# returns the difference as a string formatted like:
# "01 days, 01 minutes, 01 seconds until 2000-12-31 15:59:59"
# If ref is before dt then use 'since' instead of 'until'
        
def how_long(dt,ref):
    """ Returns time difference between dt and ref as string
    		
    Parameters
    ----------
    dt,ref: datetime.datetime object
    
    Returns
    -------
    String
    	
    Example
    -------
    >>>print(how_long(datetime(2015,12,23,12,0,0),datetime(2016,1,1)))
    '8 days, 0 minutes, 0 seconds until 2016-01-01 0:00:00'
    """
    dif = ref-dt
    if dif.days < 0:
        dif = dt-ref
        prep = 'since'
    else:
        prep = 'until'
    #hour = dif.seconds//3600 # Why without hours???
    minute = (dif.seconds//60)%60
    second = dif.seconds%60
    #return "{} days, {} hours, {} minutes, {} seconds {} {}".format(dif.days,hour,minute,second,prep,ref)
    return "{} days, {} minutes, {} seconds {} {}".format(dif.days,minute,second,prep,ref)