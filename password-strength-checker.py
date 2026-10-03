import re

def check_password_strength(password):
    # Initialize counters
    score = 0
    feedback = []

    # Check length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8-12 characters long.")

    # Check for uppercase
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    # Check for lowercase
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    # Check for numbers
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Add numbers.")

    # Check for symbols
    if re.search(r'[\W_]', password):
        score += 1
    else:
        feedback.append("Add special symbols (e.g., !@#$%).")

    # Determine strength based on score
    if score >= 6:
        strength = "Strong 💪"
    elif score >= 4:
        strength = "Moderate ⚠️"
    else:
        strength = "Weak ❌"

    return strength, feedback

# --- Main Program ---
if __name__ == "__main__":
    print("🔐 Password Strength Checker")
    user_password = input("Enter a password to test: ")
    strength, suggestions = check_password_strength(user_password)
    
    print(f"\nPassword Strength: {strength}")
    if suggestions:
        print("Suggestions to improve:")
        for tip in suggestions:
            print(f" - {tip}")
