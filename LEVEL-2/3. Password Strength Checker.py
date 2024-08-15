import re

def evaluate_password_strength(password):
    # Define criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    
    # Count how many criteria are met
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])
    
    # Evaluate the password strength based on the criteria met
    if criteria_met == 5:
        return "Strong"
    elif criteria_met == 4:
        return "Moderate"
    else:
        return "Weak"

def main():
    # Prompt the user to enter a password
    password = input("Enter a password to evaluate its strength: ")
    strength = evaluate_password_strength(password)
    print(f"The strength of your password is: {strength}")

if __name__ == "__main__":
    main()