from model.entity.student import Student

class StudentMapper:

    @staticmethod
    def form_to_entity(form):
        """
        ورودی: آبجکت فرم یا View (دارای متد get() برای فیلدها)
        خروجی: یک شیء Student
        """
        return Student(
            student_id=form.student_id.get() if hasattr(form.student_id, "get") else form["student_id"],
            name=form.name.get() if hasattr(form.name, "get") else form["name"],
            age=form.age.get() if hasattr(form.age, "get") else form["age"],
            gender=form.gender.get() if hasattr(form.gender, "get") else form["gender"],
            birthday=form.birthday.get() if hasattr(form.birthday, "get") else form["birthday"],
            email=form.email.get() if hasattr(form.email, "get") else form["email"],
        )

    @staticmethod
    def entity_to_dict(student: Student):
        """
        ورودی: یک شیء Student
        خروجی: دیکشنری برای نمایش در جدول یا JSON
        """
        return {
            "id": student.id,
            "student_id": student.student_id,
            "name": student.name,
            "age": student.age,
            "gender": student.gender,
            "birthday": student.birthday,
            "email": student.email
        }