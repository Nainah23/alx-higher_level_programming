#!/usr/bin/python3
"""Definesafnthatindentstext"""
deftext_indentation(text):
"""
printsatextwith2newlinesaftereachofthesecharacters:.,?and:

Args:
text(str):printedtext
Raises:
TypeError:Iftext!=string
"""
ifnotisinstance(text,str):
raiseTypeError("textmustbeastring")
x=0
whilex<len(text)andtext[x]=='':
x+=1
whilex<len(text):
print(text[x],end="")
iftext[x]=="\n"ortext[x]in".?:":
iftext[x]in".?:":
print("\n")
x+=1
whilex<len(text)andtext[x]=='':
x+=1
continue
x+=1
