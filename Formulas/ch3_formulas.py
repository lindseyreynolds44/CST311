# Chapter 3 Formulas

# SI Constants
kiloSI = 10 ** 3
megaSI = 10 ** 6
gigaSI = 10 ** 9

# JEDEC Constants
kiloJ = 2 ** 10
megaJ = 2 ** 20
gigaJ = 2 ** 30

#################### FORMULAS ######################

def getEstimatedRTT(a, estRTT, sampleRTT):
    result = ((1 - a) * estRTT) + (a * sampleRTT)
    return result

def getDevRTT(B, devRTT, estRTT, sampleRTT):
    result = ((1 - B) * devRTT) + (B * abs(sampleRTT - estRTT))
    return result

def getTimeoutInterval(a, B, initialEstRTT, initialDevRTT, samples):  
    devRTT = initialDevRTT
    estRTT = initialEstRTT

    for i in samples:
        estRTT = getEstimatedRTT(a, estRTT, i)
        devRTT = getDevRTT(B, devRTT, estRTT, i)
        print("Estimated: ", estRTT)
        print("Dev: ", devRTT, "\n")

    return estRTT + (4 * devRTT)

#################### Assignment 3  ######################

# ------- Assignment 3 Q8 Take TWO-------- #
a = .125
B = .25

'''
initialEstimatedRTT = 40.65
initialDevRTT = initialEstimatedRTT/2
samples = [30, 40, 100, 50]

timeout = getTimeoutInterval(a, B, initialEstimatedRTT, initialDevRTT, samples)
print("Assignment Total Timeout interval: ", timeout)

# ------- Worksheet 10 Q1-------- #
initialEstimatedRTT = 25
initialDevRTT = 5
samples = [10, 30, 25, 20, 100]

timeout = getTimeoutInterval(a, B, initialEstimatedRTT, initialDevRTT, samples)
print("Q1 Total Timeout interval: ", timeout)

# ------- Worksheet 10 Q2-------- #
initialEstimatedRTT = 175
initialDevRTT = 125
samples = [250, 300, 150, 200, 5]

timeout = getTimeoutInterval(a, B, initialEstimatedRTT, initialDevRTT, samples)
print("Q2 Total Timeout interval: ", timeout)
'''

# ------- 8 Again -------- #
initialEstimatedRTT = 0
initialDevRTT = initialEstimatedRTT/2
samples = [0, 0, 0.169277191, 0, 0.380126953, 0.290039063, 0.456054688, 0, 0]

timeout = getTimeoutInterval(a, B, initialEstimatedRTT, initialDevRTT, samples)
print("Q2 Total Timeout interval: ", timeout)




