#!/usr/bin/python3
"""Definesanaddfnforintergers"""
defadd_integer(a,b=98):
"""Addsaandb
ifafloat,convertfirsttoint
Raise:
TypeErrorifnotaninteger
"""
if((notisinstance(a,int)andnotisinstance(a,float))):
raiseTypeError("a,mustbeninteger")
if((notisinstance(b,int)andnotisinstance(b,float))):
raiseTypeError("b,mustbeninteger")
return(int(a)+int(b))