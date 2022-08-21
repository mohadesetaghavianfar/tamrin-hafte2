makus=int(input('please enter the oposite of number:\n'))
number=makus
counter=0


while makus>0:
    temp = makus % 10
    counter = (counter*10) + temp
    makus = makus // 10
if number == counter:
    print('YES :)')
if number != counter:
    print('NO :(')

