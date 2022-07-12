
#Program for Binary to Decimal Conversion

binary = int(input("Enter Binary Number :"))
decimal =0
i=0
while (binary >0):
    rem = binary %10
    decimal = decimal + rem *(2 ** i)    #multiplying remainder with ith power of 2
    binary = int(binary/10)
    i = i+ 1

print("Eqivalent Decimal number :", decimal)
