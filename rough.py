import random
a=[]
n=int(input("Enter number of elements:"))
for j in range(n):
    a.append(random.randint('h','r','t'))
print('Randomised list is: ',a)
