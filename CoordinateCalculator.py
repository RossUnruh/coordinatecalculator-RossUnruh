##-------------------------------------------------------------------------------------
## Name:  CoordinateCalculator.py
## Description:  Converts geographic coordinates in DDMMSS format to DD
## Created:  September 4th, 2024
## Author:  Ross Unruh (rossu@ksu.edu) (with a lot of help from Dr. Hutchinson's code he showed in class on 9/4/2024)
## Python Version: 3.12.0
##-------------------------------------------------------------------------------------

# Request user-suppliesd coordinates in DDMMSS format:
x = input('Please enter a coordinate value in DDMMSS format:    ')

#Convert seconds to minutes
# The negative 2 takes the last two inputs from the user.
ss = int(x[-2:]) / 60

# Add converted seconds to minutes and convert to degrees.
mm = (int(x[-4:-2:]) + ss) / 60

# Add converted minutes to degrees.
dd = int(x[:2]) + mm

# Print the final result with a friendly message.
print('Your coordinate in decimal degrees is {0}'.format(str(round(dd,2))))
