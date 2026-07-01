def check_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char in "!@#$%^&*" for char in password):
        score += 1

    if score <= 1:
        return "Weak"

    elif score <= 3:
        return "Medium"

    else:
        return "Strong"