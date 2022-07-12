# Python Program to Solve Quadratic Equation

# Quadratic equation is ax^2 +bx +c =0
# use complex math module

import cmath

a = int (input("Enter value of a: "))
b = int (input("Enter value of b: "))
c = int (input("Enter value of c: "))
print ("Given Quadratic equation is :")
print ("{0}x**2 +{1}x+{2} =0".format(a,b,c))

#Calculating discriminat 
discriminant = (b**2)-(4*a*c)

#finding solutions of quadratic equations
solution1 = (-b - cmath.sqrt(discriminant))/(2*a)
solution2 = (-b + cmath.sqrt(discriminant))/(2*a)

#printing two solutions
print ("Solutions are {0} and {1} ".format(solution1,solution2))
