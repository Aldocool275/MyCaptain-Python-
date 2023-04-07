from math import pi
r=float(input("Enter the radius:"))
Area=pi*r**2
print("The Area of the circle with radius 1.1 is:",Area)

file=input('Enter the file name:')
f=file.split(".")
print("The extension of the file is " + repr(f[-1]))