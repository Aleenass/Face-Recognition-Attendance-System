import sqlite3
from datetime import datetime


def mark_attendance(name):

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    today = datetime.now().strftime("%Y-%m-%d")

    cursor.execute(
        """
        SELECT * FROM attendance
        WHERE name=? AND date=?
        """,
        (name, today)
    )

    record = cursor.fetchone()

    if record is None:

        current_time = datetime.now().strftime("%H:%M:%S")

        cursor.execute(
            """
            INSERT INTO attendance
            (name,date,time,status)
            VALUES(?,?,?,?)
            """,
            (
                name,
                today,
                current_time,
                "Present"
            )
        )

        conn.commit()

        print(f"{name} marked present")

    conn.close()