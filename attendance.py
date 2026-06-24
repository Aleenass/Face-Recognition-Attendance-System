from datetime import datetime
import csv
import os

def mark_attendance(name):

    filename = "attendance/attendance.csv"

    if not os.path.exists("attendance"):
        os.makedirs("attendance")

    already_marked = []

    if os.path.exists(filename):

        with open(filename, "r", newline="") as file:

            reader = csv.reader(file)

            for row in reader:
                if len(row) > 0:
                    already_marked.append(row[0])

    if name not in already_marked:

        now = datetime.now()

        date = now.strftime("%Y-%m-%d")
        time = now.strftime("%H:%M:%S")

        with open(filename, "a", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                name,
                date,
                time,
                "Present"
            ])

        print(f"{name} attendance marked")