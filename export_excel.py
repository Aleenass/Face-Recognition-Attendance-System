import sqlite3
import pandas as pd

conn = sqlite3.connect("attendance.db")

query = """
SELECT *
FROM attendance
"""

df = pd.read_sql_query(query, conn)

df.to_excel(
    "Attendance_Report.xlsx",
    index=False
)

conn.close()

print("Excel report generated!")