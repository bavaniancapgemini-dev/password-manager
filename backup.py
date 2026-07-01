import shutil
import os
from datetime import datetime

def create_backup():

    if not os.path.exists("backups"):

        os.makedirs("backups")

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    backup_name = f"backups/passwords_{timestamp}.db"

    shutil.copy(
        "passwords.db",
        backup_name
    )