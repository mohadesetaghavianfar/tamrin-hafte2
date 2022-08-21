user = ('mohadeseth')
psw = ('1381')

x=0
print('Please Enter Your UserName And Your Password In 3Time\n')



while x<3:
    user1=input('you can enter your user hear:\t')
    psw1=input('you can enter your psw hear:\t')
    if (psw==psw1) and (user==user1) :   
        print('Hello!\n Welcome To Your Account.')
        break
    elif user != user1 or psw!=psw1:
        print('Oh!!!! I am So Sorry! You Are WROng,Please Enter Your Information Again :(\n')
    x=x+1
if x>2:
        print('YOU CAN NAT ENTER YOUR INFORMATION AGAIN!\n SORRY!!!!!')   

 
    
   

