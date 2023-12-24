# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 22:18:46 2023

@author: smith
"""

#PassingUnderPacev0.9
while True: #starts loop

    #variables
    trklen = float(input("What is the track length in miles: "))
    laps = float(input("Number of laps completed: " ))
    hh = float(input("Hours: ")*3600)
    mm = float(input("Minutes: ")*60)
    ss = float(input("Seconds: "))
    time = (hh + mm + ss)
    fullrun = (trklen * laps)
    avgmph = ((fullrun / time)*3600)
    
    print(avgmph)
        
    inp = input("Continue? y/n: ")
    if inp.lower() == 'n':
        print("Exiting...")
        break
    