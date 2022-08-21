temperature=float(input('please enter your temperture:\n'))
type_temperature1=input('please enter your first temperature: 1=c\t 2=f\t 3=k\n')
type_temperature2=input('please enter your second temperature: 1=c\t 2=f\t 3=k\n')


if type_temperature1=='c' and type_temperature2=='f':  #تبدیل سیلسیوس به فارنهایت
    fahrenheit=((temperature)*(9/5))+32    # or 9/5==66.6
    print('result of your temperature conversion is:', fahrenheit)
elif type_temperature1=='f' and type_temperature2=='c': #تبدیل فارنهایت به سیلسیوس
    celsius=(temperature-32)*(5)/(9)
    print('result of your temperature conversion is:',celsius)
elif type_temperature1=='f' and type_temperature2=='k' :  #تبدیل فارنهایت به کلوین
    kelvin=(5/9)*(temperature-32)+273
    print('result of your temperature conversion is:',kelvin)
elif type_temperature1=='k' and type_temperature2=='f':   #تبدیل کلوین به فاذنهایت
    fahrenheit=(temperature-273.15)*(5/9)+32
    print('result of your temperature conversion is:',fahrenheit)
elif type_temperature1=='c' and type_temperature2=='k':   #تبدیل سیلسیوس به کلوین
    kelvin=temperature+273.15
    print('result of your temperature conversion is:',kelvin)
elif type_temperature1=='k' and type_temperature2=='c':
    celsius=temperature-273.15
    print('result of your temperature conversion is:',celsius)
else:
    print('please enter your temperature again!')