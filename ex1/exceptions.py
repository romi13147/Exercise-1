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
Module for testing exception handling
'''

######################
# Raising Exceptions #
######################

# Use the function search_n from the functions module inside a new function
# also named search_n. The function should do the same as functions.search_n
# but if the variable is not found in the list then raise a ValueError.

def search_n(l,x):
""" Search for the first x in list l and returns a tuple with index and value.
	It only returns the first found value. If no value was found a ValueError Exception will raise.
	
Parameters
----------
l: list
x: any

Returns
-------
List

Examples
--------
>>>search_n([1,2,3,4,5,3,6],3)
(2,3)
"""
idx = l.index(x)
return (idx,l[idx])


########################
# Excepting Exceptions #
########################

# Define a function called safe_divide which takes two arguments and divides
# the first by the second. This function should handle exceptions that might
# occur print out what went wrong and return None if no results could be
# computed.

def safe_divide(a,b):
""" Devides a/b. It returns None with wrong argument type and Devision by 0 
	
Parameters
----------
a,b: number (b!=0)

Returns
-------
Float

Examples
--------
>>>safe_divide(5,2)
2.5
"""	
try:
	return a/b
except TypeError:
	return None
except ZeroDivisionError:
	return None