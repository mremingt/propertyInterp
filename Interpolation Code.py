"""
Author: Michael Remington
Date: 6/20/2019

Code written to make repeated interpolation easy for heat transfer problems.

Inputs:
-------
    User prompted responses
    Property files in .txt format, labeled as material.txt that follow a specific 
    format. 
        properties
        units
        magnitude level

Outputs:
--------
    Temperature and associated property
    
"""

import numpy as np

running = True

while running == True:
    # Ask user for target temp. Convert to kelvin if Celsius.
    target = float(input('Temperature: '))
    
    # Check to make sure selection is either 1 or 2
    while True:
        try:
            v = int(input('If kelvin enter 1. If Celsius enter 2: '))
            
            if v > 2 or v < 1:
                raise ValueError
            
            break
        except (ValueError, KeyError):
            print('Oops! Not an available option.')
        
    if v == 2:
        target = target + 273
    
    # Ask user for material
    material = str(input('Material: '))
    material = material.lower()
    
    # Determines file to look at
    file = material+'.txt'
    
    # Property List
    propNames,units,powers = np.loadtxt(file,dtype=str,max_rows=3)
    prop_list = {propNames[x]: x for x in range(len(propNames))}
    
    # Develop selection options from file
    prop_list_to_print, unit_list_to_print,power_list_to_print = '','',''
    for item in list(prop_list):
        prop_list_to_print = prop_list_to_print + '\t' + item
    for item in list(units):
        unit_list_to_print = unit_list_to_print + '\t' + item
    for item in list(powers):
        power_list_to_print = power_list_to_print + '\t' + item
    
    print('Enter an item from first row')
    print(prop_list_to_print)
    print(unit_list_to_print)
    print(power_list_to_print)
    print('')
    
    
    # Trap User until they give a listed option
    while True:
        try:
            prop = str(input('Property: ')) # Ask user for desired property
            # Load values in desired columns
            temp, yValues = np.loadtxt(file, dtype=float, skiprows=3, usecols=(0,)+(prop_list[prop],), unpack=True)        
            break
        except (ValueError, KeyError):
            print('Oops! Not an available option.')
            
    
    ## Begin Interpolation
    # Check Target is within the table
    while True:
        try:
            if target > temp[-1] or target < temp[0]:
                raise ValueError
            else:
                break
        except ValueError:
            print("Oops! That temperature is not in this table")
            target = float(input('Temperature: '))
    
    
    if (target in temp): # Test for exact match in table
        print('')
        print('Temp','\t', prop)
        print(target,'\t', yValues[np.where(temp==target)[0][0]])
    else:
        for item in range(len(temp)): # Cycle through the list until target is between values
            if target > temp[item]:
                pass
            else:
                x2 = temp[item]
                x1 = temp[item-1]
                
                y2 = yValues[item]
                y1 = yValues[item-1]
                break
        
        
        target_y = (target - x1)/(x2-x1)*(y2 - y1) + y1 # Interpolate
    
        print('')
        print('Temp', '\t', prop)
        print(target, '\t', target_y)
        
    ## Ask if user wants to run again
    while True:
        try:
            runAgain = str(input("Run again?:y/[n] "))
            runAgain = runAgain.lower()
            if not((runAgain in ['y','n',''])):
                raise ValueError
            break
        except (ValueError):
            print("Oops.")
    
    if runAgain in ['y']:
        running = True
    elif runAgain in ['n','']:
        running = False
    else:
        running = False