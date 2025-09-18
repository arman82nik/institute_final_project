import sqlite3


def transaction_manager(sql_command, parameter_list=None, commit=False):
    connection = sqlite3.connect('./model/repository/class_project.db')
    cursor = connection.cursor()
    if parameter_list:
        cursor.execute(sql_command, parameter_list)
    else:
        cursor.execute(sql_command)
    if commit:
        connection.commit()
        result_list = parameter_list
    else:
        result_list = cursor.fetchall()
    cursor.close()
    connection.close()
    return result_list


def create_database():
    connection = sqlite3.connect('./model/repository/class_project.db')
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS classroom (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            teacher TEXT NOT NULL,
            start_date TEXT NOT NULL,
            end_date TEXT NOT NULL,
            start_time TEXT NOT NULL,
            end_time TEXT NOT NULL
        );
        """
    )


    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        person_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        family TEXT NOT NULL,
        gender TEXT NOT NULL,
        birthday TEXT NOT NULL
        
        )
        """



    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS project (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        project_name TEXT NOT NULL,
        file_url TEXT NOT NULL,
        date_time TEXT NOT NULL,
        score INTEGER NOT NULL
        );
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS register (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        person_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        family TEXT NOT NULL,
        curse_number INTEGER NOT NULL,
        phone_number INTEGER NOT NULL
        
        )
        
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS lessons (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        person_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        code INTEGER NOT NULL,
        teacher TEXT NOT NULL,
        units INTEGER NOT NULL
        )
        
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_id INTEGER NOT NULL,
        student_id INTEGER NOT NULL,
        session_number INTEGER NOT NULL,
        present INTEGER NOT NULL,
        class_type TEXT NOT NULL
        );
        """
    )

    cursor.close()
    connection.close()