#import SymPy
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [1,2,3,4,5,6,7,8,9,10]
c = [1,2,3,4,5,6,7,8]
d=[]
for i in range(1,51):
    d.append(i)
list1 = [x for x in range(len(a)) if x % 2 == 0]
list2 = [x**2 for x in range(len(b)) if x % 2 == 1]
list3 = [x**2 for x in range(len(c)) if x % 2 == 1]
print(list1)
print(list2)
print(list3)
#print(list(sympy.primerange(0, 50)))
