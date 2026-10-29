"""Calculate BMI from weight and height and print its category."""

weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))

bmi = weight / height ** 2
print(f"BMI: {bmi:.1f}")

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal"
elif 25 <= bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print("Category:", category)
