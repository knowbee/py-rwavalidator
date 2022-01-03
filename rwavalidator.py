#!/usr/bin/env python
import re
import datetime
now = datetime.datetime.now()

def isNationalId(id):
    ID_LENGTH=16
    minAge = 16
    pattern = r'^[1-3](19|20)\d{2}[7-8]\d{7}[0-9]\d{2}$'
    regex = re.compile(pattern)
    try:
        if (len(id) < ID_LENGTH):
            return False
        if (len(id) > ID_LENGTH):
            return False
        if(now.year - int(id[1:5]) < minAge):
            return False
        match = regex.search(id)
        if not match:
            return False
        return True 
    except TypeError:
        return "Input should be string"

def isPhoneNumber(number):
    pattern = r'^(\+?25)?(078|079|075|073|072)\d{7}$'
    regex = re.compile(pattern)
    match = regex.search(number)
    if not match:
        return False;
    return True
