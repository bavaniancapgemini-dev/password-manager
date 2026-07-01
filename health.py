def analyze_passwords(data):

    weak = 0

    reused = 0

    passwords = []

    for row in data:

        password = row[3]

        if len(password) < 8:

            weak += 1

        if password in passwords:

            reused += 1

        passwords.append(password)

    total = len(data)

    if total == 0:

        score = 100

    else:

        deductions = (weak * 10) + (reused * 15)

        score = max(
            0,
            100 - deductions
        )

    return {

        "weak": weak,

        "reused": reused,

        "score": score

    }