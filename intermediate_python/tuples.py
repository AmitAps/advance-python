#Tuples: ordered, immutable, allows duplicate elements
mytuple = ("Amit", 28, "chhapra")
print(mytuple)

singletuple = ("Amit",)
print(type(singletuple))
for x in mytuple:
    print(x)

mytuple1 = ('a', 'p', 's', 'd', 'k', 'p')

print(mytuple1.count('p'))

print(mytuple1.index('p'))

# mytuple2 = "amitpratapsingh sahadi chhapra"
#
# print(mytuple2.count('sahadi'))

import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000))
