def  calculate_bmi(weight, height):

    bmi = (weight/(height**2)) * 703

    """print("your bmi is", bmi)"""

    if bmi < 18.5:
        print('your bmi is ' , bmi ,'you are underweight')
    elif 18.5 <= bmi < 25:
        print('your bmi is' , bmi , 'you are normal weight')
    elif 25 <= bmi < 30:
        print('your bmi is' , bmi , 'you are over weight')
    else:
        print('your bmi is' , bmi , 'you are obese')

weight = input("what is your weight? (please enter in pounds) ")
height = input("what is your height? (please enter in inches) ")
height = int(height)
weight = int(weight)

calculate_bmi(weight, height)