from datetime import datetime

LOG_FILE = "activity.log"

def log_activity(action):

    time = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    with open(
        LOG_FILE,
        "a"
    ) as file:

        file.write(

            f"[{time}] {action}\n"

        )
