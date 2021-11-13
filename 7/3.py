w=input('weight= ')
h=input('height= ')
weight=''
height=''
for i in range(0, len(w)):
    weight+=w[i]
for i in range(0, len(h)):
   height+=h[i]
bmi=int((float(weight)/(float(height)*float(height)))+1)

if bmi<18.5: print('Your BMI is '+str(bmi)+', you are underweight.')
elif bmi>18.5 and bmi>25: print('Your BMI is '+str(bmi)+', you are have a normal weight.')
elif bmi>=25 and bmi<30: print('Your BMI is '+str(bmi)+', you are slightly overweight.')
elif bmi>=30 and bmi<35: print('Your BMI is '+str(bmi)+', you are obese.')
elif bmi>=35: print('Your BMI is '+str(bmi)+', you are clinically obese.')