import sqlite3
from datetime import datetime

def mark_absentees():

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    today = datetime.now().strftime("%Y-%m-%d")

    # Get all registered students
    cursor.execute(
        "SELECT name FROM students"
    )

    all_students = [
        row[0]
        for row in cursor.fetchall()
    ]

    # Get today's present students
    cursor.execute(
        """
        SELECT name
        FROM attendance
        WHERE date=?
        AND status='Present'
        """,
        (today,)
    )

    present_students = [
        row[0]
        for row in cursor.fetchall()
    ]

   # Mark absentees
    # Mark absentees
    for student in all_students:

     if student not in present_students:

        cursor.execute(
            """
            SELECT *
            FROM attendance
            WHERE name=?
            AND date=?
            """,
            (student, today)
        )

        record = cursor.fetchone()

        if record is None:

            cursor.execute(
                """
                INSERT INTO attendance
                (name,date,time,status)
                VALUES(?,?,?,?)
                """,
                (
                    student,
                    today,
                    "--",
                    "Absent"
                )
            )

            print(f"{student} marked absent")

    conn.commit()
    conn.close()