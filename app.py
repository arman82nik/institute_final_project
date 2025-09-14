print("app started")

from model.repository.database_manager import create_database
create_database()
print("Database created")


import test.course_test

