import sqlite3

def register_student(name):

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO students(name) VALUES(?)",
            (name,)
        )

        conn.commit()
        print(f"{name} registered successfully")

    except:
        print(f"{name} already exists")

    conn.close()


student_name = input("Enter student name: ")
register_student(student_name)