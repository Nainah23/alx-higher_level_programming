#!/usr/bin/python3
"""Definesafnthatprintsmyname"""
defsay_my_name(first_name,last_name=""):
"""Printsmyname

Args:
first_name(str):firstname
last_name(str):lastname
Raises:
TypeError:ifeithernamesisnotastring
"""
ifnotisinstance(first_name,str):
raiseTypeError("first_namemustbeastring")
ifnotisinstance(last_name,str):
raiseTypeError("last_namemustbeastring")
print("Mynameis{}{}".format(first_name,last_name))
