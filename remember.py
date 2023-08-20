string =input("Enter a word:" )
all_freq = {} 
for i in string:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
  
print ("Count of all characters in GeeksforGeeks is :\n "+  str(all_freq))

my_list=[1,2,3,4]
my_list[3]=2
print(my_list)

x=0
if not x>0:
    print('x is  greater than 0')
else:
    print('x is not greater than 0')

string1="hello"
string2="hello"
result=string1 is string2
print(result)

a=[1,2,3]
b=[1,2,3]
result=a is not b
print(result)

b=5<2
print(b)
