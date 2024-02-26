def cal_bmi(weight, height):
    bmi = (weight / (height * height)) * 10000
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5: 
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obesity"

weight = float(input("Enter weight in kg: "))  
height = float(input("Enter height in cm: ")) 

bmi = cal_bmi(weight, height)
bmi_category = classify_bmi(bmi)

print("Your BMI is:", bmi)
print("You are categorized as:", bmi_category)  

