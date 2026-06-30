def check_strength(password):

    if len(password) < 6:

        return "Weak"

    elif len(password) < 10:

        return "Medium"

    else:

        return "Strong"