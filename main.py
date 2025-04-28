def check_password_strength(password):
    """
    Evaluates password strength based on:
    - Length
    - Presence of uppercase letters
    - Presence of lowercase letters
    - Presence of numbers
    - Presence of special characters
    
    Returns a rating of "Weak", "Moderate", or "Strong" along with specific feedback.
    """
    # Initialize score and feedback
    score = 0
    feedback = []
    
    # Check length
    if len(password) < 8:
        feedback.append("Password is too short (minimum 8 characters recommended)")
    elif len(password) >= 12:
        score += 2
        feedback.append("Good length")
    else:
        score += 1
        feedback.append("Adequate length, but longer passwords are stronger")
    
    # Check for uppercase letters
    if any(c.isupper() for c in password):
        score += 1
        feedback.append("Contains uppercase letters")
    else:
        feedback.append("Missing uppercase letters")
    
    # Check for lowercase letters
    if any(c.islower() for c in password):
        score += 1
        feedback.append("Contains lowercase letters")
    else:
        feedback.append("Missing lowercase letters")
    
    # Check for numbers
    if any(c.isdigit() for c in password):
        score += 1
        feedback.append("Contains numbers")
    else:
        feedback.append("Missing numbers")
    
    # Check for special characters
    import string
    special_chars = string.punctuation
    if any(c in special_chars for c in password):
        score += 1
        feedback.append("Contains special characters")
    else:
        feedback.append("Missing special characters")
    
    # Evaluate overall strength
    if score >= 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    return strength, feedback

def main():
    print("Password Strength Checker")
    print("========================")
    
    while True:
        password = input("\nEnter a password to check (or 'quit' to exit): ")
        
        if password.lower() == 'quit':
            print("Goodbye!")
            break
        
        strength, feedback = check_password_strength(password)
        
        print(f"\nPassword Strength: {strength}")
        print("Feedback:")
        for item in feedback:
            print(f"- {item}")
        
        if strength == "Weak":
            print("\nTip: Try adding more character types and increasing length.")
        elif strength == "Moderate":
            print("\nTip: Add more varieties of characters to make your password stronger.")

if __name__ == "__main__":
    main()
