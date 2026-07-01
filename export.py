import csv

def export_to_csv(data):

    with open(
        "password_export.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow(
            [
                "Website",
                "Username",
                "Password",
                "Category",
                "Notes"
            ]
        )

        for row in data:

            writer.writerow(
                [
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5]
                ]
            )