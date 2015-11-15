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
In this module you will define several functions.

Please document your functions according to
https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
'''

# Example so that you can see a passing test


def f():
    """Returns the string 'success'
    """
    return "success"

##############################
# Basic function definitions #
##############################

# Define a function named add that takes two numbers and returns the sum.

def add(a,b):
    """ Adds two numbers
	
    Parameters
    ----------
    a,b : int,float
		
    Returns
    -------
    Int, float
		a+b
    """
    return a+b
    
# Define a function named to_tuple that takes three arguments and returns a
# tuple of these three arguments.

def to_tuple(a,b,c):
    """ Creates a tuple out of 3 variables
	
    Parameters
    ----------
    a,b,c: any type
	
    Returns
    -------
    tuple
		(a,b,c)
    """
    return (a,b,c)
    
# Define a function named check5 that checks if a number is greater than 5 and
# returns True or False.

def check5(a):
    """Returns 'True' if a is greater than 5, otherwise it return 'False'.
    
    Parameters
    ----------
    a: int, float
    
    Returns
    -------
    True
		when a is greater than 5
    False
		when a isn't greater than 5
		
    Examples
    --------
    >>> print(check5(4))
    False
    >>> print(check5(6))
    True
    >>> print(check5(5))
    False
    """
    return a>5

# Define a function named check_n that check is a number is greater than n. The
# number should be the first argument and n the second

def check_n(a,n):
    """ Returns 'True' if a is greater than n, otherwise it return 'False'.
    
    Parameters
    ----------
    a,n: int, float
    
    Returns
    -------
    True
		when a is greater than n
    False
		when a isn't greater than n
		
    
    See Also
    --------
    check5(a)
    
    Examples
    --------
    >>> print(check_n(4,3))
    True
    """
    return a>n

#########
# LISTS #
#########

# Define a function named check_list that takes two arguments. The first
# argument is a list of numbers and the second argument is the number n to
# compare against. The function should return a list with equal length as the
# input list containing for each number in the original list either True or
# False if the number was greater than or equal to n.

def check_list(numberlist,n):
    """ Check if each value in list is greater or equal to n.
    	
    Parameters
    ----------
    numberlist: list
		Type of elements: number
    n: int, float
    
    Returns
    -------
    List
		Elements with True or False
    
    See Also
    --------
    check5(a)
    check_n(a,n)
    
    Examples
    --------
    >>> print(check_list([1,2,5,10],3))
    [False,False,True,True]
    """
    return [value>=n for value in numberlist]

# Define a function named check_list_nth that does the same as check_list but
# uses every nth element of the input list (including the first one). You will
# need a third input argument.

def check_list_nth(numberlist,n,nth):
    """ Check if every nth element in list is greater or equal to n.
    	
    Parameters
    ----------
    numberlist: list
		type of elements: number
    n: int, float
    nth: int
    
    Returns
    -------
    List
		Elements with True or False
    
    See Also
    --------
    check5(a)
    check_n(a,n)
    check_list(numberlist,n)
    
    Examples
    --------
    >>> print(check_list_nth([1,2,10,4,5,6,7,10],5,3))
    [False,False,True]
    """
    return [value>=n for value in numberlist[0::nth]]
   
# Define a function named add_new_list that takes two inputs. A list l and a
# second variable x to add to the list. Return a new list containing x as the
# last element without modifying the original list.

def add_new_list(l,x):
    """ Creates a copy of list l and adds the element x
    	
    Parameters
    ----------
    l: list
    x: any
    
    Returns
    -------
    List
    
    Examples
    --------
    >>>l = [1,2,3,'tt']
    >>>l2 =  add_new_list(l,3)
    >>>print(l)
    [1,2,3,'tt']
    >>>print(l2)
    [1,2,3,'tt',3]
    """
    l_copy = list(l)
    l_copy.append(x)
    return l_copy

# Define a function named remove_nth that takes a list and removes every nth
# element (including the first one). Use a keyword named nth to set the default
# value for nth to 2.

def remove_nth(l,nth=2):
    """ Deletes every nth element in list l
    	
    Parameters
    ----------
    l: list
    nth: int, optional
    
    Returns
    -------
    List
    
    Examples
    --------
    >>>print(remove_nth([1,2,3,4,5,6],3))
    [2,3,5,6]
    """
    l_copy = list(l)
    del l_copy[::nth]
    return l_copy

# Define a function named search_n that takes a list and a variable x and
# searches for x in the list. If the variable is found return the index of the
# variable in the list and the variable. Otherwise use None for both return
# values

def search_n(l,x):
    """ Search for the first x in list l and returns a tuple with index and value. It only returns the first found value.
    	
    Parameters
    ----------
    l: list
    x: any
    
    Returns
    -------
    List
    
    Examples
    --------
    >>>print(search_n([1,2,3,4,5,3,6],3))
    (2,3)
    """
    erg = (None,None)
    for idx,value in enumerate(l):
        if value == x:
            erg = (idx,value)
            break
    return erg

################
# Dictionaries #
################

# Define a function named args_to_dict that takes three arguments and returns a
# dictionary with the position of the argument as the key (starting at 0) and
# the argument as the value.

def args_to_dict(a,b,c):
    """ Creates a dictionary with 3 entries, keys: index, value: arguments
    	
    Parameters
    ----------
    a,b,c: any type
    
    Returns
    -------
    Dictionary
    
    Examples
    --------
    >>>print(args_to_dict(1,'22',4.6))
    {0:1,1:'22',2:4.6}
    """
    return {0:a,1:b,2:c}

# BONUS: Write a function named args_to_dict_general that does the same for any
# number of arguments
def args_to_dict_general(*args):
    """ Creates a dictionary with any number of arguments, keys: index, value: arguments
    	
    Parameters
    ----------
    args: any type
    
    Returns
    -------
    Dictionary
    
    See Also
    --------
    args_to_dict(a,b,c)
    
    Example
    -------
    >>>print(args_to_dict_general(1,'22',4.6,'ttt'))
    {0:1,1:'22',2:4.6,3:'ttt'}
    """
    #return dict(zip(range(0,len(args)),args))
    return {i:j for i,j in enumerate(args)}

# Define a function named lists_to_dict that takes two lists of equal lenght
# named keys and values and builds a dictionary out of them.

def lists_to_dict(keys,values):
    """ Creates a dictionary out of two lists with same length
    	
    Parameters
    ----------
    keys,values: any type
		Have to have same length
    
    Returns
    -------
    Dictionary
    
    See Also
    --------
    args_to_dict(a,b,c)
    args_to_dict_general(*args)
    
    Example
    -------
    >>>print(lists_to_dict([0,'aa',3],['22','d',2]))
    {0:'22','aa':'d',3:2}
    """
    return dict(zip(keys,values))

# Define a function named search_list that takes two lists a and b. The
# function searches for all elements of b in list a. The return value should be
# a dictionary containing the index of the found element of b in list a and the
# value of the found element. If nothing was found then return an empty
# dictionary.

def search_list(a,b):
    """ Creates a dictionary with elements which are in list a and list b, key: index of the element in list a
    	
    Parameters
    ----------
    a,b: list
		element: any type
    
    Returns
    -------
    Dictionary
    
    Example
    -------
    >>>print(search_list([1,2,3,4,5,6,7,8],[1,4]))
    {0:1,3:4}
    """
    r_dict = {}
    for idx,i in enumerate(a):
        for j in b:
            if  i == j:
                r_dict[idx] = i
    return r_dict

# Define a function named dict_to_string that takes a dictionary and a
# separator string. The function should only take elements out of the
# dictionary whose value is a string and then return a single string containing
# the strings stored in the dictionary seperated by the separator string.
# Return an empty string if there are no strings in the dictionary.

def dict_to_string(adict,sep):
    """ Creates a string out of the values in dictionary adict which are strings, this elements will be seperated by sep
    	
    Parameters
    ----------
    adict: dictionary
    sep: string
    
    Returns
    -------
    String
    
    Example
    -------
    >>>print(dict_to_string({0:'hi','a':1,'c':'ho'},'AND'))
    'hiANDho'
    """
    s = ''
    for value in adict.values():
        if isinstance(value, str):
            if s == '':
                s = value
            else: 
                s = s+sep+value
    return s

# Define a function named classify_by_type which takes a list l and returns a
# dictionary d. The d must have the keys 'int' and 'str' which contain the
# elements out of l that have this type. Elements that do not fit one of these
# two types should be stored in a list under the key 'others'

def classify_by_type(l):
    """ Creates a Dictionary where the elements of list l are sorted after types int, str and others
    	
    Parameters
    ----------
    l: list
    
    Returns
    -------
    Dictionary
    
    Example
    -------
    >>>print(classify_by_type([1,4,5.6,'33']))
    {'int':[1,4],'str':['33'],'others':[5.6]}
    """
    int_val, str_val, other_val = [],[],[]
    for i in l:
        if type(i) is int:
            int_val.append(i)
        elif type(i) is str:
            str_val.append(i)
        else:
            other_val.append(i)
    return {'int':int_val, 'str':str_val, 'others':other_val}