
number=int(input('Please enter a  number to calculate the factorial of the number'))
#factorial=1
if number==1:
    print('factorial is',number)
else:
    for i in range(2,number+1):
        
        factorial=factorial*i
        i=i+1
    print('factorial is',factorial)
    
    
