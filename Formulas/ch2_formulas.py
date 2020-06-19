# SI Constants
kiloSI = 10 ** 3
megaSI = 10 ** 6
gigaSI = 10 ** 9

# JEDEC Constants
kiloJ = 2 ** 10
megaJ = 2 ** 20
gigaJ = 2 ** 30

#################### FORMULAS ######################

# Time to send object over access link (L/R)
def transmissionDelay(L, R):
    result = L/R
    return result

# Time for bits to propogate over link
def propogationDelay(d, s):
    result = d/s
    return result

# Equation from Assignment 2
# A = transmission delay
# B = Arrival rate or "request rate"
def averageAccessDelay(A, B):
    result = A / (1 - A*B)
    return result

def responseTimeWithCache(missRate, accessTime):
    hitRate = 1 - missRate
    result = (hitRate * .01) + (missRate * accessTime)
    return result

def clientServerDistributionTime(N, F, Us, d):
    equ1 = (N * F) / Us
    equ2 = F / d
    return max(equ1, equ2)


def getSummation(N, Ui):
    sum = 0
    for x in range(1, N):
        sum = sum + Ui
    return sum


def P2PDistributionTime(F, Us, d, N, Ui):
    equ1 = F / Us
    equ2 = F / d
    equ3 = (N * F) / (Us + getSummation(N, Ui))

    return max(equ1, equ2, equ3)




#################### Assignment 2 ######################
'''
# ------- Problem 1 -------- #
L = 850000
R = 15 * megaSI
B = 16 # arrival rate of objects 
internetDelay = 3

# Calculations
A = transmissionDelay(L, R) # average time required to send object over the link
accessDelay = averageAccessDelay(A, B) 
totalResponseTime = accessDelay + internetDelay

print("average access delay ", totalResponseTime)


# ------- Problem 2 -------- #
missRate = .4
B = B * .4

# Calculations
accessDelay = averageAccessDelay(A, B)
responseTime = accessDelay + internetDelay
result = responseTimeWithCache(missRate, responseTime) # 0.6(.01) + 0.4(responseTime)
                                                       # Time w/ cache + w/ internet

print("average access delay with cache ", result)

'''
# ------- Problem 5 Client-Server VS P2P Architecture -------- #
'''
F = 15 * gigaJ
Us = 30 * megaSI
d = 2 * megaSI

for i in range(1, 4):
    N = 10 ** i

    Ui = 300 * kiloSI
    P2PTime = P2PDistributionTime(F, Us, d, N, Ui)
    csTime = clientServerDistributionTime(N, F, Us, d)
    print("P2P with ", N, " and ", Ui, "--", P2PTime)
    print("client server time: ", csTime)

    Ui = 700 * kiloSI
    P2PTime = P2PDistributionTime(F, Us, d, N, Ui)
    csTime = clientServerDistributionTime(N, F, Us, d)
    print("P2P with ", N, " and ", Ui, "--", P2PTime)
    print("client server time: ", csTime)

    Ui = 2 * megaSI
    P2PTime = P2PDistributionTime(F, Us, d, N, Ui)
    csTime = clientServerDistributionTime(N, F, Us, d)
    print("P2P with ", N, " and ", Ui, "--", P2PTime)
    print("client server time: ", csTime, "\n\n")

'''

F = 7 * gigaSI
Us = 99 * megaSI
d = 23 * megaSI
N = 5
Ui = 11 * megaSI

P2PTime = P2PDistributionTime(F, Us, d, N, Ui)
csTime = clientServerDistributionTime(N, F, Us, d)
print("P2P with ", N, " and ", Ui, "--", P2PTime)
print("client server time: ", csTime)

'''
L = 900 * 8 * kiloJ
R = 1 * megaSI
td = transmissionDelay(L, R)
print("Trans delay: ", td)
'''










