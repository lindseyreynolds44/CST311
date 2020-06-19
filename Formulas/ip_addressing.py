import math

# Takes a decimal value between 0 and 255 and converts it to an 8 bit
# binary number 
def convertDecimalToBinary(decimal):
    binary = ""
    index = 128
    while index >= 1:
        if decimal - index >= 0:
            binary = binary + "1"
            decimal = decimal - index
        else:
            binary = binary + "0"
        index = index / 2
    return binary

# Takes a dotted decimal IP address and prints its binary equivalent
def printDecimalToBinaryIP(address):
    DDValues = address.split(".")
    binaryValues = [""] * 4

    for i in range(0,4):
        binaryValues[i] = convertDecimalToBinary(int(DDValues[i]))

    print(binaryValues[0],binaryValues[1],binaryValues[2],binaryValues[3])


#----------- Questions -----------#

ipAddress = "223.2.7.14"

printDecimalToBinaryIP(ipAddress)  

for x in range(1, 21):
    if(x % 2 == 1):
        print(x)



