# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 01:21:07 2019

@author: User
"""
#import necessary libraries for re and regex
import re
import regex

email_validator = re.compile('[a-z]+')
print(email_validator.match('schoolofaiBellevue'))

#lets try to twist the above code
email_validator = re.compile('[a-z]')
print(email_validator.match('schoolofaiBellevue'))