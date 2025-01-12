number=int(input("enter a number: "))
if number > 0:
    print("Positive number")
elif number == 0:
    print('Zero')
else:
    print('Negative number')

for num in range(1, 11):
    if num == 10:
        break
    else:
        print(num)
# ths is a comment 