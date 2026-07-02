def generate_notifications(analysis):

    notifications = []

    if analysis["weak"] > 0:

        notifications.append(
            "⚠ Weak passwords detected"
        )

    if analysis["reused"] > 0:

        notifications.append(
            "⚠ Duplicate passwords found"
        )

    if analysis["score"] < 70:

        notifications.append(
            "⚠ Vault security is low"
        )

    if len(notifications) == 0:

        notifications.append(
            "✅ Vault security excellent"
        )

    return notifications