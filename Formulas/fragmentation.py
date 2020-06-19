import math
x = 0 # datagram size
y = 0 # MTU size
z = 0 # Header size

'''
x = float(input("Enter Datagram size: "))
y = float(input("Enter MTU size: "))
z = float(input("Enter header size: "))
'''

x = 3250 # datagram size
y = 650 # MTU size
z = 50 # Header size

print(f"\nDatagram size: {x}, MTU: {y}, Header size: {z}")

def calc_frags(x,y,z):
	x = x - z # removing the header
	return math.ceil(x / (y - z))

def calc_offset(x,y,z,offset):
	return (y - z) / 8 + offset

def calc_table(x,y,z,frag_size):
	flag = 1
	offset = 0
	print(f"\nLength\tFrag flag\toffset")
	for frags in range(frag_size):
		print(f"{y}\t{flag}\t\t{offset}")

		offset = calc_offset(x,y,z,offset)
		# Calculates the length
		x = x - (y - z)
		# sets the last values for the length and flag
		if x < y:
			y = x
			flag = 0

frags = calc_frags(x,y,z)
print(f"Number of fragments: {frags}")
calc_table(x,y,z,frags)
