string1 = input("Enter the string to check: ")
j=len(string1)
splitted_word=string1.split()
string2=[]
for i in range(1,j+1):
    string2.append(string1[-i])
    #print(string1[-i],end="")
    string3 = ''.join(string2);

if(string3 == string1):
    print("String is Palindrome")
else:
    print("String is not a Palindrome")

