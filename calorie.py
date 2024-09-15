#Calorie intake calculator
#from Medium article Arth Awasthi, A Step-by-Step Guide on How to Build a Calorie Intake Calculator in Python
# https://faun.pub/a-step-by-step-guide-on-how-to-build-a-calorie-intake-calculator-in-python-12ea72ec9e8c
# gather user info
full_name = input('what is your full name? ')
sex = input('enter your sex (male or female) ')
age = int(input('What is your age? '))
height = int(input('What is your height in centimeters? '))
weight = int(input('Enter your weight in kilograms '))
activity_level = input('enter your activity level (sedentary, lightly active, moderately active, very active) ')
weight_change = input('Enter your desired weight program (lose weight, maintain weight, gain weight) ')

# use Harris Benedict equation to calculate Basal metabolic rate. 
def calculate_bmr(weight, height, age, sex):
    if sex == 'male':
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
    return bmr

# you can calculate your Total Daily Energy Expenditure by multiplying your BMR by your activity level.
def calculate_daily_calories(bmr, activity_level):
    if activity_level == 'sedentary':
        calories = bmr * 1.2
    elif activity_level == 'lightly active':
        calories = bmr * 1.375
    elif activity_level =='moderately active':
        calories = bmr * 1.55
    else:
        calories = bmr * 1.725
    return calories

# weight change section
def calculate_weight_change(weight):
    if weight_change == 'lose weight':
        calorie_level = (calories - 500)
    elif weight_change == 'maintain weight':
        calorie_level = (calories)
    else:
        calorie_level = (calories + 500)
    return calorie_level
        

# user results
bmr = calculate_bmr(weight, height, age, sex)
calories = calculate_daily_calories(bmr, activity_level)
calorie_level = calculate_weight_change(weight)

print('Hi', full_name, 'your daily calorie needs are ',round(calories), 'kcal')
print('To', weight_change, 'your daily calorie intake is', round(calorie_level), 'kcal')
