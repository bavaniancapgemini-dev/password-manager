def password_advice(password):

    advice = []

    if len(password) < 8:

        advice.append(
            "Increase password length"
        )

    if password.islower():

        advice.append(
            "Add uppercase letters"
        )

    if password.isalpha():

        advice.append(
            "Add numbers/symbols"
        )

    if len(advice) == 0:

        return "Excellent Password"

    return "\n".join(advice)