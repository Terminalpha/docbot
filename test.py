# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 10:56:43 2021

@author: nicol
"""

import openingnames

new_openingnmes=list(openingnames.openingnames_short)
openings=[]
for opening in new_openingnmes :
    k=[]
    j=opening.split("{%%")
    change=j[0].replace("1.","")
    change=change.replace("2.","")
    change=change.replace("3.","")
    change=change.replace("4.","")
    change=change.replace("5.","")
    change=change.replace("6.","")
    change=change.replace("7.","")
    change=change.replace("8.","")
    change=change.replace("9.","")
    change=change.replace("10.","")
    change=change.replace("11.","")
    change=change.replace("12.","")
    change=change.replace("13.","")
    change=change.replace("14.","")
        
    check=[change.split(),j[1].replace("%%}","")]
    openings.append(check)
        