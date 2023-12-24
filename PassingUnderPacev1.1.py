# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 22:18:46 2023

@author: smith
"""

# PassingUnderPacev1.0
while True:  # starts loop

    # variables
    trklen = float(input("What is the track length in miles: "))
    laps = float(input("Number of laps completed: "))
    hh = float(input("Hours: "))
    mm = float(input("Minutes: "))
    ss = float(input("Seconds: "))
    time = hh + mm / 60 + ss / 3600  # Convert minutes and seconds to hours
    fullrun = trklen * laps
    avgmph = fullrun / time

    print("Average Speed (MPH): {:.2f}".format(avgmph))

    inp = input("Continue? y/n: ")
    if inp.lower() == 'n':
        print("Exiting...")
        break
