import sqlite3

conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

cursor.execute("""
SELECT *
FROM attendance
ORDER BY date DESC, time DESC
""")

records = cursor.fetchall()

print("\nAttendance Records\n")

for row in records:
    print(row)

conn.close()