# BMI مناسب هر گروه سنی:
# 19-24 age--->22
# 25-34--->23
# 35-44--->24
# 45-54--->25
# 55-64--->26
# more than 65--->27

from telnetlib import BM
age=int(input('please enter your age:\n'))
height=float(input('please enter your height in meter:\n'))
weight=float(input('please enter your weight in kg:\n'))

BMI=weight/(height**2)
print(BMI)
if BMI<16.5:
    print('BMI is:', BMI , '\t kambod vazn shadid!!!!!')
elif 16.5<BMI<18.5:
    print('BMI is:', BMI , '\t kambod vazn!')
elif 18.5<BMI<25:
    print('BMI is:', BMI , '\t vazn adi.')
elif 25<BMI<30:
    print('BMI is:', BMI , '\t azafe vazn :( ')
elif 30<BMI<35:
    print('BMI is:', BMI , '\t  chaghi mamoli (first type)')
elif 35<BMI<40:
    print('BMI is:', BMI , '\t chaghi shadid (second type)')
elif BMI>40:
    print('BMI is:', BMI , '\t chaghi besiar shadid (third type)' )
else:
    print('please enter your information again.')
