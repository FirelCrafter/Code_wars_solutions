import re


regex = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[A-Za-z/d]{6,}$', re.VERBOSE)
