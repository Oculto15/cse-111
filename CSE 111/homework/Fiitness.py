# 03 Team Activity: Writing Functions



# bmr_women = 447.593 + 9.247 weight + 3.098 height − 4.330 age
# bmr_men = 88.362 + 13.397 weight + 4.799 height − 5.677 age










# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    gender = input("What is your gender? (M/F) ")
    birthdate = input("When is your birthdate? (in this format: YYYY-MM-DD) ")
    weight = float(input('What is your weight? (in U.S. pounds) '))
    height =  float(input('What is your height? (in U.S. inches) '))
    
    # Print the results for the user to see.
    years = compute_age(birthdate)
    kg = kg_from_lb(weight)
    cm = cm_from_in(height)
    bmi = body_mass_index(kg, cm)
    bmr = basal_metabolic_rate(gender, kg, cm, years)

    print(f"Age (years): {years}")
    print(f"Weight (kg): {kg:.2f}")
    print(f"Height (cm): {cm:.1f}")
    print(f"Body mass index: {bmi:.1f}")
    print(f"Basal metabolic rate (kcal/day): {bmr:.0f}")
    pass

# Compute the years
def compute_age(birthdate):
    
    # Convert a person's birthdate from a string to a date object.
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(weight):
    kg = weight * 0.45359237
    return kg


def cm_from_in(height):
    
    cm = height * 2.54
    return cm


def body_mass_index(weight, height):
    bmi = weight / (height ** 2) * 10000
    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    
    if gender.lower() == 'f':
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
    else:
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    return bmr
    

# Run this code to start the code
main()