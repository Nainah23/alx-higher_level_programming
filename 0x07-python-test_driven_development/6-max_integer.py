#!/usr/bin/python3
"""Moduletofindthemaxintegerinalist
"""


defmax_integer(list=[]):
"""Functiontofindandreturnthemaxintegerinalistofintegers
Ifthelistisempty,thefunctionreturnsNone
"""
iflen(list)==0:
returnNone
result=list[0]
i=1
whilei<len(list):
iflist[i]>result:
result=list[i]
i+=1
returnresult

