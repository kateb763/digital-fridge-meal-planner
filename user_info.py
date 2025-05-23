class UserData:
    """
    Placeholder class for storing and managing user data.
    Can be expanded later to include methods and attributes for user profile management.
    """
    def __init__(self):
        pass

def get_user_input():
    """
    Prompts the user to input personal information needed for meal planning.

    Collects:
    - age (int)
    - gender (str)
    - weight in kilograms (int)
    - height in centimeters (int)

    Returns:
        dict: A dictionary containing the user's input data.
    """
    print("Welcome! Let's generate your meal plan.")

    age = int(input("Enter your age: "))
    gender = input("Enter your gender: ")
    weight = int(input("Enter your weight in kg: "))
    height = int(input("Enter your height in cm: "))
    
    # TODO: Additional inputs like activity level, 
    # goals, dietary preferences, and restrictions

    return {
        'age': age,
        'gender': gender,
        'weight': weight,
        'height': height,
    }

def calculate_bmr(user_profile):
    """
    Calculates the Basal Metabolic Rate (BMR) based on the Mifflin-St Jeor Equation.

    Parameters:
    - user_profile (dict): Dictionary containing user's age, gender, weight (kg), and height (cm).

    Returns:
    - float: Estimated BMR value.
    """
    weight = user_profile['weight']
    height = user_profile['height']
    age = user_profile['age']
    gender = user_profile['gender']

    if gender.lower() == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    return bmr
