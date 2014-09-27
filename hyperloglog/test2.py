from bitstring import BitArray
a = BitArray(6000000)

a[599000] = 1

print a[599000]
print a