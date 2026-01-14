def check_password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
        print("Length is at least 8 characters")
    else:
        print(" Password too short")

    if any(char.isupper() for char in password):
        score += 1
        print(" Contains uppercase letter")
    else:
        print(" No uppercase letter")

    if any(char.islower() for char in password):
        score += 1
        print(" Contains lowercase letter")
    else:
        print(" No lowercase letter")

    if any(char.isdigit() for char in password):
        score += 1
        print(" Contains number")
    else:
        print(" No number")

    if any(char in "!@#$%^&*()-_+=<>?/{}[]" for char in password):
        score += 1
        print(" Contains special character")
    else:
        print(" No special character")

    print("\nPassword Strength Result:")
    if score <= 2:
        print(" WEAK PASSWORD")
    elif score == 3 or score == 4:
        print(" MEDIUM PASSWORD")
    else:
        print(" STRONG PASSWORD")
password = input("Enter your password: ")
print()
check_password_strength(password)
