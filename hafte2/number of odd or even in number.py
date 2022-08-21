number=float(input('please enter your number:\n'))
odd=0
even=0

while number>0:
    mod=number%10
    number=number//10
    if mod%2==0:
        even=even+1
    else:
        odd=odd+1
if odd==even:
    print('number of odd equal with even.')
elif odd>even:
    print('number of odd is more than even. ')
else:
    print('number of even is more than odd.')    