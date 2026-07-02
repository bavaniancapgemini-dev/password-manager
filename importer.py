import csv

from database import save_password_db

def import_csv(

    filepath,
    owner

):

    with open(
        filepath,
        "r"
    ) as file:

        reader = csv.reader(file)

        next(reader)

        for row in reader:

            save_password_db(

                row[0],

                row[1],

                row[2],

                row[3],

                row[4],

                owner

            )