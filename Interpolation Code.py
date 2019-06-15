import numpy as np

# Ask user for target temp. Convert to kelvin if Celsius.
target = float(input('Temperature: '))
v = int(input('If kelvin enter 1. If Celsius enter 2: '))

# Check to make sure selection is either 1 or 2
if v == 2:
    target = target + 273
elif v > 2 or v < 1:
    raise ValueError('Not a valid entry.')

# Ask user for material
material = str(input('Material: '))
material = material.lower()

# Ask user for desired property
prop = str(input('Property: '))

# Property List
prop_list = {'rho':1, 
             'cp':2}


file = material+'.txt'

temp, yValues = np.loadtxt(file, dtype=float, delimiter='\t', skiprows=1, usecols=(0,)+(prop_list[prop],), unpack=True)

## Begin Interpolation
if target > temp[-1] or target < temp[0]: # Check Target is within in table
    raise ValueError("Oops! That temperature is not in this table")
    
if (target in temp): # Test for exact match in table
    print('\n',target, yValues[np.where(temp==target)[0][0]])
else:
    for item in range(len(temp)): # Cycle through the list until target is between values
        if target > temp[item]:
            pass
        else:
            x2 = temp[item]
            x1 = temp[item-1]
            
            y2 = yValues[item]
            y1 = yValues[item-1]
    
    
            target_y = (target - x1)/(x2-x1)*(y2 - y1) + y1 # Interpolate

    print('\n',target, target_y)