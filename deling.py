import math

a = int(input("geef het eerste getal: "))
b = int(input("geef de deler:"))

x = divmod(a,10)
i1 = x[0]
i0 = x[1]

print(i1, " ", i0)
rest1 = divmod(i1,b)[1]
print(str(i1) + " gedeeld door " + str(b) + " geeft " + str(int(i1/b)) + " en rest "+ str(rest1))

rest2 = rest1*10 + i0
rest3 = divmod(rest2,b)
print(str(rest2) + " gedeeld door " + str(b) + " geeft " +str(rest3[0]) + " en rest " + str(rest3[1]))
sum = int(i1/b)*10 + rest3[0]
print(str(sum) + " maal " + str(b) + " geeft " + str(sum*b))